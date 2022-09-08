package api

import (
	"fmt"
	"github.com/Funkit/go-utils/apierror"
	"github.com/Funkit/satellite-data-provider/api-composer/sattrack"
	"github.com/Funkit/satellite-data-provider/pointing"
	"github.com/Funkit/tle-provider/data"
	"github.com/go-chi/chi/v5"
	"github.com/go-chi/render"
	"log"
	"net/http"
	"time"
)

type ScheduleQuery struct {
	Constellation  string
	StartDate      time.Time
	StopDate       time.Time
	MinPassLength  int32
	GroundStations []*pointing.GroundStationInformation
}

func (sq *ScheduleQuery) Bind(r *http.Request) error {
	return nil
}

type Server struct {
	c         sattrack.Source
	router    chi.Router
	tleSource data.Source
	port      int
}

func NewServer(port int, procClient sattrack.Source, tleProvider data.Source) *Server {
	return &Server{
		c:         procClient,
		tleSource: tleProvider,
		router:    chi.NewRouter(),
		port:      port,
	}
}

func (s *Server) AddMiddlewares(middlewares ...func(handler http.Handler) http.Handler) {
	s.router.Use(middlewares...)
}

func (s *Server) SubRoutes(baseURL string, r chi.Router) {
	s.router.Mount(baseURL, r)
}

func (s *Server) Run() error {
	log.Printf("Listening on port %v\n", s.port)

	if err := http.ListenAndServe(fmt.Sprintf(":%v", s.port), s.router); err != nil {
		panic(err)
	}
	return nil
}

func (s *Server) InitializeRoutes() {
	s.router.Post("/schedule/{constellation}", s.getConstellationSchedule())
}

func (s *Server) getConstellationSchedule() http.HandlerFunc {
	return func(w http.ResponseWriter, r *http.Request) {

		var schedReq ScheduleQuery

		if err := render.Bind(r, &schedReq); err != nil {
			apierror.Handle(w, r, apierror.Wrap(err, apierror.ErrRender))
			return
		}

		constellation, err := s.tleSource.GetConstellation(schedReq.Constellation)
		if err != nil {
			apierror.Handle(w, r, apierror.Wrap(err, apierror.ErrNotFound))
			return
		}

		var buffer []*pointing.SatMon

		for _, sat := range constellation {
			buffer = append(buffer, &pointing.SatMon{
				SatelliteInformation: &pointing.SatelliteInformation{
					Name:      sat.SatelliteName,
					TleLine_1: sat.TLELine1,
					TleLine_2: sat.TLELine2,
				},
				MinimumPassLengthSec: schedReq.MinPassLength,
			})
		}

		satellites := make([]*pointing.SatMon, len(buffer))
		copy(satellites, buffer)

		satPasses, err := s.c.GetSchedule(satellites, schedReq.GroundStations, schedReq.StartDate, schedReq.StopDate, r.Context())
		if err != nil {
			apierror.Handle(w, r, err)
		}
		var resp pointing.NextPasses
		resp = satPasses

		if err := render.Render(w, r, &resp); err != nil {
			apierror.Handle(w, r, apierror.Wrap(err, apierror.ErrRender))
		}
	}
}
