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

    def pass_is_available(self, sat_pass, reference_date: datetime = datetime.now(), minimum_pass_time_sec: int = 10):
        if len(sat_pass) == 6:
            if utils.radians_to_degrees(sat_pass[3]) > self.minimum_elevation:
                delta = int((sat_pass[4].datetime() - sat_pass[0].datetime()).total_seconds())
                if delta >= minimum_pass_time_sec:
                    return True
        return False

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
                delta = int((satellite_pass[4].datetime() - satellite_pass[0].datetime()).total_seconds())

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
