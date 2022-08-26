// Copyright 2015 gRPC authors.
//
// Licensed under the Apache License, Version 2.0 (the "License");
// you may not use this file except in compliance with the License.
// You may obtain a copy of the License at
//
//     http://www.apache.org/licenses/LICENSE-2.0
//
// Unless required by applicable law or agreed to in writing, software
// distributed under the License is distributed on an "AS IS" BASIS,
// WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
// See the License for the specific language governing permissions and
// limitations under the License.

// Code generated by protoc-gen-go. DO NOT EDIT.
// versions:
// 	protoc-gen-go v1.28.0
// 	protoc        v3.21.2
// source: pointing.proto

package pointing

import (
	datetime "google.golang.org/genproto/googleapis/type/datetime"
	protoreflect "google.golang.org/protobuf/reflect/protoreflect"
	protoimpl "google.golang.org/protobuf/runtime/protoimpl"
	reflect "reflect"
	sync "sync"
)

const (
	// Verify that this generated code is sufficiently up-to-date.
	_ = protoimpl.EnforceVersion(20 - protoimpl.MinVersion)
	// Verify that runtime/protoimpl is sufficiently up-to-date.
	_ = protoimpl.EnforceVersion(protoimpl.MaxVersion - 20)
)

type SatelliteInformation struct {
	state         protoimpl.MessageState
	sizeCache     protoimpl.SizeCache
	unknownFields protoimpl.UnknownFields

	Name      string `protobuf:"bytes,1,opt,name=name,proto3" json:"name,omitempty"`
	TleLine_1 string `protobuf:"bytes,2,opt,name=tle_line_1,json=tleLine1,proto3" json:"tle_line_1,omitempty"`
	TleLine_2 string `protobuf:"bytes,3,opt,name=tle_line_2,json=tleLine2,proto3" json:"tle_line_2,omitempty"`
}

func (x *SatelliteInformation) Reset() {
	*x = SatelliteInformation{}
	if protoimpl.UnsafeEnabled {
		mi := &file_pointing_proto_msgTypes[0]
		ms := protoimpl.X.MessageStateOf(protoimpl.Pointer(x))
		ms.StoreMessageInfo(mi)
	}
}

func (x *SatelliteInformation) String() string {
	return protoimpl.X.MessageStringOf(x)
}

func (*SatelliteInformation) ProtoMessage() {}

func (x *SatelliteInformation) ProtoReflect() protoreflect.Message {
	mi := &file_pointing_proto_msgTypes[0]
	if protoimpl.UnsafeEnabled && x != nil {
		ms := protoimpl.X.MessageStateOf(protoimpl.Pointer(x))
		if ms.LoadMessageInfo() == nil {
			ms.StoreMessageInfo(mi)
		}
		return ms
	}
	return mi.MessageOf(x)
}

// Deprecated: Use SatelliteInformation.ProtoReflect.Descriptor instead.
func (*SatelliteInformation) Descriptor() ([]byte, []int) {
	return file_pointing_proto_rawDescGZIP(), []int{0}
}

func (x *SatelliteInformation) GetName() string {
	if x != nil {
		return x.Name
	}
	return ""
}

func (x *SatelliteInformation) GetTleLine_1() string {
	if x != nil {
		return x.TleLine_1
	}
	return ""
}

func (x *SatelliteInformation) GetTleLine_2() string {
	if x != nil {
		return x.TleLine_2
	}
	return ""
}

type GroundStationInformation struct {
	state         protoimpl.MessageState
	sizeCache     protoimpl.SizeCache
	unknownFields protoimpl.UnknownFields

	Name                       string  `protobuf:"bytes,1,opt,name=name,proto3" json:"name,omitempty"`
	Latitude                   float64 `protobuf:"fixed64,2,opt,name=latitude,proto3" json:"latitude,omitempty"`
	Longitude                  float64 `protobuf:"fixed64,3,opt,name=longitude,proto3" json:"longitude,omitempty"`
	Altitude                   float64 `protobuf:"fixed64,4,opt,name=altitude,proto3" json:"altitude,omitempty"`
	MinimumElevation           float64 `protobuf:"fixed64,5,opt,name=minimum_elevation,json=minimumElevation,proto3" json:"minimum_elevation,omitempty"`
	StationPositioningDelaySec int32   `protobuf:"varint,6,opt,name=station_positioning_delay_sec,json=stationPositioningDelaySec,proto3" json:"station_positioning_delay_sec,omitempty"` // Time necessary for a ground station to reposition between passes.
}

func (x *GroundStationInformation) Reset() {
	*x = GroundStationInformation{}
	if protoimpl.UnsafeEnabled {
		mi := &file_pointing_proto_msgTypes[1]
		ms := protoimpl.X.MessageStateOf(protoimpl.Pointer(x))
		ms.StoreMessageInfo(mi)
	}
}

func (x *GroundStationInformation) String() string {
	return protoimpl.X.MessageStringOf(x)
}

func (*GroundStationInformation) ProtoMessage() {}

func (x *GroundStationInformation) ProtoReflect() protoreflect.Message {
	mi := &file_pointing_proto_msgTypes[1]
	if protoimpl.UnsafeEnabled && x != nil {
		ms := protoimpl.X.MessageStateOf(protoimpl.Pointer(x))
		if ms.LoadMessageInfo() == nil {
			ms.StoreMessageInfo(mi)
		}
		return ms
	}
	return mi.MessageOf(x)
}

// Deprecated: Use GroundStationInformation.ProtoReflect.Descriptor instead.
func (*GroundStationInformation) Descriptor() ([]byte, []int) {
	return file_pointing_proto_rawDescGZIP(), []int{1}
}

func (x *GroundStationInformation) GetName() string {
	if x != nil {
		return x.Name
	}
	return ""
}

func (x *GroundStationInformation) GetLatitude() float64 {
	if x != nil {
		return x.Latitude
	}
	return 0
}

func (x *GroundStationInformation) GetLongitude() float64 {
	if x != nil {
		return x.Longitude
	}
	return 0
}

func (x *GroundStationInformation) GetAltitude() float64 {
	if x != nil {
		return x.Altitude
	}
	return 0
}

