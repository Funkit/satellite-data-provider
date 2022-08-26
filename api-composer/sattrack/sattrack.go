package sattrack

import (
	"context"
	"fmt"
	"github.com/Funkit/satellite-data-provider/pointing"
	"google.golang.org/genproto/googleapis/type/datetime"
	"google.golang.org/grpc"
	"google.golang.org/grpc/credentials"
	"google.golang.org/grpc/credentials/insecure"
	"google.golang.org/protobuf/types/known/durationpb"
	"time"
)

func TimeToGRPCDatetime(dt time.Time) *datetime.DateTime {
	_, offsetSec := dt.Zone()
	return &datetime.DateTime{
		Year:    int32(dt.Year()),
		Month:   int32(dt.Month()),
		Day:     int32(dt.Day()),
		Hours:   int32(dt.Hour()),
		Minutes: int32(dt.Minute()),
		Seconds: int32(dt.Second()),
		Nanos:   int32(dt.Nanosecond()),
		TimeOffset: &datetime.DateTime_UtcOffset{
			UtcOffset: &durationpb.Duration{
				Seconds: int64(offsetSec),
			},
		},
	}
}

type Client struct {
	serverAddress string
	grpcClient    pointing.ProcessingClient
	clientConn    *grpc.ClientConn
	dialOptions   []grpc.DialOption
}

func NewClient(tls bool, serverAddr, caFile, serverHostOverride string) (*Client, error) {
	var opts []grpc.DialOption
	if tls {
		if caFile == "" {
			caFile = "x509/ca_cert.pem"
		}
		creds, err := credentials.NewClientTLSFromFile(caFile, serverHostOverride)
		if err != nil {
			return nil, fmt.Errorf("failed to create TLS credentials %v", err)
		}
		opts = append(opts, grpc.WithTransportCredentials(creds))
	} else {
		opts = append(opts, grpc.WithTransportCredentials(insecure.NewCredentials()))
	}

	return &Client{
		serverAddress: serverAddr,
		dialOptions:   opts,
	}, nil
}

func (c *Client) Connect() error {
	conn, err := grpc.Dial(c.serverAddress, c.dialOptions...)
	if err != nil {
		return fmt.Errorf("fail to dial: %v", err)
	}
	c.clientConn = conn

	client := pointing.NewProcessingClient(conn)

	c.grpcClient = client

	return nil
}

func (c *Client) Close() {
	c.clientConn.Close()
}

func (c *Client) GetSchedule(satellites []*pointing.SatMon, stations []*pointing.GroundStationInformation, startDate, stopDate time.Time, ctx context.Context) ([]*pointing.NextPassReply, error) {
	ans, err := c.grpcClient.GetSchedule(ctx, &pointing.ScheduleRequest{
		Satellites: satellites,
		Stations:   stations,
		StartDate:  TimeToGRPCDatetime(startDate),
		StopDate:   TimeToGRPCDatetime(stopDate),
	})

	if err != nil {
		return nil, err
	}

	return ans.SatellitePasses, nil
}
