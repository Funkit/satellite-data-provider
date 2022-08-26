package main

import (
	"context"
	"encoding/json"
	"flag"
	"fmt"
	"github.com/Funkit/satellite-data-provider/pointing"
	"google.golang.org/genproto/googleapis/type/datetime"
	"google.golang.org/grpc"
	"google.golang.org/grpc/credentials"
	"google.golang.org/grpc/credentials/insecure"
	"log"
	"time"
)

var (
	tls                = flag.Bool("tls", false, "Connection uses TLS if true, else plain TCP")
	caFile             = flag.String("ca_file", "", "The file containing the CA root cert file")
	serverAddr         = flag.String("addr", "localhost:50051", "The server address in the format of host:port")
	serverHostOverride = flag.String("server_host_override", "x.test.example.com", "The server name used to verify the hostname returned by the TLS handshake")
)

func main() {
	flag.Parse()
	var opts []grpc.DialOption
	if *tls {
		if *caFile == "" {
			*caFile = "x509/ca_cert.pem"
		}
		creds, err := credentials.NewClientTLSFromFile(*caFile, *serverHostOverride)
		if err != nil {
			log.Fatalf("Failed to create TLS credentials %v", err)
		}
		opts = append(opts, grpc.WithTransportCredentials(creds))
	} else {
		opts = append(opts, grpc.WithTransportCredentials(insecure.NewCredentials()))
	}

	conn, err := grpc.Dial(*serverAddr, opts...)
	if err != nil {
		log.Fatalf("fail to dial: %v", err)
	}
	defer conn.Close()

	client := pointing.NewProcessingClient(conn)

	ctx, cancel := context.WithTimeout(context.Background(), 10*time.Second)
	defer cancel()

	ans, err := client.GetSchedule(ctx, &pointing.ScheduleRequest{
		Satellites: []*pointing.SatMon{
			{
				SatelliteInformation: &pointing.SatelliteInformation{
					Name:      "STARLINK-24",
					TleLine_1: "1 44238U 19029D   22229.17555387  .00106534  00000+0  22460-2 0  9994",
					TleLine_2: "2 44238  53.0031 183.2357 0002897 123.7131 236.4150 15.44417471179240",
				},
				MinimumPassLengthSec: 10,
			},
			{
				SatelliteInformation: &pointing.SatelliteInformation{
					Name:      "STARLINK-71",
					TleLine_1: "1 44252U 19029T   22229.15356155  .00092076  00000+0  18178-2 0  9996",
					TleLine_2: "2 44252  52.9924 177.9864 0003905 111.8634 248.2787 15.46410461179314",
				},
				MinimumPassLengthSec: 10,
			},
			{
				SatelliteInformation: &pointing.SatelliteInformation{
					Name:      "STARLINK-1007",
					TleLine_1: "1 44713U 19074A   22228.79595905  .00001502  00000+0  11967-3 0  9999",
					TleLine_2: "2 44713  53.0557 266.5525 0001331  77.7034 282.4104 15.06400880152677",
				},
				MinimumPassLengthSec: 10,
			},
		},
		Stations: []*pointing.GroundStationInformation{
			{
				Name:                       "Toulouse",
				Latitude:                   43.604652,
				Longitude:                  1.444209,
				Altitude:                   146,
				MinimumElevation:           0.5,
				StationPositioningDelaySec: 60,
			},
			{
				Name:                       "Tokyo",
				Latitude:                   35.652832,
				Longitude:                  139.839478,
				Altitude:                   37.153,
				MinimumElevation:           0.5,
				StationPositioningDelaySec: 60,
			},
		},
		StartDate: &datetime.DateTime{
			Year:       2022,
			Month:      8,
			Day:        25,
			Hours:      0,
			Minutes:    0,
			Seconds:    0,
			Nanos:      0,
			TimeOffset: nil,
		},
		StopDate: &datetime.DateTime{
			Year:       2022,
			Month:      8,
			Day:        25,
			Hours:      23,
			Minutes:    59,
			Seconds:    59,
			Nanos:      0,
			TimeOffset: nil,
		},
	})
	if err != nil {
		panic(err)
	}

	if len(ans.Passes) != 0 {
		rawJSON, err := json.MarshalIndent(ans.Passes, "", " ")
		if err != nil {
			panic(err)
		}
		fmt.Println(string(rawJSON))
	} else {
		fmt.Println("No pass found")
	}

	//ans, err := client.GetNextPass(ctx, &pointing.NextPassRequest{
	//	Satellite: &pointing.SatMon{
	//		SatelliteInformation: &pointing.SatelliteInformation{
	//			Name:      "STARLINK-24",
	//			TleLine_1: "1 44238U 19029D   22229.17555387  .00106534  00000+0  22460-2 0  9994",
	//			TleLine_2: "2 44238  53.0031 183.2357 0002897 123.7131 236.4150 15.44417471179240",
	//		},
	//		MinimumPassLengthSec: 20,
	//	},
	//	GroundStations: []*pointing.GroundStationInformation{
	//		{
	//			Name:                       "Toulouse",
	//			Latitude:                   43.604652,
	//			Longitude:                  1.444209,
	//			Altitude:                   146,
	//			MinimumElevation:           0.5,
	//			StationPositioningDelaySec: 60,
	//		},
	//	},
	//	StartDate: &datetime.DateTime{
	//		Year:       2022,
	//		Month:      8,
	//		Day:        25,
	//		Hours:      0,
	//		Minutes:    0,
	//		Seconds:    0,
	//		Nanos:      0,
	//		TimeOffset: nil,
	//	},
	//	StopDate: &datetime.DateTime{
	//		Year:       2022,
	//		Month:      8,
	//		Day:        25,
	//		Hours:      23,
	//		Minutes:    59,
	//		Seconds:    59,
	//		Nanos:      0,
	//		TimeOffset: nil,
	//	},
	//})
	//if err != nil {
	//	panic(err)
	//}
	//
	//if len(ans.Pointing) != 0 {
	//	fmt.Printf("Pass found for satellite %v at %v for station %v:\n", ans.SatelliteName, ans.Pointing[0].Date, ans.StationName)
	//	fmt.Println(ans.Pointing)
	//} else {
	//	fmt.Println("No pass found")
	//}
}
