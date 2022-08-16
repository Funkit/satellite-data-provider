import ephem
from datetime import datetime

satellite_name = "STARLINK-24             "
tle_line_1 = "1 44238U 19029D   22228.14008782  .00099335  00000+0  21125-2 0  9999"
tle_line_2 = "2 44238  53.0033 188.1678 0002676 113.9454 246.1831 15.44197523179085"
station_latitude = 43.604652
station_longitude = 1.444209
station_altitude = 146

satellite = ephem.readtle(satellite_name, tle_line_1, tle_line_2)

city = ephem.Observer()
city.lon = station_longitude
city.lat = station_latitude
city.elevation = station_altitude

current_time = datetime.now()
city.date = current_time

output = city.next_pass(body=satellite, singlepass=True)

if len(output) == 6:
    for i in range(0, 6, 2):
        print(output[i])
