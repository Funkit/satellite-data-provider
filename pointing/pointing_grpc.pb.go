// Code generated by protoc-gen-go-grpc. DO NOT EDIT.
// versions:
// - protoc-gen-go-grpc v1.2.0
// - protoc             v3.21.6
// source: pointing.proto

package pointing

import (
	context "context"
	grpc "google.golang.org/grpc"
	codes "google.golang.org/grpc/codes"
	status "google.golang.org/grpc/status"
)

// This is a compile-time assertion to ensure that this generated file
// is compatible with the grpc package it is being compiled against.
// Requires gRPC-Go v1.32.0 or later.
const _ = grpc.SupportPackageIsVersion7

// ProcessingClient is the client API for Processing service.
//
// For semantics around ctx use and closing/ending streaming RPCs, please refer to https://pkg.go.dev/google.golang.org/grpc/?tab=doc#ClientConn.NewStream.
type ProcessingClient interface {
	// For a given satellite, provided a list of ground stations, returns the first satellite pass that can be monitored
	// between start_date and stop_date.
	// A pass consists in a list of antenna pointing information (azimuth, elevation...) necessary for tracking the satellite.
	// A pass is considered valid for a given station when the elevation is above minimum_elevation and the total pass duration is above
	// minimum_pass_length_sec.
	GetNextPass(ctx context.Context, in *NextPassRequest, opts ...grpc.CallOption) (*NextPassReply, error)
	// Provided a list of satellites and ground stations, returns a list of passes that monitors as many satellites as possible between
	// start_date and stop_date.
	GetSchedule(ctx context.Context, in *ScheduleRequest, opts ...grpc.CallOption) (*ScheduleReply, error)
}

type processingClient struct {
	cc grpc.ClientConnInterface
}

func NewProcessingClient(cc grpc.ClientConnInterface) ProcessingClient {
	return &processingClient{cc}
}

func (c *processingClient) GetNextPass(ctx context.Context, in *NextPassRequest, opts ...grpc.CallOption) (*NextPassReply, error) {
	out := new(NextPassReply)
	err := c.cc.Invoke(ctx, "/pointing.Processing/GetNextPass", in, out, opts...)
	if err != nil {
		return nil, err
	}
	return out, nil
}

func (c *processingClient) GetSchedule(ctx context.Context, in *ScheduleRequest, opts ...grpc.CallOption) (*ScheduleReply, error) {
	out := new(ScheduleReply)
	err := c.cc.Invoke(ctx, "/pointing.Processing/GetSchedule", in, out, opts...)
	if err != nil {
		return nil, err
	}
	return out, nil
}

// ProcessingServer is the server API for Processing service.
// All implementations must embed UnimplementedProcessingServer
// for forward compatibility
type ProcessingServer interface {
	// For a given satellite, provided a list of ground stations, returns the first satellite pass that can be monitored
	// between start_date and stop_date.
	// A pass consists in a list of antenna pointing information (azimuth, elevation...) necessary for tracking the satellite.
	// A pass is considered valid for a given station when the elevation is above minimum_elevation and the total pass duration is above
	// minimum_pass_length_sec.
	GetNextPass(context.Context, *NextPassRequest) (*NextPassReply, error)
	// Provided a list of satellites and ground stations, returns a list of passes that monitors as many satellites as possible between
	// start_date and stop_date.
	GetSchedule(context.Context, *ScheduleRequest) (*ScheduleReply, error)
	mustEmbedUnimplementedProcessingServer()
}

// UnimplementedProcessingServer must be embedded to have forward compatible implementations.
type UnimplementedProcessingServer struct {
}

func (UnimplementedProcessingServer) GetNextPass(context.Context, *NextPassRequest) (*NextPassReply, error) {
	return nil, status.Errorf(codes.Unimplemented, "method GetNextPass not implemented")
}
func (UnimplementedProcessingServer) GetSchedule(context.Context, *ScheduleRequest) (*ScheduleReply, error) {
	return nil, status.Errorf(codes.Unimplemented, "method GetSchedule not implemented")
}
func (UnimplementedProcessingServer) mustEmbedUnimplementedProcessingServer() {}

// UnsafeProcessingServer may be embedded to opt out of forward compatibility for this service.
// Use of this interface is not recommended, as added methods to ProcessingServer will
// result in compilation errors.
type UnsafeProcessingServer interface {
	mustEmbedUnimplementedProcessingServer()
}

func RegisterProcessingServer(s grpc.ServiceRegistrar, srv ProcessingServer) {
	s.RegisterService(&Processing_ServiceDesc, srv)
}

func _Processing_GetNextPass_Handler(srv interface{}, ctx context.Context, dec func(interface{}) error, interceptor grpc.UnaryServerInterceptor) (interface{}, error) {
	in := new(NextPassRequest)
	if err := dec(in); err != nil {
		return nil, err
	}
	if interceptor == nil {
		return srv.(ProcessingServer).GetNextPass(ctx, in)
	}
	info := &grpc.UnaryServerInfo{
		Server:     srv,
		FullMethod: "/pointing.Processing/GetNextPass",
	}
	handler := func(ctx context.Context, req interface{}) (interface{}, error) {
		return srv.(ProcessingServer).GetNextPass(ctx, req.(*NextPassRequest))
	}
	return interceptor(ctx, in, info, handler)
}

func _Processing_GetSchedule_Handler(srv interface{}, ctx context.Context, dec func(interface{}) error, interceptor grpc.UnaryServerInterceptor) (interface{}, error) {
	in := new(ScheduleRequest)
	if err := dec(in); err != nil {
		return nil, err
	}
	if interceptor == nil {
		return srv.(ProcessingServer).GetSchedule(ctx, in)
	}
	info := &grpc.UnaryServerInfo{
		Server:     srv,
		FullMethod: "/pointing.Processing/GetSchedule",
	}
	handler := func(ctx context.Context, req interface{}) (interface{}, error) {
		return srv.(ProcessingServer).GetSchedule(ctx, req.(*ScheduleRequest))
	}
	return interceptor(ctx, in, info, handler)
}

// Processing_ServiceDesc is the grpc.ServiceDesc for Processing service.
// It's only intended for direct use with grpc.RegisterService,
// and not to be introspected or modified (even as a copy)
var Processing_ServiceDesc = grpc.ServiceDesc{
	ServiceName: "pointing.Processing",
	HandlerType: (*ProcessingServer)(nil),
	Methods: []grpc.MethodDesc{
		{
			MethodName: "GetNextPass",
			Handler:    _Processing_GetNextPass_Handler,
		},
		{
			MethodName: "GetSchedule",
			Handler:    _Processing_GetSchedule_Handler,
		},
	},
	Streams:  []grpc.StreamDesc{},
	Metadata: "pointing.proto",
}
