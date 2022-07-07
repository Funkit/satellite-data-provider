# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

import pointing_pb2 as pointing__pb2


class ProcessingStub(object):
    """The greeting service definition.
    """

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.GetAntennaPointing = channel.unary_unary(
                '/pointing.Processing/GetAntennaPointing',
                request_serializer=pointing__pb2.AntennaPointingRequest.SerializeToString,
                response_deserializer=pointing__pb2.AntennaPointingReply.FromString,
                )


class ProcessingServicer(object):
    """The greeting service definition.
    """

    def GetAntennaPointing(self, request, context):
        """Sends a greeting
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_ProcessingServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'GetAntennaPointing': grpc.unary_unary_rpc_method_handler(
                    servicer.GetAntennaPointing,
                    request_deserializer=pointing__pb2.AntennaPointingRequest.FromString,
                    response_serializer=pointing__pb2.AntennaPointingReply.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'pointing.Processing', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class Processing(object):
    """The greeting service definition.
    """

    @staticmethod
    def GetAntennaPointing(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/pointing.Processing/GetAntennaPointing',
            pointing__pb2.AntennaPointingRequest.SerializeToString,
            pointing__pb2.AntennaPointingReply.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
