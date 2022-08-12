from eph import get_pointing_range_list
import sys

print('Number of arguments:', len(sys.argv))

if len(sys.argv) != 9 :
    print("Wrong number of arguments. See README.")

satellite_name = sys.argv[1]
tle_line_1 = sys.argv[2]
tle_line_2 = sys.argv[3]
station_latitude = float(sys.argv[4])
station_longitude = float(sys.argv[5])
station_altitude = float(sys.argv[6])
date_start = sys.argv[7]
date_stop = sys.argv[8]

pointingRangeList = get_pointing_range_list(satellite_name,
                                            tle_line_1,
                                            tle_line_2,
                                            station_latitude,
                                            station_longitude,
                                            station_altitude,
                                            date_start,
                                            date_stop)

print(pointingRangeList)
