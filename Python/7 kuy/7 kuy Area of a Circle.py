'''
Complete the function which will return the area of a circle with the given radius.

Returned value is expected to be accurate up to tolerance of 0.01.

If the radius is not positive, raise ValueError.
'''

from math import pi

def circle_area(r):
    if r <= 0:
        raise ValueError
    return pi * r ** 2