# -*- coding: utf-8 -*-
# flake8: noqa
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: ydb_export_v1.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from ydb._grpc.v4.protos import ydb_export_pb2 as protos_dot_ydb__export__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x13ydb_export_v1.proto\x12\rYdb.Export.V1\x1a\x17protos/ydb_export.proto2\xa9\x01\n\rExportService\x12K\n\nExportToYt\x12\x1d.Ydb.Export.ExportToYtRequest\x1a\x1e.Ydb.Export.ExportToYtResponse\x12K\n\nExportToS3\x12\x1d.Ydb.Export.ExportToS3Request\x1a\x1e.Ydb.Export.ExportToS3ResponseBQ\n\x18tech.ydb.proto.export.v1Z5github.com/ydb-platform/ydb-go-genproto/Ydb_Export_V1b\x06proto3')

_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'ydb_export_v1_pb2', globals())
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'\n\030tech.ydb.proto.export.v1Z5github.com/ydb-platform/ydb-go-genproto/Ydb_Export_V1'
  _EXPORTSERVICE._serialized_start=64
  _EXPORTSERVICE._serialized_end=233
# @@protoc_insertion_point(module_scope)
