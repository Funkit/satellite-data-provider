package main

import (
	"context"
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

	ans, err := client.GetNextPass(ctx, &pointing.NextPassRequest{
		Satellite: &pointing.SatMon{
			SatelliteInformation: &pointing.SatelliteInformation{
				Name:      "STARLINK-24",
				TleLine_1: "1 44238U 19029D   22229.17555387  .00106534  00000+0  22460-2 0  9994",
				TleLine_2: "2 44238  53.0031 183.2357 0002897 123.7131 236.4150 15.44417471179240",
			},
			MinimumPassLengthSec: 20,
		},
		GroundStations: []*pointing.GroundStationInformation{
			{
				Name:                       "Toulouse",
				Latitude:                   43.604652,
				Longitude:                  1.444209,
				Altitude:                   146,
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

	if len(ans.Pointing) != 0 {
		fmt.Printf("Pass found for satellite %v at %v for station %v:\n", ans.SatelliteName, ans.Pointing[0].Date, ans.StationName)
		fmt.Println(ans.Pointing)
	} else {
		fmt.Println("No pass found")
	}
}
