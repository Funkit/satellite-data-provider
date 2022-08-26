import ephem
from datetime import datetime, timedelta
from eph import groundstation, schedule


def test_1():
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


def test_2():
    satellite = ephem.readtle("STARLINK-24",
                              "1 44238U 19029D   22228.14008782  .00099335  00000+0  21125-2 0  9999",
                              "2 44238  53.0033 188.1678 0002676 113.9454 246.1831 15.44197523179085")

    station = groundstation.Station(name="Toulouse",
                                    latitude=43.604652,
                                    longitude=1.444209,
                                    altitude=146,
                                    positioning_timeout_sec=35)

    pos = station.next_available_pass(satellite, datetime.now(), datetime.now() + timedelta(hours=24), 100)

    for item in pos:
        print(item)


def test_3():
    satellite1 = ephem.readtle("STARLINK-24",
                               "1 44238U 19029D   22229.17555387  .00106534  00000+0  22460-2 0  9994",
                               "2 44238  53.0031 183.2357 0002897 123.7131 236.4150 15.44417471179240")
    satellite2 = ephem.readtle("STARLINK-71",
                               "1 44252U 19029T   22229.15356155  .00092076  00000+0  18178-2 0  9996",
                               "2 44252  52.9924 177.9864 0003905 111.8634 248.2787 15.46410461179314")
    satellite3 = ephem.readtle("STARLINK-1007",
                               "1 44713U 19074A   22228.79595905  .00001502  00000+0  11967-3 0  9999",
                               "2 44713  53.0557 266.5525 0001331  77.7034 282.4104 15.06400880152677")

    sat_list = [satellite1, satellite2, satellite3]

    station = groundstation.Station(name="Toulouse",
                                    latitude=43.604652,
                                    longitude=1.444209,
                                    altitude=146)

    passes = station.next_available_passes(sat_list, datetime.now(), datetime.now() + timedelta(hours=24), 100)

    for item in passes:
        print(item)
        print(passes[item])


def test_4():
    satellite1 = ephem.readtle("STARLINK-24",
                               "1 44238U 19029D   22229.17555387  .00106534  00000+0  22460-2 0  9994",
                               "2 44238  53.0031 183.2357 0002897 123.7131 236.4150 15.44417471179240")
    satellite2 = ephem.readtle("STARLINK-71",
                               "1 44252U 19029T   22229.15356155  .00092076  00000+0  18178-2 0  9996",
                               "2 44252  52.9924 177.9864 0003905 111.8634 248.2787 15.46410461179314")
    satellite3 = ephem.readtle("STARLINK-1007",
                               "1 44713U 19074A   22228.79595905  .00001502  00000+0  11967-3 0  9999",
                               "2 44713  53.0557 266.5525 0001331  77.7034 282.4104 15.06400880152677")

    sat_list = [satellite1, satellite2, satellite3]

    station = groundstation.Station(name="Toulouse",
                                    latitude=43.604652,
                                    longitude=1.444209,
                                    altitude=146)

    passes = station.next_available_passes_sequence(sat_list, datetime.now(), datetime.now() + timedelta(hours=4), 100)

    for item in passes:
        print(item)


def test_5():
    sat_list = [
        ephem.readtle("STARLINK-24",
                              "1 44238U 19029D   22229.17555387  .00106534  00000+0  22460-2 0  9994",
                              "2 44238  53.0031 183.2357 0002897 123.7131 236.4150 15.44417471179240"),
        ephem.readtle("STARLINK-71",
                      "1 44252U 19029T   22229.15356155  .00092076  00000+0  18178-2 0  9996",
                      "2 44252  52.9924 177.9864 0003905 111.8634 248.2787 15.46410461179314"),
        ephem.readtle("STARLINK-1007",
                      "1 44713U 19074A   22228.79595905  .00001502  00000+0  11967-3 0  9999",
                      "2 44713  53.0557 266.5525 0001331  77.7034 282.4104 15.06400880152677")
    ]

    station_list = [
        groundstation.Station(name="Toulouse",
                              latitude=43.604652,
                              longitude=1.444209,
                              altitude=146,
                              positioning_timeout_sec=100),
        groundstation.Station(name="Tokyo",
                              latitude=35.652832,
                              longitude=139.839478,
                              altitude=37.153,
                              positioning_timeout_sec=100)
    ]

    passes = schedule.get_schedule(station_list, sat_list, datetime.now(), datetime.now() + timedelta(hours=4), 100)

    for item in passes:
        print(item)


def test_6():
    sat = ephem.readtle("STARLINK-24",
                          "1 44238U 19029D   22229.17555387  .00106534  00000+0  22460-2 0  9994",
                          "2 44238  53.0031 183.2357 0002897 123.7131 236.4150 15.44417471179240")

    station_list = [
        groundstation.Station(name="Toulouse",
                              latitude=43.604652,
                              longitude=1.444209,
                              altitude=146,
                              positioning_timeout_sec=100),
        groundstation.Station(name="Tokyo",
                              latitude=35.652832,
                              longitude=139.839478,
                              altitude=37.153,
                              positioning_timeout_sec=100)
    ]

    sat_pass = schedule.get_next_pass(sat, station_list, datetime.now(), datetime.now() + timedelta(hours=4), 100)

    print(sat_pass)


if __name__ == '__main__':
    test_2()
