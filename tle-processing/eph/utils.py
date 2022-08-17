import math
from ephem import Angle

PYEPHEM_DATE_PATTERN = '%Y/%m/%d %H:%M:%S'


def radians_to_degrees(angle: Angle):
    return angle/math.pi*180