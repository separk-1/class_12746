#%%
import numpy as np

A = np.array([[1,2],[3,4]]) # create a square matrix
B = np.linalg.inv(A)    # use np.linalg.inv to take its inverse

print(A)
print(B)
print(np.dot(A,B)) # use np.dot to multiply the matrices to get the identity


# %%
