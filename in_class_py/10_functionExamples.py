"""This program illustrates functions with data types of real, integer, Boolean
and string data types. It also illustrates functions with multiple arguments as
well as one function calling another function"""

# %%
import math


def isDivisible(x, y):
    """This Boolean function has two return statements, but only one of them will be
    reached when the function is executed"""
    if x % y == 0:
        return True
    else:
        return False


def radiusGivenVolume(v):
    """This real function returns the radius of a circle given its volume"""
    r = ((3*v)/(4*math.pi))**(1/3)
    return r


def nearestDiameter(r):
    """This integer function returns the nearest integer diameter given the radius."""
    d = 2*r
    return round(d)


def successful(v, divisor):
    """This str function returns a character string"""
    r = radiusGivenVolume(v)
    d = nearestDiameter(r)
    if isDivisible(d, divisor):
        return "Yes"
    else:
        return "No"


volume = 500.0
radius = radiusGivenVolume(volume)
diameter = nearestDiameter(radius)
print(successful(volume, 3))

# %%