func (x *GroundStationInformation) GetMinimumElevation() float64 {
	if x != nil {
		return x.MinimumElevation
	}
	return 0
}

func (x *GroundStationInformation) GetStationPositioningDelaySec() int32 {
	if x != nil {
		return x.StationPositioningDelaySec
	}
	return 0
}

type NextPassRequest struct {
	state         protoimpl.MessageState
	sizeCache     protoimpl.SizeCache
	unknownFields protoimpl.UnknownFields

	Satellite      *SatMon                     `protobuf:"bytes,1,opt,name=satellite,proto3" json:"satellite,omitempty"`
	GroundStations []*GroundStationInformation `protobuf:"bytes,2,rep,name=ground_stations,json=groundStations,proto3" json:"ground_stations,omitempty"`
	StartDate      *datetime.DateTime          `protobuf:"bytes,3,opt,name=start_date,json=startDate,proto3" json:"start_date,omitempty"`
	StopDate       *datetime.DateTime          `protobuf:"bytes,4,opt,name=stop_date,json=stopDate,proto3" json:"stop_date,omitempty"`
}

func (x *NextPassRequest) Reset() {
	*x = NextPassRequest{}
	if protoimpl.UnsafeEnabled {
		mi := &file_pointing_proto_msgTypes[2]
		ms := protoimpl.X.MessageStateOf(protoimpl.Pointer(x))
		ms.StoreMessageInfo(mi)
	}
}

func (x *NextPassRequest) String() string {
	return protoimpl.X.MessageStringOf(x)
}

func (*NextPassRequest) ProtoMessage() {}

func (x *NextPassRequest) ProtoReflect() protoreflect.Message {
	mi := &file_pointing_proto_msgTypes[2]
	if protoimpl.UnsafeEnabled && x != nil {
		ms := protoimpl.X.MessageStateOf(protoimpl.Pointer(x))
		if ms.LoadMessageInfo() == nil {
			ms.StoreMessageInfo(mi)
		}
		return ms
	}
	return mi.MessageOf(x)
}

// Deprecated: Use NextPassRequest.ProtoReflect.Descriptor instead.
func (*NextPassRequest) Descriptor() ([]byte, []int) {
	return file_pointing_proto_rawDescGZIP(), []int{2}
}

func (x *NextPassRequest) GetSatellite() *SatMon {
	if x != nil {
		return x.Satellite
	}
	return nil
}

func (x *NextPassRequest) GetGroundStations() []*GroundStationInformation {
	if x != nil {
		return x.GroundStations
	}
	return nil
}

func (x *NextPassRequest) GetStartDate() *datetime.DateTime {
	if x != nil {
		return x.StartDate
	}
	return nil
}

func (x *NextPassRequest) GetStopDate() *datetime.DateTime {
	if x != nil {
		return x.StopDate
	}
	return nil
}

type NextPassReply struct {
	state         protoimpl.MessageState
	sizeCache     protoimpl.SizeCache
	unknownFields protoimpl.UnknownFields

	SatelliteName string                 `protobuf:"bytes,1,opt,name=satellite_name,json=satelliteName,proto3" json:"satellite_name,omitempty"`
	StationName   string                 `protobuf:"bytes,2,opt,name=station_name,json=stationName,proto3" json:"station_name,omitempty"`
	Pointing      []*PointingInformation `protobuf:"bytes,3,rep,name=pointing,proto3" json:"pointing,omitempty"`
}

func (x *NextPassReply) Reset() {
	*x = NextPassReply{}
	if protoimpl.UnsafeEnabled {
		mi := &file_pointing_proto_msgTypes[3]
		ms := protoimpl.X.MessageStateOf(protoimpl.Pointer(x))
		ms.StoreMessageInfo(mi)
	}
}

func (x *NextPassReply) String() string {
	return protoimpl.X.MessageStringOf(x)
}

func (*NextPassReply) ProtoMessage() {}

func (x *NextPassReply) ProtoReflect() protoreflect.Message {
	mi := &file_pointing_proto_msgTypes[3]
	if protoimpl.UnsafeEnabled && x != nil {
		ms := protoimpl.X.MessageStateOf(protoimpl.Pointer(x))
		if ms.LoadMessageInfo() == nil {
			ms.StoreMessageInfo(mi)
		}
		return ms
	}
	return mi.MessageOf(x)
}

// Deprecated: Use NextPassReply.ProtoReflect.Descriptor instead.
func (*NextPassReply) Descriptor() ([]byte, []int) {
	return file_pointing_proto_rawDescGZIP(), []int{3}
}

func (x *NextPassReply) GetSatelliteName() string {
	if x != nil {
		return x.SatelliteName
	}
	return ""
}

func (x *NextPassReply) GetStationName() string {
	if x != nil {
		return x.StationName
	}
	return ""
}

func (x *NextPassReply) GetPointing() []*PointingInformation {
	if x != nil {
		return x.Pointing
	}
	return nil
}

type PointingInformation struct {
	state         protoimpl.MessageState
	sizeCache     protoimpl.SizeCache
	unknownFields protoimpl.UnknownFields

	Date        *datetime.DateTime `protobuf:"bytes,1,opt,name=date,proto3" json:"date,omitempty"`
	Azimuth     float64            `protobuf:"fixed64,2,opt,name=azimuth,proto3" json:"azimuth,omitempty"`
	Elevation   float64            `protobuf:"fixed64,3,opt,name=elevation,proto3" json:"elevation,omitempty"`
	RangeMeters float64            `protobuf:"fixed64,5,opt,name=range_meters,json=rangeMeters,proto3" json:"range_meters,omitempty"`
}

func (x *PointingInformation) Reset() {
	*x = PointingInformation{}
	if protoimpl.UnsafeEnabled {
		mi := &file_pointing_proto_msgTypes[4]
		ms := protoimpl.X.MessageStateOf(protoimpl.Pointer(x))
		ms.StoreMessageInfo(mi)
	}
}

func (x *PointingInformation) String() string {
	return protoimpl.X.MessageStringOf(x)
}

func (*PointingInformation) ProtoMessage() {}

