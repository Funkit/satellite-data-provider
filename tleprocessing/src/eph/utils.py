import math
from ephem import Angle

PYEPHEM_DATE_PATTERN = '%Y/%m/%d %H:%M:%S'
SECONDS_IN_DAY = 86400


def radians_to_degrees(angle: Angle):
    return angle/math.pi*180
