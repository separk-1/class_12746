# Seongeun Park, shimin xu 

import matplotlib.pyplot as plt
import numpy as np

plt.style.use('_mpl-gallery')

# make data
np.random.seed(1)
x = 4 + np.random.normal(0, 1.5, 200)

# plot:
fig, ax = plt.subplots()

ax.hist(x, bins=8, linewidth=0.5, color = 'blue', edgecolor="red")

ax.set(xlim=(0, 8), xticks=np.arange(1, 4),
       ylim=(0, 40), yticks=np.linspace(0, 56, 9))

plt.show()