func (x *PointingInformation) ProtoReflect() protoreflect.Message {
	mi := &file_pointing_proto_msgTypes[4]
	if protoimpl.UnsafeEnabled && x != nil {
		ms := protoimpl.X.MessageStateOf(protoimpl.Pointer(x))
		if ms.LoadMessageInfo() == nil {
			ms.StoreMessageInfo(mi)
		}
		return ms
	}
	return mi.MessageOf(x)
}

// Deprecated: Use PointingInformation.ProtoReflect.Descriptor instead.
func (*PointingInformation) Descriptor() ([]byte, []int) {
	return file_pointing_proto_rawDescGZIP(), []int{4}
}

func (x *PointingInformation) GetDate() *datetime.DateTime {
	if x != nil {
		return x.Date
	}
	return nil
}

func (x *PointingInformation) GetAzimuth() float64 {
	if x != nil {
		return x.Azimuth
	}
	return 0
}

func (x *PointingInformation) GetElevation() float64 {
	if x != nil {
		return x.Elevation
	}
	return 0
}

func (x *PointingInformation) GetRangeMeters() float64 {
	if x != nil {
		return x.RangeMeters
	}
	return 0
}

type ScheduleRequest struct {
	state         protoimpl.MessageState
	sizeCache     protoimpl.SizeCache
	unknownFields protoimpl.UnknownFields

	Satellites []*SatMon                   `protobuf:"bytes,1,rep,name=satellites,proto3" json:"satellites,omitempty"`
	Stations   []*GroundStationInformation `protobuf:"bytes,3,rep,name=stations,proto3" json:"stations,omitempty"`
	StartDate  *datetime.DateTime          `protobuf:"bytes,4,opt,name=start_date,json=startDate,proto3" json:"start_date,omitempty"`
	StopDate   *datetime.DateTime          `protobuf:"bytes,5,opt,name=stop_date,json=stopDate,proto3" json:"stop_date,omitempty"`
}

func (x *ScheduleRequest) Reset() {
	*x = ScheduleRequest{}
	if protoimpl.UnsafeEnabled {
		mi := &file_pointing_proto_msgTypes[5]
		ms := protoimpl.X.MessageStateOf(protoimpl.Pointer(x))
		ms.StoreMessageInfo(mi)
	}
}

func (x *ScheduleRequest) String() string {
	return protoimpl.X.MessageStringOf(x)
}

func (*ScheduleRequest) ProtoMessage() {}

func (x *ScheduleRequest) ProtoReflect() protoreflect.Message {
	mi := &file_pointing_proto_msgTypes[5]
	if protoimpl.UnsafeEnabled && x != nil {
		ms := protoimpl.X.MessageStateOf(protoimpl.Pointer(x))
		if ms.LoadMessageInfo() == nil {
			ms.StoreMessageInfo(mi)
		}
		return ms
	}
	return mi.MessageOf(x)
}

// Deprecated: Use ScheduleRequest.ProtoReflect.Descriptor instead.
func (*ScheduleRequest) Descriptor() ([]byte, []int) {
	return file_pointing_proto_rawDescGZIP(), []int{5}
}

func (x *ScheduleRequest) GetSatellites() []*SatMon {
	if x != nil {
		return x.Satellites
	}
	return nil
}

func (x *ScheduleRequest) GetStations() []*GroundStationInformation {
	if x != nil {
		return x.Stations
	}
	return nil
}

func (x *ScheduleRequest) GetStartDate() *datetime.DateTime {
	if x != nil {
		return x.StartDate
	}
	return nil
}

func (x *ScheduleRequest) GetStopDate() *datetime.DateTime {
	if x != nil {
		return x.StopDate
	}
	return nil
}

type SatMon struct {
	state         protoimpl.MessageState
	sizeCache     protoimpl.SizeCache
	unknownFields protoimpl.UnknownFields

	SatelliteInformation *SatelliteInformation `protobuf:"bytes,1,opt,name=satellite_information,json=satelliteInformation,proto3" json:"satellite_information,omitempty"`
	MinimumPassLengthSec int32                 `protobuf:"varint,2,opt,name=minimum_pass_length_sec,json=minimumPassLengthSec,proto3" json:"minimum_pass_length_sec,omitempty"`
}

func (x *SatMon) Reset() {
	*x = SatMon{}
	if protoimpl.UnsafeEnabled {
		mi := &file_pointing_proto_msgTypes[6]
		ms := protoimpl.X.MessageStateOf(protoimpl.Pointer(x))
		ms.StoreMessageInfo(mi)
	}
}

func (x *SatMon) String() string {
	return protoimpl.X.MessageStringOf(x)
}

func (*SatMon) ProtoMessage() {}

func (x *SatMon) ProtoReflect() protoreflect.Message {
	mi := &file_pointing_proto_msgTypes[6]
	if protoimpl.UnsafeEnabled && x != nil {
		ms := protoimpl.X.MessageStateOf(protoimpl.Pointer(x))
		if ms.LoadMessageInfo() == nil {
			ms.StoreMessageInfo(mi)
		}
		return ms
	}
	return mi.MessageOf(x)
}

// Deprecated: Use SatMon.ProtoReflect.Descriptor instead.
func (*SatMon) Descriptor() ([]byte, []int) {
	return file_pointing_proto_rawDescGZIP(), []int{6}
}

func (x *SatMon) GetSatelliteInformation() *SatelliteInformation {
	if x != nil {
		return x.SatelliteInformation
	}
	return nil
}

func (x *SatMon) GetMinimumPassLengthSec() int32 {
	if x != nil {
		return x.MinimumPassLengthSec
	}
	return 0
}

type ScheduleReply struct {
	state         protoimpl.MessageState
	sizeCache     protoimpl.SizeCache
	unknownFields protoimpl.UnknownFields

	SatellitePasses []*NextPassReply `protobuf:"bytes,1,rep,name=satellite_passes,json=satellitePasses,proto3" json:"satellite_passes,omitempty"`
}

func (x *ScheduleReply) Reset() {
	*x = ScheduleReply{}
	if protoimpl.UnsafeEnabled {
		mi := &file_pointing_proto_msgTypes[7]
		ms := protoimpl.X.MessageStateOf(protoimpl.Pointer(x))
		ms.StoreMessageInfo(mi)
	}
}

