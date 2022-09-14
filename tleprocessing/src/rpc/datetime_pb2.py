"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
_sym_db = _symbol_database.Default()
from google.protobuf import duration_pb2 as google_dot_protobuf_dot_duration__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x0edatetime.proto\x12\x0bgoogle.type\x1a\x1egoogle/protobuf/duration.proto"\xe0\x01\n\x08DateTime\x12\x0c\n\x04year\x18\x01 \x01(\x05\x12\r\n\x05month\x18\x02 \x01(\x05\x12\x0b\n\x03day\x18\x03 \x01(\x05\x12\r\n\x05hours\x18\x04 \x01(\x05\x12\x0f\n\x07minutes\x18\x05 \x01(\x05\x12\x0f\n\x07seconds\x18\x06 \x01(\x05\x12\r\n\x05nanos\x18\x07 \x01(\x05\x12/\n\nutc_offset\x18\x08 \x01(\x0b2\x19.google.protobuf.DurationH\x00\x12*\n\ttime_zone\x18\t \x01(\x0b2\x15.google.type.TimeZoneH\x00B\r\n\x0btime_offset"\'\n\x08TimeZone\x12\n\n\x02id\x18\x01 \x01(\t\x12\x0f\n\x07version\x18\x02 \x01(\tBi\n\x0fcom.google.typeB\rDateTimeProtoP\x01Z<google.golang.org/genproto/googleapis/type/datetime;datetime\xf8\x01\x01\xa2\x02\x03GTPb\x06proto3')
_DATETIME = DESCRIPTOR.message_types_by_name['DateTime']
_TIMEZONE = DESCRIPTOR.message_types_by_name['TimeZone']
DateTime = _reflection.GeneratedProtocolMessageType('DateTime', (_message.Message,), {'DESCRIPTOR': _DATETIME, '__module__': 'datetime_pb2'})
_sym_db.RegisterMessage(DateTime)
TimeZone = _reflection.GeneratedProtocolMessageType('TimeZone', (_message.Message,), {'DESCRIPTOR': _TIMEZONE, '__module__': 'datetime_pb2'})
_sym_db.RegisterMessage(TimeZone)
if _descriptor._USE_C_DESCRIPTORS == False:
    DESCRIPTOR._options = None
    DESCRIPTOR._serialized_options = b'\n\x0fcom.google.typeB\rDateTimeProtoP\x01Z<google.golang.org/genproto/googleapis/type/datetime;datetime\xf8\x01\x01\xa2\x02\x03GTP'
    _DATETIME._serialized_start = 64
    _DATETIME._serialized_end = 288
    _TIMEZONE._serialized_start = 290
    _TIMEZONE._serialized_end = 329