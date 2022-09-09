from datetime import datetime, timedelta
from . import utils, groundstation


def get_schedule(stations: list[groundstation.Station], satellites, start_date: datetime, end_date: datetime) -> list:

    delta = int((end_date - start_date).total_seconds())

    if delta < 0:
        raise ValueError("end_date cannot be before reference_date")

    if delta > utils.SECONDS_IN_DAY:
        raise ValueError("maximum allowed time delta between end_date and reference_date is 24 hours")

    output = []

    # TODO: copy satellites ?
    ref_date = start_date
    previous_station_name = ""
    while end_date > ref_date and len(satellites) > 0:
        earliest_sat_name = ""
        earliest_sat_pass = []
        earliest_sat_index = -1
        earliest_sat_station = stations[0]
        earliest_sat_date = end_date
        for i in range(len(satellites)):
            for station in stations:
                sat_pass = station.next_available_pass(satellites[i]['info'], ref_date, end_date, satellites[i]['minimum_pass_length'])
                if len(sat_pass) != 0:
                    dt = datetime.strptime(sat_pass[0]['date'], utils.PYEPHEM_DATE_PATTERN)
                    if ((station.name != previous_station_name) and (dt < earliest_sat_date)) or \
                            ((station.name == previous_station_name) and
                             (dt < earliest_sat_date + timedelta(seconds=station.positioning_timeout_sec))):
                        earliest_sat_date = dt
                        earliest_sat_pass = sat_pass
                        earliest_sat_name = satellites[i]['info'].name
                        earliest_sat_station = station
                        earliest_sat_index = i

        if earliest_sat_name == "":
            return output

        output.append({
            "satellite": earliest_sat_name,
            "station": earliest_sat_station.name,
            "coordinates": earliest_sat_pass
        })

        previous_station_name = earliest_sat_station.name

        del satellites[earliest_sat_index]

        ref_date = datetime.strptime(earliest_sat_pass[-1]['date'], utils.PYEPHEM_DATE_PATTERN)

    return output


def get_next_pass(satellite, ground_stations: list[groundstation.Station], start_date: datetime, stop_date: datetime,
                  minimum_pass_length_sec: int = 10):
    earliest_pass = []
    earliest_pass_date = stop_date
    earliest_station_name = ""

    for station in ground_stations:
        sat_pass = station.next_available_pass(satellite, start_date, stop_date, 10)
        print("satellite = %s, start_date = %s, stop_date = %s, request.satellite.minimum_pass_length_sec = %d"
              % (satellite.name,
                 start_date,
                 stop_date,
                 minimum_pass_length_sec))

        if len(sat_pass) > 0:
            print("sat_pass has ", len(sat_pass), " items")
            pass_start = datetime.strptime(sat_pass[-1]['date'], utils.PYEPHEM_DATE_PATTERN)
            print("len(earliest_pass) == 0: ", len(earliest_pass) == 0)
            print("pass_start < earliest_pass_date: ", pass_start < earliest_pass_date)
            if len(earliest_pass) == 0 or pass_start < earliest_pass_date:
                earliest_pass_date = pass_start
                earliest_pass = sat_pass
                earliest_station_name = station.name

        if earliest_station_name == "":
            return dict

        return {
            "satellite_name": satellite.name,
            "station_name": earliest_station_name,
            "pass": earliest_pass
        }
