import ephem
import json
import os
from datetime import datetime
from eph import groundstation


def default(o):
    if isinstance(o, datetime):
        return o.isoformat()


def test_next_pass():
    satellite = ephem.readtle("STARLINK-24",
                              "1 44238U 19029D   22228.14008782  .00099335  00000+0  21125-2 0  9999",
                              "2 44238  53.0033 188.1678 0002676 113.9454 246.1831 15.44197523179085")

    station = groundstation.Station(name="Toulouse",
                                    latitude=43.604652,
                                    longitude=1.444209,
                                    altitude=146,
                                    positioning_timeout_sec=35)

    _, _, got = station.next_pass(satellite, datetime.strptime("2022/09/08 12:00:00", "%Y/%m/%d %H:%M:%S"))
    got_str = json.dumps(got, indent=4, default=default)

    dirname = os.path.dirname(__file__)
    filename = os.path.join(dirname, '../../samples/next_pass.json')
    with open(filename, 'r') as data_file:
        want_raw = data_file.read()

    want = json.loads(want_raw)
    want_str = json.dumps(want, indent=4, default=default)

    assert got_str == want_str


def test_next_available_pass():
    satellite = ephem.readtle("STARLINK-24",
                              "1 44238U 19029D   22228.14008782  .00099335  00000+0  21125-2 0  9999",
                              "2 44238  53.0033 188.1678 0002676 113.9454 246.1831 15.44197523179085")

    station = groundstation.Station(name="Toulouse",
                                    latitude=43.604652,
                                    longitude=1.444209,
                                    altitude=146,
                                    positioning_timeout_sec=35)

    start, stop, got = station.next_available_pass(satellite,
                                                   datetime.strptime("2022/09/08 12:00:00", "%Y/%m/%d %H:%M:%S"),
                                                   datetime.strptime("2022/09/09 12:00:00", "%Y/%m/%d %H:%M:%S"),
                                                   30)

    got_str = json.dumps(got, indent=4, default=default)

    dirname = os.path.dirname(__file__)
    filename = os.path.join(dirname, '../../samples/next_available_pass.json')
    with open(filename, 'r') as data_file:
        want_raw = data_file.read()

    want = json.loads(want_raw)
    want_str = json.dumps(want, indent=4, default=default)

    assert got_str == want_str and \
           start == datetime.strptime("2022/09/08 12:00:39", "%Y/%m/%d %H:%M:%S") and \
           stop == datetime.strptime("2022/09/08 12:07:17", "%Y/%m/%d %H:%M:%S")


def test_all_available_pass():
    satellite = ephem.readtle("STARLINK-24",
                              "1 44238U 19029D   22228.14008782  .00099335  00000+0  21125-2 0  9999",
                              "2 44238  53.0033 188.1678 0002676 113.9454 246.1831 15.44197523179085")

    station = groundstation.Station(name="Toulouse",
                                    latitude=43.604652,
                                    longitude=1.444209,
                                    altitude=146,
                                    positioning_timeout_sec=35)

    got = station.all_available_passes(satellite,
                                       datetime.strptime("2022/09/08 12:00:00", "%Y/%m/%d %H:%M:%S"),
                                       datetime.strptime("2022/09/09 12:00:00", "%Y/%m/%d %H:%M:%S"),
                                       30)

    got_str = json.dumps(got, indent=4, default=default)

    dirname = os.path.dirname(__file__)
    filename = os.path.join(dirname, '../../samples/all_available_passes.json')
    with open(filename, 'r') as data_file:
        want_raw = data_file.read()

    want = json.loads(want_raw)
    want_str = json.dumps(want, indent=4, default=default)

    assert got_str == want_str


def test_next_available_passes():
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

    got = station.next_available_passes(sat_list,
                                        datetime.strptime("2022/09/08 12:00:00", "%Y/%m/%d %H:%M:%S"),
                                        datetime.strptime("2022/09/09 12:00:00", "%Y/%m/%d %H:%M:%S"),
                                        30)

    got_str = json.dumps(got, indent=4, default=default)

    dirname = os.path.dirname(__file__)
    filename = os.path.join(dirname, '../../samples/next_available_passes.json')

    with open(filename, 'r') as data_file:
        want_raw = data_file.read()

    want = json.loads(want_raw)
    want_str = json.dumps(want, indent=4, default=default)

    assert got_str == want_str


def test_next_available_passes_sequence():
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

    got = station.next_available_passes_sequence(sat_list,
                                                 datetime.strptime("2022/09/08 12:00:00", "%Y/%m/%d %H:%M:%S"),
                                                 datetime.strptime("2022/09/09 12:00:00", "%Y/%m/%d %H:%M:%S"),
                                                 30)

    got_str = json.dumps(got, indent=4, default=default)

    dirname = os.path.dirname(__file__)
    filename = os.path.join(dirname, '../../samples/next_available_passes_sequence.json')

    with open(filename, 'r') as data_file:
        want_raw = data_file.read()

    want = json.loads(want_raw)
    want_str = json.dumps(want, indent=4, default=default)

    assert got_str == want_str
