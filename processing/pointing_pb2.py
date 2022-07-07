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


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x0epointing.proto\x12\x08pointing\x1a\x0e\x64\x61tetime.proto\"\x9f\x01\n\x16\x41ntennaPointingRequest\x12=\n\x15satellite_information\x18\x01 \x01(\x0b\x32\x1e.pointing.SatelliteInformation\x12\x46\n\x1aground_station_information\x18\x02 \x01(\x0b\x32\".pointing.GroundStationInformation\"V\n\x14SatelliteInformation\x12\x16\n\x0esatellite_name\x18\x01 \x01(\t\x12\x12\n\ntle_line_1\x18\x02 \x01(\t\x12\x12\n\ntle_line_2\x18\x03 \x01(\t\"\xbe\x01\n\x18GroundStationInformation\x12\x18\n\x10station_latitude\x18\x01 \x01(\x01\x12\x19\n\x11station_longitude\x18\x02 \x01(\x01\x12\x18\n\x10station_altitude\x18\x03 \x01(\x01\x12)\n\nstart_date\x18\x04 \x01(\x0b\x32\x15.google.type.DateTime\x12(\n\tstop_date\x18\x05 \x01(\x0b\x32\x15.google.type.DateTime\"\'\n\x14\x41ntennaPointingReply\x12\x0f\n\x07message\x18\x01 \x01(\t2f\n\nProcessing\x12X\n\x12GetAntennaPointing\x12 .pointing.AntennaPointingRequest\x1a\x1e.pointing.AntennaPointingReply\"\x00\x42l\n\x1e\x66unkit.satellite-data-providerB\x14\x41ntennaPointingProtoP\x01Z2github.com/Funkit/satellite-data-provider/pointingb\x06proto3')



_ANTENNAPOINTINGREQUEST = DESCRIPTOR.message_types_by_name['AntennaPointingRequest']
_SATELLITEINFORMATION = DESCRIPTOR.message_types_by_name['SatelliteInformation']
_GROUNDSTATIONINFORMATION = DESCRIPTOR.message_types_by_name['GroundStationInformation']
_ANTENNAPOINTINGREPLY = DESCRIPTOR.message_types_by_name['AntennaPointingReply']
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

_PROCESSING = DESCRIPTOR.services_by_name['Processing']
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'\n\036funkit.satellite-data-providerB\024AntennaPointingProtoP\001Z2github.com/Funkit/satellite-data-provider/pointing'
  _ANTENNAPOINTINGREQUEST._serialized_start=45
  _ANTENNAPOINTINGREQUEST._serialized_end=204
  _SATELLITEINFORMATION._serialized_start=206
  _SATELLITEINFORMATION._serialized_end=292
  _GROUNDSTATIONINFORMATION._serialized_start=295
  _GROUNDSTATIONINFORMATION._serialized_end=485
  _ANTENNAPOINTINGREPLY._serialized_start=487
  _ANTENNAPOINTINGREPLY._serialized_end=526
  _PROCESSING._serialized_start=528
  _PROCESSING._serialized_end=630
# @@protoc_insertion_point(module_scope)
