#%%
# This program demonstrates the initial concepts for Object Oriented Programming

class point:
     '''point represents a point is 3D space in Cartesian coordinates'''
     def __init__(self, xcoord,ycoord,zcoord):
            self.x = xcoord
            self.y = ycoord
            self.z = zcoord

# Create an instance of the class Point
# Assign values to the attributes of the instance through the argument list

p1 = point(5.0, -10.2, 6.7) 

print("\nThe point is [", p1.x, p1.y, p1.z, "]")

# %%