func (x *ScheduleReply) String() string {
	return protoimpl.X.MessageStringOf(x)
}

func (*ScheduleReply) ProtoMessage() {}

func (x *ScheduleReply) ProtoReflect() protoreflect.Message {
	mi := &file_pointing_proto_msgTypes[7]
	if protoimpl.UnsafeEnabled && x != nil {
		ms := protoimpl.X.MessageStateOf(protoimpl.Pointer(x))
		if ms.LoadMessageInfo() == nil {
			ms.StoreMessageInfo(mi)
		}
		return ms
	}
	return mi.MessageOf(x)
}

// Deprecated: Use ScheduleReply.ProtoReflect.Descriptor instead.
func (*ScheduleReply) Descriptor() ([]byte, []int) {
	return file_pointing_proto_rawDescGZIP(), []int{7}
}

func (x *ScheduleReply) GetSatellitePasses() []*NextPassReply {
	if x != nil {
		return x.SatellitePasses
	}
	return nil
}

var File_pointing_proto protoreflect.FileDescriptor

var file_pointing_proto_rawDesc = []byte{
	0x0a, 0x0e, 0x70, 0x6f, 0x69, 0x6e, 0x74, 0x69, 0x6e, 0x67, 0x2e, 0x70, 0x72, 0x6f, 0x74, 0x6f,
	0x12, 0x08, 0x70, 0x6f, 0x69, 0x6e, 0x74, 0x69, 0x6e, 0x67, 0x1a, 0x0e, 0x64, 0x61, 0x74, 0x65,
	0x74, 0x69, 0x6d, 0x65, 0x2e, 0x70, 0x72, 0x6f, 0x74, 0x6f, 0x22, 0x66, 0x0a, 0x14, 0x53, 0x61,
	0x74, 0x65, 0x6c, 0x6c, 0x69, 0x74, 0x65, 0x49, 0x6e, 0x66, 0x6f, 0x72, 0x6d, 0x61, 0x74, 0x69,
	0x6f, 0x6e, 0x12, 0x12, 0x0a, 0x04, 0x6e, 0x61, 0x6d, 0x65, 0x18, 0x01, 0x20, 0x01, 0x28, 0x09,
	0x52, 0x04, 0x6e, 0x61, 0x6d, 0x65, 0x12, 0x1c, 0x0a, 0x0a, 0x74, 0x6c, 0x65, 0x5f, 0x6c, 0x69,
	0x6e, 0x65, 0x5f, 0x31, 0x18, 0x02, 0x20, 0x01, 0x28, 0x09, 0x52, 0x08, 0x74, 0x6c, 0x65, 0x4c,
	0x69, 0x6e, 0x65, 0x31, 0x12, 0x1c, 0x0a, 0x0a, 0x74, 0x6c, 0x65, 0x5f, 0x6c, 0x69, 0x6e, 0x65,
	0x5f, 0x32, 0x18, 0x03, 0x20, 0x01, 0x28, 0x09, 0x52, 0x08, 0x74, 0x6c, 0x65, 0x4c, 0x69, 0x6e,
	0x65, 0x32, 0x22, 0xf4, 0x01, 0x0a, 0x18, 0x47, 0x72, 0x6f, 0x75, 0x6e, 0x64, 0x53, 0x74, 0x61,
	0x74, 0x69, 0x6f, 0x6e, 0x49, 0x6e, 0x66, 0x6f, 0x72, 0x6d, 0x61, 0x74, 0x69, 0x6f, 0x6e, 0x12,
	0x12, 0x0a, 0x04, 0x6e, 0x61, 0x6d, 0x65, 0x18, 0x01, 0x20, 0x01, 0x28, 0x09, 0x52, 0x04, 0x6e,
	0x61, 0x6d, 0x65, 0x12, 0x1a, 0x0a, 0x08, 0x6c, 0x61, 0x74, 0x69, 0x74, 0x75, 0x64, 0x65, 0x18,
	0x02, 0x20, 0x01, 0x28, 0x01, 0x52, 0x08, 0x6c, 0x61, 0x74, 0x69, 0x74, 0x75, 0x64, 0x65, 0x12,
	0x1c, 0x0a, 0x09, 0x6c, 0x6f, 0x6e, 0x67, 0x69, 0x74, 0x75, 0x64, 0x65, 0x18, 0x03, 0x20, 0x01,
	0x28, 0x01, 0x52, 0x09, 0x6c, 0x6f, 0x6e, 0x67, 0x69, 0x74, 0x75, 0x64, 0x65, 0x12, 0x1a, 0x0a,
	0x08, 0x61, 0x6c, 0x74, 0x69, 0x74, 0x75, 0x64, 0x65, 0x18, 0x04, 0x20, 0x01, 0x28, 0x01, 0x52,
	0x08, 0x61, 0x6c, 0x74, 0x69, 0x74, 0x75, 0x64, 0x65, 0x12, 0x2b, 0x0a, 0x11, 0x6d, 0x69, 0x6e,
	0x69, 0x6d, 0x75, 0x6d, 0x5f, 0x65, 0x6c, 0x65, 0x76, 0x61, 0x74, 0x69, 0x6f, 0x6e, 0x18, 0x05,
	0x20, 0x01, 0x28, 0x01, 0x52, 0x10, 0x6d, 0x69, 0x6e, 0x69, 0x6d, 0x75, 0x6d, 0x45, 0x6c, 0x65,
	0x76, 0x61, 0x74, 0x69, 0x6f, 0x6e, 0x12, 0x41, 0x0a, 0x1d, 0x73, 0x74, 0x61, 0x74, 0x69, 0x6f,
	0x6e, 0x5f, 0x70, 0x6f, 0x73, 0x69, 0x74, 0x69, 0x6f, 0x6e, 0x69, 0x6e, 0x67, 0x5f, 0x64, 0x65,
	0x6c, 0x61, 0x79, 0x5f, 0x73, 0x65, 0x63, 0x18, 0x06, 0x20, 0x01, 0x28, 0x05, 0x52, 0x1a, 0x73,
	0x74, 0x61, 0x74, 0x69, 0x6f, 0x6e, 0x50, 0x6f, 0x73, 0x69, 0x74, 0x69, 0x6f, 0x6e, 0x69, 0x6e,
	0x67, 0x44, 0x65, 0x6c, 0x61, 0x79, 0x53, 0x65, 0x63, 0x22, 0xf8, 0x01, 0x0a, 0x0f, 0x4e, 0x65,
	0x78, 0x74, 0x50, 0x61, 0x73, 0x73, 0x52, 0x65, 0x71, 0x75, 0x65, 0x73, 0x74, 0x12, 0x2e, 0x0a,
	0x09, 0x73, 0x61, 0x74, 0x65, 0x6c, 0x6c, 0x69, 0x74, 0x65, 0x18, 0x01, 0x20, 0x01, 0x28, 0x0b,
	0x32, 0x10, 0x2e, 0x70, 0x6f, 0x69, 0x6e, 0x74, 0x69, 0x6e, 0x67, 0x2e, 0x53, 0x61, 0x74, 0x4d,
	0x6f, 0x6e, 0x52, 0x09, 0x73, 0x61, 0x74, 0x65, 0x6c, 0x6c, 0x69, 0x74, 0x65, 0x12, 0x4b, 0x0a,
	0x0f, 0x67, 0x72, 0x6f, 0x75, 0x6e, 0x64, 0x5f, 0x73, 0x74, 0x61, 0x74, 0x69, 0x6f, 0x6e, 0x73,
	0x18, 0x02, 0x20, 0x03, 0x28, 0x0b, 0x32, 0x22, 0x2e, 0x70, 0x6f, 0x69, 0x6e, 0x74, 0x69, 0x6e,
	0x67, 0x2e, 0x47, 0x72, 0x6f, 0x75, 0x6e, 0x64, 0x53, 0x74, 0x61, 0x74, 0x69, 0x6f, 0x6e, 0x49,
	0x6e, 0x66, 0x6f, 0x72, 0x6d, 0x61, 0x74, 0x69, 0x6f, 0x6e, 0x52, 0x0e, 0x67, 0x72, 0x6f, 0x75,
	0x6e, 0x64, 0x53, 0x74, 0x61, 0x74, 0x69, 0x6f, 0x6e, 0x73, 0x12, 0x34, 0x0a, 0x0a, 0x73, 0x74,
	0x61, 0x72, 0x74, 0x5f, 0x64, 0x61, 0x74, 0x65, 0x18, 0x03, 0x20, 0x01, 0x28, 0x0b, 0x32, 0x15,
	0x2e, 0x67, 0x6f, 0x6f, 0x67, 0x6c, 0x65, 0x2e, 0x74, 0x79, 0x70, 0x65, 0x2e, 0x44, 0x61, 0x74,
	0x65, 0x54, 0x69, 0x6d, 0x65, 0x52, 0x09, 0x73, 0x74, 0x61, 0x72, 0x74, 0x44, 0x61, 0x74, 0x65,
	0x12, 0x32, 0x0a, 0x09, 0x73, 0x74, 0x6f, 0x70, 0x5f, 0x64, 0x61, 0x74, 0x65, 0x18, 0x04, 0x20,
	0x01, 0x28, 0x0b, 0x32, 0x15, 0x2e, 0x67, 0x6f, 0x6f, 0x67, 0x6c, 0x65, 0x2e, 0x74, 0x79, 0x70,
	0x65, 0x2e, 0x44, 0x61, 0x74, 0x65, 0x54, 0x69, 0x6d, 0x65, 0x52, 0x08, 0x73, 0x74, 0x6f, 0x70,
	0x44, 0x61, 0x74, 0x65, 0x22, 0x94, 0x01, 0x0a, 0x0d, 0x4e, 0x65, 0x78, 0x74, 0x50, 0x61, 0x73,
	0x73, 0x52, 0x65, 0x70, 0x6c, 0x79, 0x12, 0x25, 0x0a, 0x0e, 0x73, 0x61, 0x74, 0x65, 0x6c, 0x6c,
	0x69, 0x74, 0x65, 0x5f, 0x6e, 0x61, 0x6d, 0x65, 0x18, 0x01, 0x20, 0x01, 0x28, 0x09, 0x52, 0x0d,
	0x73, 0x61, 0x74, 0x65, 0x6c, 0x6c, 0x69, 0x74, 0x65, 0x4e, 0x61, 0x6d, 0x65, 0x12, 0x21, 0x0a,
	0x0c, 0x73, 0x74, 0x61, 0x74, 0x69, 0x6f, 0x6e, 0x5f, 0x6e, 0x61, 0x6d, 0x65, 0x18, 0x02, 0x20,
	0x01, 0x28, 0x09, 0x52, 0x0b, 0x73, 0x74, 0x61, 0x74, 0x69, 0x6f, 0x6e, 0x4e, 0x61, 0x6d, 0x65,
	0x12, 0x39, 0x0a, 0x08, 0x70, 0x6f, 0x69, 0x6e, 0x74, 0x69, 0x6e, 0x67, 0x18, 0x03, 0x20, 0x03,
	0x28, 0x0b, 0x32, 0x1d, 0x2e, 0x70, 0x6f, 0x69, 0x6e, 0x74, 0x69, 0x6e, 0x67, 0x2e, 0x50, 0x6f,
	0x69, 0x6e, 0x74, 0x69, 0x6e, 0x67, 0x49, 0x6e, 0x66, 0x6f, 0x72, 0x6d, 0x61, 0x74, 0x69, 0x6f,
	0x6e, 0x52, 0x08, 0x70, 0x6f, 0x69, 0x6e, 0x74, 0x69, 0x6e, 0x67, 0x22, 0xa1, 0x01, 0x0a, 0x13,
	0x50, 0x6f, 0x69, 0x6e, 0x74, 0x69, 0x6e, 0x67, 0x49, 0x6e, 0x66, 0x6f, 0x72, 0x6d, 0x61, 0x74,
	0x69, 0x6f, 0x6e, 0x12, 0x29, 0x0a, 0x04, 0x64, 0x61, 0x74, 0x65, 0x18, 0x01, 0x20, 0x01, 0x28,
	0x0b, 0x32, 0x15, 0x2e, 0x67, 0x6f, 0x6f, 0x67, 0x6c, 0x65, 0x2e, 0x74, 0x79, 0x70, 0x65, 0x2e,
	0x44, 0x61, 0x74, 0x65, 0x54, 0x69, 0x6d, 0x65, 0x52, 0x04, 0x64, 0x61, 0x74, 0x65, 0x12, 0x18,
	0x0a, 0x07, 0x61, 0x7a, 0x69, 0x6d, 0x75, 0x74, 0x68, 0x18, 0x02, 0x20, 0x01, 0x28, 0x01, 0x52,
	0x07, 0x61, 0x7a, 0x69, 0x6d, 0x75, 0x74, 0x68, 0x12, 0x1c, 0x0a, 0x09, 0x65, 0x6c, 0x65, 0x76,
	0x61, 0x74, 0x69, 0x6f, 0x6e, 0x18, 0x03, 0x20, 0x01, 0x28, 0x01, 0x52, 0x09, 0x65, 0x6c, 0x65,
	0x76, 0x61, 0x74, 0x69, 0x6f, 0x6e, 0x12, 0x21, 0x0a, 0x0c, 0x72, 0x61, 0x6e, 0x67, 0x65, 0x5f,
	0x6d, 0x65, 0x74, 0x65, 0x72, 0x73, 0x18, 0x05, 0x20, 0x01, 0x28, 0x01, 0x52, 0x0b, 0x72, 0x61,
	0x6e, 0x67, 0x65, 0x4d, 0x65, 0x74, 0x65, 0x72, 0x73, 0x4a, 0x04, 0x08, 0x04, 0x10, 0x05, 0x22,
	0xed, 0x01, 0x0a, 0x0f, 0x53, 0x63, 0x68, 0x65, 0x64, 0x75, 0x6c, 0x65, 0x52, 0x65, 0x71, 0x75,
	0x65, 0x73, 0x74, 0x12, 0x30, 0x0a, 0x0a, 0x73, 0x61, 0x74, 0x65, 0x6c, 0x6c, 0x69, 0x74, 0x65,
	0x73, 0x18, 0x01, 0x20, 0x03, 0x28, 0x0b, 0x32, 0x10, 0x2e, 0x70, 0x6f, 0x69, 0x6e, 0x74, 0x69,
	0x6e, 0x67, 0x2e, 0x53, 0x61, 0x74, 0x4d, 0x6f, 0x6e, 0x52, 0x0a, 0x73, 0x61, 0x74, 0x65, 0x6c,
	0x6c, 0x69, 0x74, 0x65, 0x73, 0x12, 0x3e, 0x0a, 0x08, 0x73, 0x74, 0x61, 0x74, 0x69, 0x6f, 0x6e,
	0x73, 0x18, 0x03, 0x20, 0x03, 0x28, 0x0b, 0x32, 0x22, 0x2e, 0x70, 0x6f, 0x69, 0x6e, 0x74, 0x69,
	0x6e, 0x67, 0x2e, 0x47, 0x72, 0x6f, 0x75, 0x6e, 0x64, 0x53, 0x74, 0x61, 0x74, 0x69, 0x6f, 0x6e,
	0x49, 0x6e, 0x66, 0x6f, 0x72, 0x6d, 0x61, 0x74, 0x69, 0x6f, 0x6e, 0x52, 0x08, 0x73, 0x74, 0x61,
	0x74, 0x69, 0x6f, 0x6e, 0x73, 0x12, 0x34, 0x0a, 0x0a, 0x73, 0x74, 0x61, 0x72, 0x74, 0x5f, 0x64,
	0x61, 0x74, 0x65, 0x18, 0x04, 0x20, 0x01, 0x28, 0x0b, 0x32, 0x15, 0x2e, 0x67, 0x6f, 0x6f, 0x67,
	0x6c, 0x65, 0x2e, 0x74, 0x79, 0x70, 0x65, 0x2e, 0x44, 0x61, 0x74, 0x65, 0x54, 0x69, 0x6d, 0x65,
	0x52, 0x09, 0x73, 0x74, 0x61, 0x72, 0x74, 0x44, 0x61, 0x74, 0x65, 0x12, 0x32, 0x0a, 0x09, 0x73,
	0x74, 0x6f, 0x70, 0x5f, 0x64, 0x61, 0x74, 0x65, 0x18, 0x05, 0x20, 0x01, 0x28, 0x0b, 0x32, 0x15,
	0x2e, 0x67, 0x6f, 0x6f, 0x67, 0x6c, 0x65, 0x2e, 0x74, 0x79, 0x70, 0x65, 0x2e, 0x44, 0x61, 0x74,
	0x65, 0x54, 0x69, 0x6d, 0x65, 0x52, 0x08, 0x73, 0x74, 0x6f, 0x70, 0x44, 0x61, 0x74, 0x65, 0x22,
	0x94, 0x01, 0x0a, 0x06, 0x53, 0x61, 0x74, 0x4d, 0x6f, 0x6e, 0x12, 0x53, 0x0a, 0x15, 0x73, 0x61,
	0x74, 0x65, 0x6c, 0x6c, 0x69, 0x74, 0x65, 0x5f, 0x69, 0x6e, 0x66, 0x6f, 0x72, 0x6d, 0x61, 0x74,
	0x69, 0x6f, 0x6e, 0x18, 0x01, 0x20, 0x01, 0x28, 0x0b, 0x32, 0x1e, 0x2e, 0x70, 0x6f, 0x69, 0x6e,
	0x74, 0x69, 0x6e, 0x67, 0x2e, 0x53, 0x61, 0x74, 0x65, 0x6c, 0x6c, 0x69, 0x74, 0x65, 0x49, 0x6e,
	0x66, 0x6f, 0x72, 0x6d, 0x61, 0x74, 0x69, 0x6f, 0x6e, 0x52, 0x14, 0x73, 0x61, 0x74, 0x65, 0x6c,
	0x6c, 0x69, 0x74, 0x65, 0x49, 0x6e, 0x66, 0x6f, 0x72, 0x6d, 0x61, 0x74, 0x69, 0x6f, 0x6e, 0x12,
	0x35, 0x0a, 0x17, 0x6d, 0x69, 0x6e, 0x69, 0x6d, 0x75, 0x6d, 0x5f, 0x70, 0x61, 0x73, 0x73, 0x5f,
	0x6c, 0x65, 0x6e, 0x67, 0x74, 0x68, 0x5f, 0x73, 0x65, 0x63, 0x18, 0x02, 0x20, 0x01, 0x28, 0x05,
	0x52, 0x14, 0x6d, 0x69, 0x6e, 0x69, 0x6d, 0x75, 0x6d, 0x50, 0x61, 0x73, 0x73, 0x4c, 0x65, 0x6e,
	0x67, 0x74, 0x68, 0x53, 0x65, 0x63, 0x22, 0x53, 0x0a, 0x0d, 0x53, 0x63, 0x68, 0x65, 0x64, 0x75,
	0x6c, 0x65, 0x52, 0x65, 0x70, 0x6c, 0x79, 0x12, 0x42, 0x0a, 0x10, 0x73, 0x61, 0x74, 0x65, 0x6c,
	0x6c, 0x69, 0x74, 0x65, 0x5f, 0x70, 0x61, 0x73, 0x73, 0x65, 0x73, 0x18, 0x01, 0x20, 0x03, 0x28,
	0x0b, 0x32, 0x17, 0x2e, 0x70, 0x6f, 0x69, 0x6e, 0x74, 0x69, 0x6e, 0x67, 0x2e, 0x4e, 0x65, 0x78,
	0x74, 0x50, 0x61, 0x73, 0x73, 0x52, 0x65, 0x70, 0x6c, 0x79, 0x52, 0x0f, 0x73, 0x61, 0x74, 0x65,
	0x6c, 0x6c, 0x69, 0x74, 0x65, 0x50, 0x61, 0x73, 0x73, 0x65, 0x73, 0x32, 0x92, 0x01, 0x0a, 0x0a,
	0x50, 0x72, 0x6f, 0x63, 0x65, 0x73, 0x73, 0x69, 0x6e, 0x67, 0x12, 0x41, 0x0a, 0x0b, 0x47, 0x65,
	0x74, 0x4e, 0x65, 0x78, 0x74, 0x50, 0x61, 0x73, 0x73, 0x12, 0x19, 0x2e, 0x70, 0x6f, 0x69, 0x6e,
	0x74, 0x69, 0x6e, 0x67, 0x2e, 0x4e, 0x65, 0x78, 0x74, 0x50, 0x61, 0x73, 0x73, 0x52, 0x65, 0x71,
	0x75, 0x65, 0x73, 0x74, 0x1a, 0x17, 0x2e, 0x70, 0x6f, 0x69, 0x6e, 0x74, 0x69, 0x6e, 0x67, 0x2e,
	0x4e, 0x65, 0x78, 0x74, 0x50, 0x61, 0x73, 0x73, 0x52, 0x65, 0x70, 0x6c, 0x79, 0x12, 0x41, 0x0a,
	0x0b, 0x47, 0x65, 0x74, 0x53, 0x63, 0x68, 0x65, 0x64, 0x75, 0x6c, 0x65, 0x12, 0x19, 0x2e, 0x70,
	0x6f, 0x69, 0x6e, 0x74, 0x69, 0x6e, 0x67, 0x2e, 0x53, 0x63, 0x68, 0x65, 0x64, 0x75, 0x6c, 0x65,
	0x52, 0x65, 0x71, 0x75, 0x65, 0x73, 0x74, 0x1a, 0x17, 0x2e, 0x70, 0x6f, 0x69, 0x6e, 0x74, 0x69,
	0x6e, 0x67, 0x2e, 0x53, 0x63, 0x68, 0x65, 0x64, 0x75, 0x6c, 0x65, 0x52, 0x65, 0x70, 0x6c, 0x79,
	0x42, 0x6c, 0x0a, 0x1e, 0x66, 0x75, 0x6e, 0x6b, 0x69, 0x74, 0x2e, 0x73, 0x61, 0x74, 0x65, 0x6c,
	0x6c, 0x69, 0x74, 0x65, 0x2d, 0x64, 0x61, 0x74, 0x61, 0x2d, 0x70, 0x72, 0x6f, 0x76, 0x69, 0x64,
	0x65, 0x72, 0x42, 0x14, 0x41, 0x6e, 0x74, 0x65, 0x6e, 0x6e, 0x61, 0x50, 0x6f, 0x69, 0x6e, 0x74,
	0x69, 0x6e, 0x67, 0x50, 0x72, 0x6f, 0x74, 0x6f, 0x50, 0x01, 0x5a, 0x32, 0x67, 0x69, 0x74, 0x68,
	0x75, 0x62, 0x2e, 0x63, 0x6f, 0x6d, 0x2f, 0x46, 0x75, 0x6e, 0x6b, 0x69, 0x74, 0x2f, 0x73, 0x61,
	0x74, 0x65, 0x6c, 0x6c, 0x69, 0x74, 0x65, 0x2d, 0x64, 0x61, 0x74, 0x61, 0x2d, 0x70, 0x72, 0x6f,
	0x76, 0x69, 0x64, 0x65, 0x72, 0x2f, 0x73, 0x61, 0x74, 0x74, 0x72, 0x61, 0x63, 0x6b, 0x62, 0x06,
	0x70, 0x72, 0x6f, 0x74, 0x6f, 0x33,
}

