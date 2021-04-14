# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: kikimr/public/api/protos/ydb_common.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='kikimr/public/api/protos/ydb_common.proto',
  package='Ydb',
  syntax='proto3',
  serialized_pb=_b('\n)kikimr/public/api/protos/ydb_common.proto\x12\x03Ydb\"J\n\x0b\x46\x65\x61tureFlag\";\n\x06Status\x12\x16\n\x12STATUS_UNSPECIFIED\x10\x00\x12\x0b\n\x07\x45NABLED\x10\x01\x12\x0c\n\x08\x44ISABLED\x10\x02\"\"\n\x08\x43ostInfo\x12\x16\n\x0e\x63onsumed_units\x18\x01 \x01(\x01\x42(\n\x15\x63om.yandex.ydb.commonB\x0c\x43ommonProtos\xf8\x01\x01\x62\x06proto3')
)



_FEATUREFLAG_STATUS = _descriptor.EnumDescriptor(
  name='Status',
  full_name='Ydb.FeatureFlag.Status',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='STATUS_UNSPECIFIED', index=0, number=0,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='ENABLED', index=1, number=1,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='DISABLED', index=2, number=2,
      options=None,
      type=None),
  ],
  containing_type=None,
  options=None,
  serialized_start=65,
  serialized_end=124,
)
_sym_db.RegisterEnumDescriptor(_FEATUREFLAG_STATUS)


_FEATUREFLAG = _descriptor.Descriptor(
  name='FeatureFlag',
  full_name='Ydb.FeatureFlag',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
    _FEATUREFLAG_STATUS,
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=50,
  serialized_end=124,
)


_COSTINFO = _descriptor.Descriptor(
  name='CostInfo',
  full_name='Ydb.CostInfo',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='consumed_units', full_name='Ydb.CostInfo.consumed_units', index=0,
      number=1, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=126,
  serialized_end=160,
)

_FEATUREFLAG_STATUS.containing_type = _FEATUREFLAG
DESCRIPTOR.message_types_by_name['FeatureFlag'] = _FEATUREFLAG
DESCRIPTOR.message_types_by_name['CostInfo'] = _COSTINFO
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

FeatureFlag = _reflection.GeneratedProtocolMessageType('FeatureFlag', (_message.Message,), dict(
  DESCRIPTOR = _FEATUREFLAG,
  __module__ = 'kikimr.public.api.protos.ydb_common_pb2'
  # @@protoc_insertion_point(class_scope:Ydb.FeatureFlag)
  ))
_sym_db.RegisterMessage(FeatureFlag)

CostInfo = _reflection.GeneratedProtocolMessageType('CostInfo', (_message.Message,), dict(
  DESCRIPTOR = _COSTINFO,
  __module__ = 'kikimr.public.api.protos.ydb_common_pb2'
  # @@protoc_insertion_point(class_scope:Ydb.CostInfo)
  ))
_sym_db.RegisterMessage(CostInfo)


DESCRIPTOR.has_options = True
DESCRIPTOR._options = _descriptor._ParseOptions(descriptor_pb2.FileOptions(), _b('\n\025com.yandex.ydb.commonB\014CommonProtos\370\001\001'))
# @@protoc_insertion_point(module_scope)
