# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
import grpc

from kikimr.public.api.protos.draft import streaming_pb2 as kikimr_dot_public_dot_api_dot_protos_dot_draft_dot_streaming__pb2


class StreamingServiceStub(object):
  # missing associated documentation comment in .proto file
  pass

  def __init__(self, channel):
    """Constructor.

    Args:
      channel: A grpc.Channel.
    """
    self.InstallQuery = channel.unary_unary(
        '/Streaming.V1.StreamingService/InstallQuery',
        request_serializer=kikimr_dot_public_dot_api_dot_protos_dot_draft_dot_streaming__pb2.InstallQueryRequest.SerializeToString,
        response_deserializer=kikimr_dot_public_dot_api_dot_protos_dot_draft_dot_streaming__pb2.InstallQueryResponse.FromString,
        )
    self.DeleteQuery = channel.unary_unary(
        '/Streaming.V1.StreamingService/DeleteQuery',
        request_serializer=kikimr_dot_public_dot_api_dot_protos_dot_draft_dot_streaming__pb2.DeleteQueryRequest.SerializeToString,
        response_deserializer=kikimr_dot_public_dot_api_dot_protos_dot_draft_dot_streaming__pb2.DeleteQueryResponse.FromString,
        )
    self.ListQueries = channel.unary_unary(
        '/Streaming.V1.StreamingService/ListQueries',
        request_serializer=kikimr_dot_public_dot_api_dot_protos_dot_draft_dot_streaming__pb2.ListQueriesRequest.SerializeToString,
        response_deserializer=kikimr_dot_public_dot_api_dot_protos_dot_draft_dot_streaming__pb2.ListQueriesResponse.FromString,
        )
    self.DescribeQuery = channel.unary_unary(
        '/Streaming.V1.StreamingService/DescribeQuery',
        request_serializer=kikimr_dot_public_dot_api_dot_protos_dot_draft_dot_streaming__pb2.DescribeQueryRequest.SerializeToString,
        response_deserializer=kikimr_dot_public_dot_api_dot_protos_dot_draft_dot_streaming__pb2.DescribeQueryResponse.FromString,
        )


class StreamingServiceServicer(object):
  # missing associated documentation comment in .proto file
  pass

  def InstallQuery(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def DeleteQuery(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def ListQueries(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def DescribeQuery(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')


def add_StreamingServiceServicer_to_server(servicer, server):
  rpc_method_handlers = {
      'InstallQuery': grpc.unary_unary_rpc_method_handler(
          servicer.InstallQuery,
          request_deserializer=kikimr_dot_public_dot_api_dot_protos_dot_draft_dot_streaming__pb2.InstallQueryRequest.FromString,
          response_serializer=kikimr_dot_public_dot_api_dot_protos_dot_draft_dot_streaming__pb2.InstallQueryResponse.SerializeToString,
      ),
      'DeleteQuery': grpc.unary_unary_rpc_method_handler(
          servicer.DeleteQuery,
          request_deserializer=kikimr_dot_public_dot_api_dot_protos_dot_draft_dot_streaming__pb2.DeleteQueryRequest.FromString,
          response_serializer=kikimr_dot_public_dot_api_dot_protos_dot_draft_dot_streaming__pb2.DeleteQueryResponse.SerializeToString,
      ),
      'ListQueries': grpc.unary_unary_rpc_method_handler(
          servicer.ListQueries,
          request_deserializer=kikimr_dot_public_dot_api_dot_protos_dot_draft_dot_streaming__pb2.ListQueriesRequest.FromString,
          response_serializer=kikimr_dot_public_dot_api_dot_protos_dot_draft_dot_streaming__pb2.ListQueriesResponse.SerializeToString,
      ),
      'DescribeQuery': grpc.unary_unary_rpc_method_handler(
          servicer.DescribeQuery,
          request_deserializer=kikimr_dot_public_dot_api_dot_protos_dot_draft_dot_streaming__pb2.DescribeQueryRequest.FromString,
          response_serializer=kikimr_dot_public_dot_api_dot_protos_dot_draft_dot_streaming__pb2.DescribeQueryResponse.SerializeToString,
      ),
  }
  generic_handler = grpc.method_handlers_generic_handler(
      'Streaming.V1.StreamingService', rpc_method_handlers)
  server.add_generic_rpc_handlers((generic_handler,))
