# %%
import math

class point:
    """point represents a point is 3D space in Cartesian coordinates"""

    def __init__(self, xcoord, ycoord, zcoord):
        self.x = xcoord
        self.y = ycoord
        self.z = zcoord

    def distance(self):
        """This method computes the distance of the point from the origin"""
        self.sum = math.sqrt(self.x**2+self.y**2+self.z**2)
        return self.sum

# The class definition above is just an abstraction. It becomes real when you create an instance of the
# class and execute the function. The execution of distance happens in the print statement.

p1 = point(5.0, -10.2, 6.7)    # instantiate the class point in the variable p1


# The last part of the print statement executes the method distance on the point p1
print("The distance of point [%.1f, %.1f, %.1f ] "
      "from the origin is %.2f units" % (p1.x, p1.y, p1.z, p1.distance()))

print("p1 belongs to ", type(p1))
print("It is", isinstance(p1, point), "that p1 is an instance of point")

# %%
