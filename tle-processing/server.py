import logging
from concurrent import futures
from datetime import datetime, timedelta

import ephem
import grpc

import pointing_pb2
import pointing_pb2_grpc
from datetimeutils import grpc_datetime_to_datetime, datetime_to_grpc_datetime
from eph import PYEPHEM_DATE_PATTERN


class ProcessingServicer(pointing_pb2_grpc.ProcessingServicer):
    """Provides methods that implement functionality of pointing server."""

    def GetAntennaPointing(self, request, context):
        start_date = grpc_datetime_to_datetime(request.start_date)
        stop_date = grpc_datetime_to_datetime(request.stop_date)

        delta = int((stop_date - start_date).total_seconds())

        satellite = ephem.readtle(request.satellite_information.satellite_name,
                                  request.satellite_information.tle_line_1,
                                  request.satellite_information.tle_line_2)

        city = ephem.Observer()
        city.lon = request.ground_station_information.station_longitude
        city.lat = request.ground_station_information.station_latitude
        city.elevation = request.ground_station_information.station_altitude

        for x in range(0, delta):
            current_date = start_date + timedelta(0, x)
            current_date_string = current_date.strftime(PYEPHEM_DATE_PATTERN)
            city.date = current_date_string
            satellite.compute(city)

            yield pointing_pb2.AntennaPointingReply(satellite_name=request.satellite_information.satellite_name,
                                                    date=datetime_to_grpc_datetime(datetime.now() + timedelta(hours=x)),
                                                    azimuth=satellite.az,
                                                    elevation=satellite.alt,
                                                    range_meters=satellite.range)


def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    pointing_pb2_grpc.add_ProcessingServicer_to_server(ProcessingServicer(), server)
    server.add_insecure_port('[::]:50051')
    server.start()
    server.wait_for_termination()


if __name__ == '__main__':
    logging.basicConfig()
    serve()
