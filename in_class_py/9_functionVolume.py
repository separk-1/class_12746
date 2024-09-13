# %%
import math

def volume(radius):
    """This function computes the volume of a sphere given the radius.
    Remember to import the math module so that pi is defined. """

    v = (4/3)*math.pi*(radius**3)
    return v

newRadius = 5.0
newVolume = volume(newRadius)

print("\n The volume of a sphere with radius ", newRadius, "units is ", newVolume, " units cubed")


# %%
