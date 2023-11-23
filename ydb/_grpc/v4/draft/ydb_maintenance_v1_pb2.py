# -*- coding: utf-8 -*-
# flake8: noqa
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: draft/ydb_maintenance_v1.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from draft.protos import ydb_maintenance_pb2 as draft_dot_protos_dot_ydb__maintenance__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x1e\x64raft/ydb_maintenance_v1.proto\x12\x12Ydb.Maintenance.V1\x1a\"draft/protos/ydb_maintenance.proto2\x84\t\n\x12MaintenanceService\x12g\n\x10ListClusterNodes\x12(.Ydb.Maintenance.ListClusterNodesRequest\x1a).Ydb.Maintenance.ListClusterNodesResponse\x12p\n\x15\x43reateMaintenanceTask\x12-.Ydb.Maintenance.CreateMaintenanceTaskRequest\x1a(.Ydb.Maintenance.MaintenanceTaskResponse\x12r\n\x16RefreshMaintenanceTask\x12..Ydb.Maintenance.RefreshMaintenanceTaskRequest\x1a(.Ydb.Maintenance.MaintenanceTaskResponse\x12t\n\x19GetMaintenanceTaskDetails\x12*.Ydb.Maintenance.GetMaintenanceTaskRequest\x1a+.Ydb.Maintenance.GetMaintenanceTaskResponse\x12s\n\x14ListMaintenanceTasks\x12,.Ydb.Maintenance.ListMaintenanceTasksRequest\x1a-.Ydb.Maintenance.ListMaintenanceTasksResponse\x12r\n\x13\x44ropMaintenanceTask\x12+.Ydb.Maintenance.DropMaintenanceTaskRequest\x1a..Ydb.Maintenance.ManageMaintenanceTaskResponse\x12~\n\x19ProlongateMaintenanceTask\x12\x31.Ydb.Maintenance.ProlongateMaintenanceTaskRequest\x1a..Ydb.Maintenance.ManageMaintenanceTaskResponse\x12]\n\rReleasePermit\x12%.Ydb.Maintenance.ReleasePermitRequest\x1a%.Ydb.Maintenance.ManagePermitResponse\x12\x63\n\x10ProlongatePermit\x12(.Ydb.Maintenance.ProlongatePermitRequest\x1a%.Ydb.Maintenance.ManagePermitResponse\x12|\n\x17GetReadableActionReason\x12/.Ydb.Maintenance.GetReadableActionReasonRequest\x1a\x30.Ydb.Maintenance.GetReadableActionReasonResponseBd\n tech.ydb.proto.draft.maintenanceZ@github.com/ydb-platform/ydb-go-genproto/draft/Ydb_Maintenance_V1b\x06proto3')

_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'draft.ydb_maintenance_v1_pb2', globals())
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'\n tech.ydb.proto.draft.maintenanceZ@github.com/ydb-platform/ydb-go-genproto/draft/Ydb_Maintenance_V1'
  _MAINTENANCESERVICE._serialized_start=91
  _MAINTENANCESERVICE._serialized_end=1247
# @@protoc_insertion_point(module_scope)
