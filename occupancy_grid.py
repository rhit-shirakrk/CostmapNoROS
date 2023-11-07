"""
Generate an occupancy grid from an las/laz file
"""

import geemap
from random import sample
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.colors import LogNorm

las = geemap.read_lidar('Powerline_analysis_cl.laz') # only need x,y,z 

#* Pick 625 random sample points (perfect squares work better for this demonstration)
sample_data = sample(list(zip(las.X, las.Y, las.Z)), 625) # list of 625 tuples, where each tuple is formatted (x, y, z)
x, y, z = zip(*sample_data) # unzip into a (giant) tuple of respective coordinates

# # #* Pick the first 625 points (perfect squares work better for this demonstration)
# las = geemap.read_lidar('Powerline_analysis_cl.laz') # only need x,y,z 
# x_data = las.X[:625]
# y_data = las.Y[:625]
# z_data = las.Z[:625]

x_data = np.array(x)
y_data = np.array(y)
z_data = np.array(z)



# Source: https://stackoverflow.com/a/39727937
N = int(len(z_data)**.5)
z = z_data.reshape(N, N)
plt.imshow(z, extent=(np.amin(x_data), np.amax(x_data), np.amin(y_data), np.amax(y_data)), norm=LogNorm(), aspect = 'auto')
plt.title("2D Height Map of 625 Random Points")
plt.colorbar()
plt.show()

"""
Possible improvements:
- Smooth colors out (similar to source)
"""