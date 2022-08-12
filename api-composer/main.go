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
	"io"
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

	ans, err := client.GetAntennaPointing(ctx, &pointing.AntennaPointingRequest{
		SatelliteInformation: &pointing.SatelliteInformation{
			SatelliteName: "CALSPHERE 1",
			TleLine_1:     "1 00900U 64063C   22187.89574347  .00000359  00000+0  37304-3 0  9991",
			TleLine_2:     "2 00900  90.1740  41.2695 0026288 328.3188  44.6768 13.73833077873339",
		},
		GroundStationInformation: &pointing.GroundStationInformation{
			StationLatitude:  43.604652,
			StationLongitude: 1.444209,
			StationAltitude:  146,
		},
		StartDate: &datetime.DateTime{
			Year:       2022,
			Month:      7,
			Day:        28,
			Hours:      16,
			Minutes:    0,
			Seconds:    0,
			Nanos:      0,
			TimeOffset: nil,
		},
		StopDate: &datetime.DateTime{
			Year:       2022,
			Month:      7,
			Day:        28,
			Hours:      17,
			Minutes:    0,
			Seconds:    0,
			Nanos:      0,
			TimeOffset: nil,
		},
	})
	if err != nil {
		panic(err)
	}

	for {
		val, err := ans.Recv()
		if err == io.EOF {
			return
		}
		if err != nil {
			panic(err)
		}
		fmt.Printf("%v - %v: %v %v %v\n", val.SatelliteName, val.Date, val.Azimuth, val.Elevation, val.RangeMeters)
	}
}