var (
	file_pointing_proto_rawDescOnce sync.Once
	file_pointing_proto_rawDescData = file_pointing_proto_rawDesc
)

func file_pointing_proto_rawDescGZIP() []byte {
	file_pointing_proto_rawDescOnce.Do(func() {
		file_pointing_proto_rawDescData = protoimpl.X.CompressGZIP(file_pointing_proto_rawDescData)
	})
	return file_pointing_proto_rawDescData
}

var file_pointing_proto_msgTypes = make([]protoimpl.MessageInfo, 8)
var file_pointing_proto_goTypes = []interface{}{
	(*SatelliteInformation)(nil),     // 0: pointing.SatelliteInformation
	(*GroundStationInformation)(nil), // 1: pointing.GroundStationInformation
	(*NextPassRequest)(nil),          // 2: pointing.NextPassRequest
	(*NextPassReply)(nil),            // 3: pointing.NextPassReply
	(*PointingInformation)(nil),      // 4: pointing.PointingInformation
	(*ScheduleRequest)(nil),          // 5: pointing.ScheduleRequest
	(*SatMon)(nil),                   // 6: pointing.SatMon
	(*ScheduleReply)(nil),            // 7: pointing.ScheduleReply
	(*datetime.DateTime)(nil),        // 8: google.type.DateTime
}
var file_pointing_proto_depIdxs = []int32{
	6,  // 0: pointing.NextPassRequest.satellite:type_name -> pointing.SatMon
	1,  // 1: pointing.NextPassRequest.ground_stations:type_name -> pointing.GroundStationInformation
	8,  // 2: pointing.NextPassRequest.start_date:type_name -> google.type.DateTime
	8,  // 3: pointing.NextPassRequest.stop_date:type_name -> google.type.DateTime
	4,  // 4: pointing.NextPassReply.pointing:type_name -> pointing.PointingInformation
	8,  // 5: pointing.PointingInformation.date:type_name -> google.type.DateTime
	6,  // 6: pointing.ScheduleRequest.satellites:type_name -> pointing.SatMon
	1,  // 7: pointing.ScheduleRequest.stations:type_name -> pointing.GroundStationInformation
	8,  // 8: pointing.ScheduleRequest.start_date:type_name -> google.type.DateTime
	8,  // 9: pointing.ScheduleRequest.stop_date:type_name -> google.type.DateTime
	0,  // 10: pointing.SatMon.satellite_information:type_name -> pointing.SatelliteInformation
	3,  // 11: pointing.ScheduleReply.satellite_passes:type_name -> pointing.NextPassReply
	2,  // 12: pointing.Processing.GetNextPass:input_type -> pointing.NextPassRequest
	5,  // 13: pointing.Processing.GetSchedule:input_type -> pointing.ScheduleRequest
	3,  // 14: pointing.Processing.GetNextPass:output_type -> pointing.NextPassReply
	7,  // 15: pointing.Processing.GetSchedule:output_type -> pointing.ScheduleReply
	14, // [14:16] is the sub-list for method output_type
	12, // [12:14] is the sub-list for method input_type
	12, // [12:12] is the sub-list for extension type_name
	12, // [12:12] is the sub-list for extension extendee
	0,  // [0:12] is the sub-list for field type_name
}

