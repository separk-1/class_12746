# Seongeun Park, shimin xu 
'''
Running the same code on macOS and Windows showed no significant differences in performance or results. 
On macOS, the interface arrows were lighter, and the icon buttons were separated, but these were just visual differences that didn’t affect functionality.
'''

import matplotlib.pyplot as plt
import numpy as np

plt.style.use('bmh') # changed style

# make data:
np.random.seed(1)
x = np.random.uniform(-3, 3, 256)
y = np.random.uniform(-3, 3, 256)
z = (1 - x/2 + x**5 + y**3) * np.exp(-x**2 - y**2)
levels = np.linspace(z.min(), z.max(), 7)

# plot:
fig, ax = plt.subplots()

ax.plot(x, y, 'o', markersize=2, color='white') # changed marker, color
ax.tricontourf(x, y, z, levels=levels)

ax.set(xlim=(-3, 3), ylim=(-3, 3))

plt.show()


