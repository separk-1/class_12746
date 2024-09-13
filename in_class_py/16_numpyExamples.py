# %%
import numpy
# import math

# Create a mathematical array using numpy

myArray = numpy.array([1, 2, 3, 4, 5, 6])
print("\n", myArray, " is a ", type(myArray), "variable")

# create a matrix by concatonating 2 arrays

myMatrix = numpy.array([[6, 5, 7],[4, 7, 9]])
squareMatrix = myMatrix**2
print('The square of \n', myMatrix, '\n is \n', squareMatrix)

# %%
# Use the numpy linalg package to compute the distance between two points

point1 = numpy.array([0,0,1])
point2 = numpy.array([1,0,1])

distance = numpy.linalg.norm(point1 - point2)
print('The distance between point1 and point2 is ', distance)
# %%
