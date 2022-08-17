import ephem
from datetime import datetime, timedelta
from . import utils


class Station:
    def __init__(self, name: str, latitude: float, longitude: float, altitude: float,
                 minimum_elevation: float = 0, positioning_timeout_sec: int = 0):
        self.name = name
        self.obs = ephem.Observer()
        self.obs.lat = latitude
        self.obs.lon = longitude
        self.obs.elevation = altitude
        self.minimum_elevation = minimum_elevation
        self.positioning_timeout_sec = positioning_timeout_sec

    def next_pass(self, satellite, reference_date: datetime) -> list:
        output = []

        self.obs.date = reference_date
        satellite_pass = self.obs.next_pass(satellite)

        # TODO: satellite copy ?
        start_date = satellite_pass[0].datetime()
        stop_date = satellite_pass[4].datetime()

        delta = int((stop_date - start_date).total_seconds())

        for x in range(0, delta):
            current_date = start_date + timedelta(0, x)
            current_date_string = current_date.strftime(utils.PYEPHEM_DATE_PATTERN)
            self.obs.date = current_date_string
            satellite.compute(self.obs)
            if utils.radians_to_degrees(satellite.alt) > self.minimum_elevation:
                output.append({
                    "date": current_date_string,
                    "azimuth": satellite.az,
                    "elevation": satellite.alt,
                    "range": satellite.range
                })

        return output

    def next_available_pass(self, satellite, reference_date: datetime, end_date: datetime,
                            minimum_pass_time_sec: int = 10) -> list:

        delta = int((end_date - reference_date).total_seconds())

        if delta < 0:
            raise ValueError("end_date cannot be before reference_date")

        if delta > utils.SECONDS_IN_DAY:
            raise ValueError("maximum allowed time delta between end_date and reference_date is 24 hours")

        ref_date = reference_date
        while int((end_date - ref_date).total_seconds()) > 0:
            self.obs.date = ref_date
            satellite_pass = self.obs.next_pass(satellite)

            if utils.radians_to_degrees(satellite_pass[3]) > self.minimum_elevation:
                sat_pass = self.next_pass(satellite, ref_date)
                if len(sat_pass) > minimum_pass_time_sec:
                    return sat_pass

            ref_date = satellite_pass[4].datetime()

        return []

    def next_available_passes(self, satellites, reference_date: datetime, end_date: datetime,
                              minimum_pass_time_sec: int = 10) -> dict:

        delta = int((end_date - reference_date).total_seconds())

        if delta < 0:
            raise ValueError("end_date cannot be before reference_date")

        if delta > utils.SECONDS_IN_DAY:
            raise ValueError("maximum allowed time delta between end_date and reference_date is 24 hours")

        output = {}

        for satellite in satellites:
            output[satellite.name] = self.next_available_pass(satellite,
                                                              reference_date,
                                                              end_date,
                                                              minimum_pass_time_sec)

        return output

    def ordered_passes(self, satellites: list, reference_date: datetime, end_date: datetime,
                       minimum_pass_time_sec: int = 10) -> list:

        delta = int((end_date - reference_date).total_seconds())

        if delta < 0:
            raise ValueError("end_date cannot be before reference_date")

        if delta > utils.SECONDS_IN_DAY:
            raise ValueError("maximum allowed time delta between end_date and reference_date is 24 hours")

        output = []

        ref_date = reference_date

        while int((end_date - ref_date).total_seconds()) > minimum_pass_time_sec \
                and len(satellites) > 0:
            earliest_sat_name = ""
            earliest_sat_index = -1
            earliest_sat_pass = []
            earliest_sat_date = end_date

            # TODO: satellites copy ?
            for i in range(len(satellites)):
                sat_pass = self.next_available_pass(satellites[i], ref_date, end_date, minimum_pass_time_sec)
                if len(sat_pass) > 0:
                    dt = datetime.strptime(sat_pass[0]['date'], utils.PYEPHEM_DATE_PATTERN)
                    if dt < earliest_sat_date:
                        earliest_sat_date = dt
                        earliest_sat_pass = sat_pass
                        earliest_sat_name = satellites[i].name
                        earliest_sat_index = i

            if len(earliest_sat_pass) == 0:
                return output

            output.append({
                'name': earliest_sat_name,
                'pass': earliest_sat_pass
            })

            del satellites[earliest_sat_index]

            ref_date = datetime.strptime(earliest_sat_pass[-1]['date'], utils.PYEPHEM_DATE_PATTERN)
            ref_date = ref_date + timedelta(seconds=self.positioning_timeout_sec)

        return output
