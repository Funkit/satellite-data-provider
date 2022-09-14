"""Client and server classes corresponding to protobuf-defined services."""
import grpc
from . import pointing_pb2 as pointing__pb2

class ProcessingStub(object):
    """This Service processes satellite and ground station information and returns pointing information for satellite tracking.
    """

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.GetNextPass = channel.unary_unary('/pointing.Processing/GetNextPass', request_serializer=pointing__pb2.NextPassRequest.SerializeToString, response_deserializer=pointing__pb2.NextPassReply.FromString)
        self.GetSchedule = channel.unary_unary('/pointing.Processing/GetSchedule', request_serializer=pointing__pb2.ScheduleRequest.SerializeToString, response_deserializer=pointing__pb2.ScheduleReply.FromString)

class ProcessingServicer(object):
    """This Service processes satellite and ground station information and returns pointing information for satellite tracking.
    """

    def GetNextPass(self, request, context):
        """For a given satellite, provided a list of ground stations, returns the first satellite pass that can be monitored
        between start_date and stop_date.
        A pass consists in a list of antenna pointing information (azimuth, elevation...) necessary for tracking the satellite.
        A pass is considered valid for a given station when the elevation is above minimum_elevation and the total pass duration is above
        minimum_pass_length_sec.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetSchedule(self, request, context):
        """Provided a list of satellites and ground stations, returns a list of passes that monitors as many satellites as possible between
        start_date and stop_date.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

def add_ProcessingServicer_to_server(servicer, server):
    rpc_method_handlers = {'GetNextPass': grpc.unary_unary_rpc_method_handler(servicer.GetNextPass, request_deserializer=pointing__pb2.NextPassRequest.FromString, response_serializer=pointing__pb2.NextPassReply.SerializeToString), 'GetSchedule': grpc.unary_unary_rpc_method_handler(servicer.GetSchedule, request_deserializer=pointing__pb2.ScheduleRequest.FromString, response_serializer=pointing__pb2.ScheduleReply.SerializeToString)}
    generic_handler = grpc.method_handlers_generic_handler('pointing.Processing', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))

class Processing(object):
    """This Service processes satellite and ground station information and returns pointing information for satellite tracking.
    """

    @staticmethod
    def GetNextPass(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None):
        return grpc.experimental.unary_unary(request, target, '/pointing.Processing/GetNextPass', pointing__pb2.NextPassRequest.SerializeToString, pointing__pb2.NextPassReply.FromString, options, channel_credentials, insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def GetSchedule(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None):
        return grpc.experimental.unary_unary(request, target, '/pointing.Processing/GetSchedule', pointing__pb2.ScheduleRequest.SerializeToString, pointing__pb2.ScheduleReply.FromString, options, channel_credentials, insecure, call_credentials, compression, wait_for_ready, timeout, metadata)