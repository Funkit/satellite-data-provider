import ephem
from datetime import datetime, timedelta

def GetRange(satellite_name, tle_line_1, tle_line_2, station_latitude, station_longitude, station_altitude, computation_date):
    satellite = ephem.readtle(satellite_name, tle_line_1, tle_line_2)

    city = ephem.Observer()
    city.lon, city.lat, city.elevation, city.date = station_latitude , station_longitude , station_altitude, computation_date
    satellite.compute(city)
    return satellite.az, satellite.alt, satellite.range

def GetPointingRangeList(satellite_name, tle_line_1, tle_line_2, station_latitude, station_longitude, station_altitude, date_start, date_stop):
    date_pattern = '%Y/%m/%d %H:%M:%S'

    datetime_start = datetime.strptime(date_start, date_pattern)
    datetime_stop = datetime.strptime(date_stop, date_pattern)

    number_of_entries = int((datetime_stop - datetime_start).total_seconds())
    range_list = []
    for i in range(number_of_entries):
        current_date = datetime_start + timedelta(0,i)
        current_date_string = current_date.strftime(date_pattern)

        azimuth, elevation, range_meter = GetRange(satellite_name, tle_line_1, tle_line_2, station_latitude, station_longitude, station_altitude, current_date_string)
        
        range_list.append({
            "date": current_date_string,
            "azimuth": azimuth,
            "elevation": elevation,
            "range": range_meter
        })
    
    return range_list

