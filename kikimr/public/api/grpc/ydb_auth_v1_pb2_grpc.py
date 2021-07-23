# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
import grpc

from kikimr.public.api.protos import ydb_auth_pb2 as kikimr_dot_public_dot_api_dot_protos_dot_ydb__auth__pb2


class AuthServiceStub(object):
  # missing associated documentation comment in .proto file
  pass

  def __init__(self, channel):
    """Constructor.

    Args:
      channel: A grpc.Channel.
    """
    self.Login = channel.unary_unary(
        '/Ydb.Auth.V1.AuthService/Login',
        request_serializer=kikimr_dot_public_dot_api_dot_protos_dot_ydb__auth__pb2.LoginRequest.SerializeToString,
        response_deserializer=kikimr_dot_public_dot_api_dot_protos_dot_ydb__auth__pb2.LoginResponse.FromString,
        )


class AuthServiceServicer(object):
  # missing associated documentation comment in .proto file
  pass

  def Login(self, request, context):
    """Perform login using built-in auth system
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')


def add_AuthServiceServicer_to_server(servicer, server):
  rpc_method_handlers = {
      'Login': grpc.unary_unary_rpc_method_handler(
          servicer.Login,
          request_deserializer=kikimr_dot_public_dot_api_dot_protos_dot_ydb__auth__pb2.LoginRequest.FromString,
          response_serializer=kikimr_dot_public_dot_api_dot_protos_dot_ydb__auth__pb2.LoginResponse.SerializeToString,
      ),
  }
  generic_handler = grpc.method_handlers_generic_handler(
      'Ydb.Auth.V1.AuthService', rpc_method_handlers)
  server.add_generic_rpc_handlers((generic_handler,))
