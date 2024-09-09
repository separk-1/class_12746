# Seongeun Park / seongeup / 12-746 A1 / Homework 2-2

import math

def cartesian_to_polar(x, y):
    # calculate r: distance from (0, 0) to (x, y)
    r = math.sqrt(x**2 + y**2)
    
    # tan(theta) = y/x
    # theta = arctan(y/x)
    # math.atan2(a, b): arc tangent
    # math.degrees = radian to degree
    theta = math.degrees(math.atan2(y, x))
    
    return r, theta

# "interesting" pairs of x, y values
test_values = [
    (0, 0),   
    (0, 1),   
    (1, 1),   
    (-1, 0),   
    (-1, -1),   
    (1e-10, 1e+3)  
]

for x, y in test_values:
    r, theta = cartesian_to_polar(x, y)
    print(f"When x is {x} and y is {y}, r is {r} and theta is {theta} degrees")
