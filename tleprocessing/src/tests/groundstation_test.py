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

    start, stop, got = station.next_pass(satellite, datetime.strptime("2022/09/08 12:00:00", "%Y/%m/%d %H:%M:%S"))
    got_str = json.dumps(got, indent=4, default=default)

    dirname = os.path.dirname(__file__)
    filename = os.path.join(dirname, '..\\..\\samples\\next_pass.json')
    with open(filename, 'r') as data_file:
        want_raw = data_file.read()

    want = json.loads(want_raw)
    want_str = json.dumps(want, indent=4, default=default)

    assert got_str == want_str


if __name__ == '__main__':
    test_next_pass()
