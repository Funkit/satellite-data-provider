import logging
from concurrent import futures
from datetime import datetime

import ephem
import grpc

import pointing_pb2
import pointing_pb2_grpc
from datetimeutils import grpc_datetime_to_datetime, datetime_to_grpc_datetime
from eph import groundstation, utils, schedule


def format_satellite_passes(satellite_passes):
    output = []

    for sat_pass in satellite_passes:
        formatted_pass = [pointing_pb2.PointingInformation(date=datetime_to_grpc_datetime(datetime.strptime(x['date'], utils.PYEPHEM_DATE_PATTERN)),
                                                           azimuth=x['azimuth'],
                                                           elevation=x['elevation'],
                                                           range_meters=x['range'])
                          for x in sat_pass['coordinates']]
        output.append(pointing_pb2.NextPassReply(satellite_name=sat_pass['satellite'],
                                                 station_name=sat_pass['station'],
                                                 pointing=formatted_pass))

    return output


class ProcessingServicer(pointing_pb2_grpc.ProcessingServicer):
    """Provides methods that implement functionality of sattrack server."""

    def GetNextPass(self, request, context):
        start_date = grpc_datetime_to_datetime(request.start_date)
        stop_date = grpc_datetime_to_datetime(request.stop_date)

        satellite = ephem.readtle(request.satellite.satellite_information.name,
                                  request.satellite.satellite_information.tle_line_1,
                                  request.satellite.satellite_information.tle_line_2)

        earliest_pass = []
        earliest_pass_date = stop_date
        earliest_station_name = ""

        for station in request.ground_stations:
            st = groundstation.Station(station.name,
                                       station.latitude,
                                       station.longitude,
                                       station.altitude,
                                       station.minimum_elevation,
                                       station.station_positioning_delay_sec)

            sat_pass = st.next_available_pass(satellite, start_date, stop_date)
            print(len(sat_pass))

            if len(sat_pass) > 0:
                pass_start = datetime.strptime(sat_pass[-1]['date'], utils.PYEPHEM_DATE_PATTERN)
                if len(earliest_pass) == 0 or pass_start < earliest_pass_date:
                    earliest_pass_date = pass_start
                    earliest_pass = sat_pass
                    earliest_station_name = station.name

        earliest_formatted_pass = [pointing_pb2.PointingInformation(date=datetime_to_grpc_datetime(datetime.strptime(x['date'], utils.PYEPHEM_DATE_PATTERN)),
                                                                    azimuth=x['azimuth'],
                                                                    elevation=x['elevation'],
                                                                    range_meters=x['range'])
                                   for x in earliest_pass]

        return pointing_pb2.NextPassReply(satellite_name=request.satellite.satellite_information.name,
                                          station_name=earliest_station_name,
                                          pointing=earliest_formatted_pass)

    def GetSchedule(self, request, context):
        start_date = grpc_datetime_to_datetime(request.start_date)
        stop_date = grpc_datetime_to_datetime(request.stop_date)

        satellites = [
            {
                "info": ephem.readtle(sat.satellite_information.name,
                                      sat.satellite_information.tle_line_1,
                                      sat.satellite_information.tle_line_2),
                "minimum_pass_length": sat.minimum_pass_length_sec
            }
            for sat in request.satellites
        ]

        stations = [groundstation.Station(station.name,
                                          station.latitude,
                                          station.longitude,
                                          station.altitude,
                                          station.minimum_elevation,
                                          station.station_positioning_delay_sec) for station in request.stations]

        satellite_passes = schedule.get_schedule(stations, satellites, start_date, stop_date)

        return pointing_pb2.ScheduleReply(satellite_passes=format_satellite_passes(satellite_passes))


def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    pointing_pb2_grpc.add_ProcessingServicer_to_server(ProcessingServicer(), server)
    server.add_insecure_port('[::]:50051')
    server.start()
    server.wait_for_termination()


if __name__ == '__main__':
    logging.basicConfig()
    serve()