func init() { file_pointing_proto_init() }
func file_pointing_proto_init() {
	if File_pointing_proto != nil {
		return
	}
	if !protoimpl.UnsafeEnabled {
		file_pointing_proto_msgTypes[0].Exporter = func(v interface{}, i int) interface{} {
			switch v := v.(*SatelliteInformation); i {
			case 0:
				return &v.state
			case 1:
				return &v.sizeCache
			case 2:
				return &v.unknownFields
			default:
				return nil
			}
		}
		file_pointing_proto_msgTypes[1].Exporter = func(v interface{}, i int) interface{} {
			switch v := v.(*GroundStationInformation); i {
			case 0:
				return &v.state
			case 1:
				return &v.sizeCache
			case 2:
				return &v.unknownFields
			default:
				return nil
			}
		}
		file_pointing_proto_msgTypes[2].Exporter = func(v interface{}, i int) interface{} {
			switch v := v.(*NextPassRequest); i {
			case 0:
				return &v.state
			case 1:
				return &v.sizeCache
			case 2:
				return &v.unknownFields
			default:
				return nil
			}
		}
		file_pointing_proto_msgTypes[3].Exporter = func(v interface{}, i int) interface{} {
			switch v := v.(*NextPassReply); i {
			case 0:
				return &v.state
			case 1:
				return &v.sizeCache
			case 2:
				return &v.unknownFields
			default:
				return nil
			}
		}
		file_pointing_proto_msgTypes[4].Exporter = func(v interface{}, i int) interface{} {
			switch v := v.(*PointingInformation); i {
			case 0:
				return &v.state
			case 1:
				return &v.sizeCache
			case 2:
				return &v.unknownFields
			default:
				return nil
			}
		}
		file_pointing_proto_msgTypes[5].Exporter = func(v interface{}, i int) interface{} {
			switch v := v.(*ScheduleRequest); i {
			case 0:
				return &v.state
			case 1:
				return &v.sizeCache
			case 2:
				return &v.unknownFields
			default:
				return nil
			}
		}
		file_pointing_proto_msgTypes[6].Exporter = func(v interface{}, i int) interface{} {
			switch v := v.(*SatMon); i {
			case 0:
				return &v.state
			case 1:
				return &v.sizeCache
			case 2:
				return &v.unknownFields
			default:
				return nil
			}
		}
		file_pointing_proto_msgTypes[7].Exporter = func(v interface{}, i int) interface{} {
			switch v := v.(*ScheduleReply); i {
			case 0:
				return &v.state
			case 1:
				return &v.sizeCache
			case 2:
				return &v.unknownFields
			default:
				return nil
			}
		}
	}
	type x struct{}
	out := protoimpl.TypeBuilder{
		File: protoimpl.DescBuilder{
			GoPackagePath: reflect.TypeOf(x{}).PkgPath(),
			RawDescriptor: file_pointing_proto_rawDesc,
			NumEnums:      0,
			NumMessages:   8,
			NumExtensions: 0,
			NumServices:   1,
		},
		GoTypes:           file_pointing_proto_goTypes,
		DependencyIndexes: file_pointing_proto_depIdxs,
		MessageInfos:      file_pointing_proto_msgTypes,
	}.Build()
	File_pointing_proto = out.File
	file_pointing_proto_rawDesc = nil
	file_pointing_proto_goTypes = nil
	file_pointing_proto_depIdxs = nil
}
