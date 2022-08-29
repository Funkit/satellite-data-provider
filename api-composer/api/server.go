package api

import (
	"fmt"
	"github.com/Funkit/satellite-data-provider/api-composer/sattrack"
	"github.com/go-chi/chi/v5"
	"log"
	"net/http"
)

type Server struct {
	c      *sattrack.Client
	router chi.Router
	port   int
}

func NewServer(port int, tls bool, serverAddr, caFile, serverHostOverride string) (*Server, error) {
	cl, err := sattrack.NewClient(tls, serverAddr, caFile, serverHostOverride)
	if err != nil {
		return nil, err
	}

	return &Server{
		c:      cl,
		router: chi.NewRouter(),
		port:   port,
	}, nil
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
	s.router.Get("/schedule/{constellation}", s.getConstellationSchedule())
}

func (s *Server) getConstellationSchedule() http.HandlerFunc {
	return func(w http.ResponseWriter, r *http.Request) {
		constellation := chi.URLParam(r, "constellation")
		switch constellation {
		case "oneweb":

		}
	}
}
