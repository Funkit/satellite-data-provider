"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
_sym_db = _symbol_database.Default()
from . import datetime_pb2 as datetime__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x0epointing.proto\x12\x08pointing\x1a\x0edatetime.proto"L\n\x14SatelliteInformation\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x12\n\ntle_line_1\x18\x02 \x01(\t\x12\x12\n\ntle_line_2\x18\x03 \x01(\t"\xa1\x01\n\x18GroundStationInformation\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x10\n\x08latitude\x18\x02 \x01(\x01\x12\x11\n\tlongitude\x18\x03 \x01(\x01\x12\x10\n\x08altitude\x18\x04 \x01(\x01\x12\x19\n\x11minimum_elevation\x18\x05 \x01(\x01\x12%\n\x1dstation_positioning_delay_sec\x18\x06 \x01(\x05"\xc8\x01\n\x0fNextPassRequest\x12#\n\tsatellite\x18\x01 \x01(\x0b2\x10.pointing.SatMon\x12;\n\x0fground_stations\x18\x02 \x03(\x0b2".pointing.GroundStationInformation\x12)\n\nstart_date\x18\x03 \x01(\x0b2\x15.google.type.DateTime\x12(\n\tstop_date\x18\x04 \x01(\x0b2\x15.google.type.DateTime"n\n\rNextPassReply\x12\x16\n\x0esatellite_name\x18\x01 \x01(\t\x12\x14\n\x0cstation_name\x18\x02 \x01(\t\x12/\n\x08pointing\x18\x03 \x03(\x0b2\x1d.pointing.PointingInformation"z\n\x13PointingInformation\x12#\n\x04date\x18\x01 \x01(\x0b2\x15.google.type.DateTime\x12\x0f\n\x07azimuth\x18\x02 \x01(\x01\x12\x11\n\televation\x18\x03 \x01(\x01\x12\x14\n\x0crange_meters\x18\x05 \x01(\x01J\x04\x08\x04\x10\x05"\xc2\x01\n\x0fScheduleRequest\x12$\n\nsatellites\x18\x01 \x03(\x0b2\x10.pointing.SatMon\x124\n\x08stations\x18\x03 \x03(\x0b2".pointing.GroundStationInformation\x12)\n\nstart_date\x18\x04 \x01(\x0b2\x15.google.type.DateTime\x12(\n\tstop_date\x18\x05 \x01(\x0b2\x15.google.type.DateTime"h\n\x06SatMon\x12=\n\x15satellite_information\x18\x01 \x01(\x0b2\x1e.pointing.SatelliteInformation\x12\x1f\n\x17minimum_pass_length_sec\x18\x02 \x01(\x05"B\n\rScheduleReply\x121\n\x10satellite_passes\x18\x01 \x03(\x0b2\x17.pointing.NextPassReply2\x92\x01\n\nProcessing\x12A\n\x0bGetNextPass\x12\x19.pointing.NextPassRequest\x1a\x17.pointing.NextPassReply\x12A\n\x0bGetSchedule\x12\x19.pointing.ScheduleRequest\x1a\x17.pointing.ScheduleReplyBl\n\x1efunkit.satellite-data-providerB\x14AntennaPointingProtoP\x01Z2github.com/Funkit/satellite-data-provider/pointingb\x06proto3')
_SATELLITEINFORMATION = DESCRIPTOR.message_types_by_name['SatelliteInformation']
_GROUNDSTATIONINFORMATION = DESCRIPTOR.message_types_by_name['GroundStationInformation']
_NEXTPASSREQUEST = DESCRIPTOR.message_types_by_name['NextPassRequest']
_NEXTPASSREPLY = DESCRIPTOR.message_types_by_name['NextPassReply']
_POINTINGINFORMATION = DESCRIPTOR.message_types_by_name['PointingInformation']
_SCHEDULEREQUEST = DESCRIPTOR.message_types_by_name['ScheduleRequest']
_SATMON = DESCRIPTOR.message_types_by_name['SatMon']
_SCHEDULEREPLY = DESCRIPTOR.message_types_by_name['ScheduleReply']
SatelliteInformation = _reflection.GeneratedProtocolMessageType('SatelliteInformation', (_message.Message,), {'DESCRIPTOR': _SATELLITEINFORMATION, '__module__': 'pointing_pb2'})
_sym_db.RegisterMessage(SatelliteInformation)
GroundStationInformation = _reflection.GeneratedProtocolMessageType('GroundStationInformation', (_message.Message,), {'DESCRIPTOR': _GROUNDSTATIONINFORMATION, '__module__': 'pointing_pb2'})
_sym_db.RegisterMessage(GroundStationInformation)
NextPassRequest = _reflection.GeneratedProtocolMessageType('NextPassRequest', (_message.Message,), {'DESCRIPTOR': _NEXTPASSREQUEST, '__module__': 'pointing_pb2'})
_sym_db.RegisterMessage(NextPassRequest)
NextPassReply = _reflection.GeneratedProtocolMessageType('NextPassReply', (_message.Message,), {'DESCRIPTOR': _NEXTPASSREPLY, '__module__': 'pointing_pb2'})
_sym_db.RegisterMessage(NextPassReply)
PointingInformation = _reflection.GeneratedProtocolMessageType('PointingInformation', (_message.Message,), {'DESCRIPTOR': _POINTINGINFORMATION, '__module__': 'pointing_pb2'})
_sym_db.RegisterMessage(PointingInformation)
ScheduleRequest = _reflection.GeneratedProtocolMessageType('ScheduleRequest', (_message.Message,), {'DESCRIPTOR': _SCHEDULEREQUEST, '__module__': 'pointing_pb2'})
_sym_db.RegisterMessage(ScheduleRequest)
SatMon = _reflection.GeneratedProtocolMessageType('SatMon', (_message.Message,), {'DESCRIPTOR': _SATMON, '__module__': 'pointing_pb2'})
_sym_db.RegisterMessage(SatMon)
ScheduleReply = _reflection.GeneratedProtocolMessageType('ScheduleReply', (_message.Message,), {'DESCRIPTOR': _SCHEDULEREPLY, '__module__': 'pointing_pb2'})
_sym_db.RegisterMessage(ScheduleReply)
_PROCESSING = DESCRIPTOR.services_by_name['Processing']
if _descriptor._USE_C_DESCRIPTORS == False:
    DESCRIPTOR._options = None
    DESCRIPTOR._serialized_options = b'\n\x1efunkit.satellite-data-providerB\x14AntennaPointingProtoP\x01Z2github.com/Funkit/satellite-data-provider/pointing'
    _SATELLITEINFORMATION._serialized_start = 44
    _SATELLITEINFORMATION._serialized_end = 120
    _GROUNDSTATIONINFORMATION._serialized_start = 123
    _GROUNDSTATIONINFORMATION._serialized_end = 284
    _NEXTPASSREQUEST._serialized_start = 287
    _NEXTPASSREQUEST._serialized_end = 487
    _NEXTPASSREPLY._serialized_start = 489
    _NEXTPASSREPLY._serialized_end = 599
    _POINTINGINFORMATION._serialized_start = 601
    _POINTINGINFORMATION._serialized_end = 723
    _SCHEDULEREQUEST._serialized_start = 726
    _SCHEDULEREQUEST._serialized_end = 920
    _SATMON._serialized_start = 922
    _SATMON._serialized_end = 1026
    _SCHEDULEREPLY._serialized_start = 1028
    _SCHEDULEREPLY._serialized_end = 1094
    _PROCESSING._serialized_start = 1097
    _PROCESSING._serialized_end = 1243