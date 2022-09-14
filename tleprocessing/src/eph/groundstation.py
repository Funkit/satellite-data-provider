from typing import Tuple
import ephem
from datetime import datetime, timedelta
from . import utils


class Station:
    def __init__(self, name: str, latitude: float, longitude: float, altitude: float,
                 minimum_elevation_degrees: float = 0, positioning_timeout_sec: int = 0):
        self.name = name
        self.obs = ephem.Observer()
        self.obs.lat = latitude
        self.obs.lon = longitude
        self.obs.elevation = altitude
        self.minimum_elevation = minimum_elevation_degrees
        self.positioning_timeout_sec = positioning_timeout_sec

    def next_pass(self, satellite, reference_date: datetime) -> Tuple[datetime, datetime, list]:
        """
        Returns a list containing the date, azimuth, elevation and range per second for next visibility window.
        """

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
            output.append({
                "date": current_date_string,
                "azimuth": satellite.az,
                "elevation": satellite.alt,
                "range": satellite.range
            })

        return start_date, stop_date, output

    def next_available_pass(self, satellite, start_date: datetime, end_date: datetime,
                            minimum_pass_time_sec: int = 10) -> Tuple[datetime, datetime, list[dict]]:
        """
        Returns the next availability window between start_date and end_date where
        there are at least minimum_pass_time_sec position samples with elevation above self.minimum_elevation
        """

        delta = int((end_date - start_date).total_seconds())

        if delta < 0:
            raise ValueError("end_date cannot be before reference_date")

        if delta > utils.SECONDS_IN_DAY:
            raise ValueError("maximum allowed time delta between end_date and reference_date is 24 hours")

        current_date = start_date
        while int((end_date - current_date).total_seconds()) > 0:
            self.obs.date = current_date
            start_date, stop_date, satellite_pass = self.next_pass(satellite, current_date)

            available_pass = [item for item in satellite_pass if
                              item['elevation'] > self.minimum_elevation]

            if len(available_pass) >= minimum_pass_time_sec:
                return datetime.strptime(available_pass[0]["date"], utils.PYEPHEM_DATE_PATTERN), \
                       datetime.strptime(available_pass[-1]["date"], utils.PYEPHEM_DATE_PATTERN), available_pass

            current_date = stop_date

        return start_date, end_date, []

    def all_available_passes(self, satellite, start_date: datetime, end_date: datetime,
                             minimum_pass_time_sec: int = 10) -> list:
        """
        Returns all availability windows between start_date and end_date where
        there are at least minimum_pass_time_sec position samples with elevation above self.minimum_elevation
        """

        delta = int((end_date - start_date).total_seconds())

        if delta < 0:
            raise ValueError("end_date cannot be before reference_date")

        if delta > utils.SECONDS_IN_DAY:
            raise ValueError("maximum allowed time delta between end_date and reference_date is 24 hours")

        current_date = start_date

        output = []

        while int((end_date - current_date).total_seconds()) > minimum_pass_time_sec:
            _, _, sat_pass = self.next_available_pass(satellite, current_date, end_date, minimum_pass_time_sec)
            if len(sat_pass) == 0:
                return output

            output.append(sat_pass)
            current_date = datetime.strptime(sat_pass[-1]['date'], utils.PYEPHEM_DATE_PATTERN)

        return output

    def next_available_passes(self, satellites, start_date: datetime, end_date: datetime,
                              minimum_pass_time_sec: int = 10) -> dict:
        """
        Returns, per satellite, all availability windows between start_date and end_date where
        there are at least minimum_pass_time_sec position samples with elevation above self.minimum_elevation
        """

        delta = int((end_date - start_date).total_seconds())

        if delta < 0:
            raise ValueError("end_date cannot be before reference_date")

        if delta > utils.SECONDS_IN_DAY:
            raise ValueError("maximum allowed time delta between end_date and reference_date is 24 hours")

        output = {}

        for satellite in satellites:
            start, stop, sat_pass = self.next_available_pass(satellite,
                                                             start_date,
                                                             end_date,
                                                             minimum_pass_time_sec)

            output[satellite.name] = {
                "start": start,
                "stop": stop,
                "coordinates": sat_pass
            }

        return output

    def next_available_passes_sequence(self, satellites: list, start_date: datetime, end_date: datetime,
                                       minimum_pass_time_sec: int = 10) -> list:

        """
        Returns, a sequence of passes to track multiple satellites one after the other.
        """

        delta = int((end_date - start_date).total_seconds())

        if delta < 0:
            raise ValueError("end_date cannot be before reference_date")

        if delta > utils.SECONDS_IN_DAY:
            raise ValueError("maximum allowed time delta between end_date and reference_date is 24 hours")

        output = []

        ref_date = start_date

        while int((end_date - ref_date).total_seconds()) > minimum_pass_time_sec \
                and len(satellites) > 0:
            earliest_sat_name = ""
            earliest_sat_index = -1
            earliest_sat_pass = []
            earliest_sat_date = end_date

            # TODO: satellites copy ?
            for i in range(len(satellites)):
                dt, _, sat_pass = self.next_available_pass(satellites[i], ref_date, end_date, minimum_pass_time_sec)
                if len(sat_pass) > 0:
                    if dt < earliest_sat_date:
                        earliest_sat_date = dt
                        earliest_sat_pass = sat_pass
                        earliest_sat_name = satellites[i].name
                        earliest_sat_index = i

            if len(earliest_sat_pass) == 0:
                return output

            output.append({
                'name': earliest_sat_name,
                'coordinates': earliest_sat_pass
            })

            del satellites[earliest_sat_index]

            ref_date = datetime.strptime(earliest_sat_pass[-1]['date'], utils.PYEPHEM_DATE_PATTERN)
            ref_date = ref_date + timedelta(seconds=self.positioning_timeout_sec)

        return output
