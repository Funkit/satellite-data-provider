from concurrent import futures
import logging

import grpc
import pointing_pb2
import pointing_pb2_grpc


class ProcessingServicer(pointing_pb2_grpc.ProcessingServicer):
    """Provides methods that implement functionality of pointing server."""

    def GetAntennaPointing(self, request, context):
        return pointing_pb2.AntennaPointingReply(message="Satellite name = %s" % request.satellite_information.satellite_name)


def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    pointing_pb2_grpc.add_ProcessingServicer_to_server(ProcessingServicer(), server)
    server.add_insecure_port('[::]:50051')
    server.start()
    server.wait_for_termination()


if __name__ == '__main__':
    logging.basicConfig()
    serve()


