import ephem
import json
import os
from datetime import datetime
from eph import groundstation, schedule


def default(o):
    if isinstance(o, datetime):
        return o.isoformat()


def test_schedule_get_next_pass():
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

    got = schedule.get_next_pass(sat,
                                 station_list,
                                 datetime.strptime("2022/09/08 12:00:00", "%Y/%m/%d %H:%M:%S"),
                                 datetime.strptime("2022/09/09 12:00:00", "%Y/%m/%d %H:%M:%S"),
                                 30)

    got_str = json.dumps(got, indent=4, default=default)

    dirname = os.path.dirname(__file__)
    filename = os.path.join(dirname, '../../samples/schedule_next_pass.json')
    with open(filename, 'r') as data_file:
        want_raw = data_file.read()

    want = json.loads(want_raw)
    want_str = json.dumps(want, indent=4, default=default)

    assert got_str == want_str


def test_schedule_get_schedule():
    sat_list = [
        {
            "info": ephem.readtle("STARLINK-24",
                                  "1 44238U 19029D   22229.17555387  .00106534  00000+0  22460-2 0  9994",
                                  "2 44238  53.0031 183.2357 0002897 123.7131 236.4150 15.44417471179240"),
            "minimum_pass_length": 30
        },
        {
            "info": ephem.readtle("STARLINK-71",
                                  "1 44252U 19029T   22229.15356155  .00092076  00000+0  18178-2 0  9996",
                                  "2 44252  52.9924 177.9864 0003905 111.8634 248.2787 15.46410461179314"),
            "minimum_pass_length": 30
        },
        {
            "info": ephem.readtle("STARLINK-1007",
                                  "1 44713U 19074A   22228.79595905  .00001502  00000+0  11967-3 0  9999",
                                  "2 44713  53.0557 266.5525 0001331  77.7034 282.4104 15.06400880152677"),
            "minimum_pass_length": 30
        }
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

    got = schedule.get_schedule(sat_list,
                                station_list,
                                datetime.strptime("2022/09/08 12:00:00", "%Y/%m/%d %H:%M:%S"),
                                datetime.strptime("2022/09/09 12:00:00", "%Y/%m/%d %H:%M:%S"))

    got_str = json.dumps(got, indent=4, default=default)

    dirname = os.path.dirname(__file__)
    filename = os.path.join(dirname, '../../samples/schedule_get_schedule.json')
    with open(filename, 'r') as data_file:
        want_raw = data_file.read()

    want = json.loads(want_raw)
    want_str = json.dumps(want, indent=4, default=default)

    assert got_str == want_str


if __name__ == '__main__':
    test_schedule_get_schedule()
