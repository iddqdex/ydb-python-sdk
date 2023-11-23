# -*- coding: utf-8 -*-
# flake8: noqa
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: ydb_coordination_v1.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from ydb._grpc.v4.protos import ydb_coordination_pb2 as protos_dot_ydb__coordination__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x19ydb_coordination_v1.proto\x12\x13Ydb.Coordination.V1\x1a\x1dprotos/ydb_coordination.proto2\xca\x03\n\x13\x43oordinationService\x12R\n\x07Session\x12 .Ydb.Coordination.SessionRequest\x1a!.Ydb.Coordination.SessionResponse(\x01\x30\x01\x12W\n\nCreateNode\x12#.Ydb.Coordination.CreateNodeRequest\x1a$.Ydb.Coordination.CreateNodeResponse\x12T\n\tAlterNode\x12\".Ydb.Coordination.AlterNodeRequest\x1a#.Ydb.Coordination.AlterNodeResponse\x12Q\n\x08\x44ropNode\x12!.Ydb.Coordination.DropNodeRequest\x1a\".Ydb.Coordination.DropNodeResponse\x12]\n\x0c\x44\x65scribeNode\x12%.Ydb.Coordination.DescribeNodeRequest\x1a&.Ydb.Coordination.DescribeNodeResponseBq\n\x1etech.ydb.proto.coordination.v1B\x10\x43oordinationGrpcP\x01Z;github.com/ydb-platform/ydb-go-genproto/Ydb_Coordination_V1b\x06proto3')

_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'ydb_coordination_v1_pb2', globals())
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'\n\036tech.ydb.proto.coordination.v1B\020CoordinationGrpcP\001Z;github.com/ydb-platform/ydb-go-genproto/Ydb_Coordination_V1'
  _COORDINATIONSERVICE._serialized_start=82
  _COORDINATIONSERVICE._serialized_end=540
# @@protoc_insertion_point(module_scope)
