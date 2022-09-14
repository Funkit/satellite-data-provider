from rpc import datetimeutils


def test_7():
    datetimeutils.test_func()
    #val = datetime_pb2.DateTime(year=2022,
    #                            month=9,
    #                            day=14,
    #                            hours=14,
    #                            minutes=42,
    #                            seconds=38)

    #val = pointing_pb2.SatMon(
    #    minimum_pass_length_sec=30,
    #    satellite_information=pointing_pb2.SatelliteInformation(
    #        name="STARLINK-24",
    #        tle_line_1="1 44238U 19029D   22229.17555387  .00106534  00000+0  22460-2 0  9994",
    #        tle_line_2="2 44238  53.0031 183.2357 0002897 123.7131 236.4150 15.44417471179240"
    #    )
    #)

    #print(val)


if __name__ == '__main__':
    test_7()
