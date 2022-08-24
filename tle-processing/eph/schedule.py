from datetime import datetime, timedelta
from . import utils, groundstation


def get_schedule(stations: list[groundstation.Station], satellites, start_date: datetime, end_date: datetime,
                 minimum_pass_time_sec: int = 10) -> list:

    delta = int((end_date - start_date).total_seconds())

    if delta < 0:
        raise ValueError("end_date cannot be before reference_date")

    if delta > utils.SECONDS_IN_DAY:
        raise ValueError("maximum allowed time delta between end_date and reference_date is 24 hours")

    output = []

    # TODO: copy satellites ?
    ref_date = start_date
    previous_station_name = ""
    while int((end_date - ref_date).total_seconds()) > minimum_pass_time_sec \
            and len(satellites) > 0:
        earliest_sat_name = ""
        earliest_sat_pass = []
        earliest_sat_index = -1
        earliest_sat_station = stations[0]
        earliest_sat_date = end_date
        for i in range(len(satellites)):
            for station in stations:
                sat_pass = station.next_available_pass(satellites[i], ref_date, end_date, minimum_pass_time_sec)
                if len(sat_pass) != 0:
                    dt = datetime.strptime(sat_pass[0]['date'], utils.PYEPHEM_DATE_PATTERN)
                    if ((station.name != previous_station_name) and (dt  < earliest_sat_date)) or \
                            ((station.name == previous_station_name) and (dt  < earliest_sat_date + timedelta(seconds=station.positioning_timeout_sec))):
                        earliest_sat_date = dt
                        earliest_sat_pass = sat_pass
                        earliest_sat_name = satellites[i].name
                        earliest_sat_station = station
                        earliest_sat_index = i

        if earliest_sat_name == "":
            return output

        output.append({
            "satellite": earliest_sat_name,
            "station": earliest_sat_station.name,
            "pass": earliest_sat_pass
        })

        previous_station_name = earliest_sat_station.name

        del satellites[earliest_sat_index]

        ref_date = datetime.strptime(earliest_sat_pass[-1]['date'], utils.PYEPHEM_DATE_PATTERN)

    return output
