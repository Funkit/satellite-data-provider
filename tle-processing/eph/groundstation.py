import ephem

from datetime import datetime, timedelta
PYEPHEM_DATE_PATTERN = '%Y/%m/%d %H:%M:%S'


class Station(object):
    def __init__(self, latitude: float, longitude: float, altitude: float,
                 minimum_elevation: float = 0, positioning_timeout_sec: int = 0):
        self.obs = ephem.Observer()
        self.obs.lat = latitude
        self.obs.lon = longitude
        self.obs.elevation = altitude
        self.minimum_elevation = minimum_elevation
        self.positioning_timeout_sec = positioning_timeout_sec

    def next_pass(self, satellite, reference_date: datetime):
        output = []

        self.obs.date = reference_date
        satellite_pass = self.obs.next_pass(satellite)

        max_altitude = satellite_pass[3]
        if max_altitude > self.minimum_elevation:
            # TODO: satellite copy ?
            start_date = satellite_pass[0].datetime()
            stop_date = satellite_pass[4].datetime()

            delta = int((stop_date - start_date).total_seconds())

            for x in range(0, delta):
                current_date = start_date + timedelta(0, x)
                current_date_string = current_date.strftime(PYEPHEM_DATE_PATTERN)
                self.obs.date = current_date_string
                satellite.compute(self.obs)
                if satellite.alt > self.minimum_elevation:
                    output.append({
                        "date": current_date_string,
                        "azimuth": satellite.az,
                        "elevation": satellite.alt,
                        "range": satellite.range
                    })

        return output
