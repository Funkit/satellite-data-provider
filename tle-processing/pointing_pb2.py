# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: pointing.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


import datetime_pb2 as datetime__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x0epointing.proto\x12\x08pointing\x1a\x0e\x64\x61tetime.proto\"\xf4\x01\n\x16\x41ntennaPointingRequest\x12=\n\x15satellite_information\x18\x01 \x01(\x0b\x32\x1e.pointing.SatelliteInformation\x12\x46\n\x1aground_station_information\x18\x02 \x01(\x0b\x32\".pointing.GroundStationInformation\x12)\n\nstart_date\x18\x03 \x01(\x0b\x32\x15.google.type.DateTime\x12(\n\tstop_date\x18\x04 \x01(\x0b\x32\x15.google.type.DateTime\"V\n\x14SatelliteInformation\x12\x16\n\x0esatellite_name\x18\x01 \x01(\t\x12\x12\n\ntle_line_1\x18\x02 \x01(\t\x12\x12\n\ntle_line_2\x18\x03 \x01(\t\"i\n\x18GroundStationInformation\x12\x18\n\x10station_latitude\x18\x01 \x01(\x01\x12\x19\n\x11station_longitude\x18\x02 \x01(\x01\x12\x18\n\x10station_altitude\x18\x03 \x01(\x01\"\x8d\x01\n\x14\x41ntennaPointingReply\x12\x16\n\x0esatellite_name\x18\x01 \x01(\t\x12#\n\x04\x64\x61te\x18\x02 \x01(\x0b\x32\x15.google.type.DateTime\x12\x0f\n\x07\x61zimuth\x18\x03 \x01(\x01\x12\x11\n\televation\x18\x04 \x01(\x01\x12\x14\n\x0crange_meters\x18\x05 \x01(\x01\"\xc7\x01\n\x0fNextPassRequest\x12=\n\x15satellite_information\x18\x01 \x01(\x0b\x32\x1e.pointing.SatelliteInformation\x12\x46\n\x1aground_station_information\x18\x02 \x01(\x0b\x32\".pointing.GroundStationInformation\x12-\n\x0ereference_date\x18\x03 \x01(\x0b\x32\x15.google.type.DateTime2\xb2\x01\n\nProcessing\x12X\n\x12GetAntennaPointing\x12 .pointing.AntennaPointingRequest\x1a\x1e.pointing.AntennaPointingReply0\x01\x12J\n\x0bGetNextPass\x12\x19.pointing.NextPassRequest\x1a\x1e.pointing.AntennaPointingReply0\x01\x42l\n\x1e\x66unkit.satellite-data-providerB\x14\x41ntennaPointingProtoP\x01Z2github.com/Funkit/satellite-data-provider/pointingb\x06proto3')



_ANTENNAPOINTINGREQUEST = DESCRIPTOR.message_types_by_name['AntennaPointingRequest']
_SATELLITEINFORMATION = DESCRIPTOR.message_types_by_name['SatelliteInformation']
_GROUNDSTATIONINFORMATION = DESCRIPTOR.message_types_by_name['GroundStationInformation']
_ANTENNAPOINTINGREPLY = DESCRIPTOR.message_types_by_name['AntennaPointingReply']
_NEXTPASSREQUEST = DESCRIPTOR.message_types_by_name['NextPassRequest']
AntennaPointingRequest = _reflection.GeneratedProtocolMessageType('AntennaPointingRequest', (_message.Message,), {
  'DESCRIPTOR' : _ANTENNAPOINTINGREQUEST,
  '__module__' : 'pointing_pb2'
  # @@protoc_insertion_point(class_scope:pointing.AntennaPointingRequest)
  })
_sym_db.RegisterMessage(AntennaPointingRequest)

SatelliteInformation = _reflection.GeneratedProtocolMessageType('SatelliteInformation', (_message.Message,), {
  'DESCRIPTOR' : _SATELLITEINFORMATION,
  '__module__' : 'pointing_pb2'
  # @@protoc_insertion_point(class_scope:pointing.SatelliteInformation)
  })
_sym_db.RegisterMessage(SatelliteInformation)

GroundStationInformation = _reflection.GeneratedProtocolMessageType('GroundStationInformation', (_message.Message,), {
  'DESCRIPTOR' : _GROUNDSTATIONINFORMATION,
  '__module__' : 'pointing_pb2'
  # @@protoc_insertion_point(class_scope:pointing.GroundStationInformation)
  })
_sym_db.RegisterMessage(GroundStationInformation)

AntennaPointingReply = _reflection.GeneratedProtocolMessageType('AntennaPointingReply', (_message.Message,), {
  'DESCRIPTOR' : _ANTENNAPOINTINGREPLY,
  '__module__' : 'pointing_pb2'
  # @@protoc_insertion_point(class_scope:pointing.AntennaPointingReply)
  })
_sym_db.RegisterMessage(AntennaPointingReply)

NextPassRequest = _reflection.GeneratedProtocolMessageType('NextPassRequest', (_message.Message,), {
  'DESCRIPTOR' : _NEXTPASSREQUEST,
  '__module__' : 'pointing_pb2'
  # @@protoc_insertion_point(class_scope:pointing.NextPassRequest)
  })
_sym_db.RegisterMessage(NextPassRequest)

_PROCESSING = DESCRIPTOR.services_by_name['Processing']
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'\n\036funkit.satellite-data-providerB\024AntennaPointingProtoP\001Z2github.com/Funkit/satellite-data-provider/pointing'
  _ANTENNAPOINTINGREQUEST._serialized_start=45
  _ANTENNAPOINTINGREQUEST._serialized_end=289
  _SATELLITEINFORMATION._serialized_start=291
  _SATELLITEINFORMATION._serialized_end=377
  _GROUNDSTATIONINFORMATION._serialized_start=379
  _GROUNDSTATIONINFORMATION._serialized_end=484
  _ANTENNAPOINTINGREPLY._serialized_start=487
  _ANTENNAPOINTINGREPLY._serialized_end=628
  _NEXTPASSREQUEST._serialized_start=631
  _NEXTPASSREQUEST._serialized_end=830
  _PROCESSING._serialized_start=833
  _PROCESSING._serialized_end=1011
# @@protoc_insertion_point(module_scope)