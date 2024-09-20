# Seongeun Park, shimin xu 
'''
Running the same code on macOS and Windows showed no significant differences in performance or results. 
On macOS, the interface arrows were lighter, and the icon buttons were separated, but these were just visual differences that didn’t affect functionality.
'''

import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import axes3d

plt.style.use('fivethirtyeight') # changed style 

# Make data
X, Y, Z = axes3d.get_test_data(0.05)

# Plot
fig, ax = plt.subplots(subplot_kw={"projection": "3d"})
ax.plot_wireframe(X, Y, Z, rstride=10, cstride=10, color='darkgreen') # added color

ax.set(xticklabels=[],
       yticklabels=[],
       zticklabels=[])

plt.show()