# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: terminal.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.protobuf import empty_pb2 as google_dot_protobuf_dot_empty__pb2
from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x0eterminal.proto\x1a\x1bgoogle/protobuf/empty.proto\x1a\x1fgoogle/protobuf/timestamp.proto\"_\n\rpollutionData\x12\n\n\x02id\x18\x01 \x01(\x05\x12-\n\ttimestamp\x18\x02 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12\x13\n\x0b\x63oefficient\x18\x03 \x01(\x02\"^\n\x0cwellnessData\x12\n\n\x02id\x18\x01 \x01(\x05\x12-\n\ttimestamp\x18\x02 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12\x13\n\x0b\x63oefficient\x18\x03 \x01(\x02\"M\n\x07\x61irData\x12!\n\tpollution\x18\x01 \x03(\x0b\x32\x0e.pollutionData\x12\x1f\n\x08wellness\x18\x02 \x03(\x0b\x32\r.wellnessData2B\n\x0csend_results\x12\x32\n\x0csend_results\x12\x08.airData\x1a\x16.google.protobuf.Empty\"\x00\x62\x06proto3')

_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'terminal_pb2', globals())
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _POLLUTIONDATA._serialized_start=80
  _POLLUTIONDATA._serialized_end=175
  _WELLNESSDATA._serialized_start=177
  _WELLNESSDATA._serialized_end=271
  _AIRDATA._serialized_start=273
  _AIRDATA._serialized_end=350
  _SEND_RESULTS._serialized_start=352
  _SEND_RESULTS._serialized_end=418
# @@protoc_insertion_point(module_scope)
