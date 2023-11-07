"""
Generate an occupancy grid from an las/laz file and visualize depth through a continuous heat map.
"""

import geemap
from random import sample
import numpy as np
from scipy.interpolate import griddata
import matplotlib.pylab as plt
from matplotlib import cm

# #* Pick 625 random sample points (perfect squares work better for this demonstration)
# las = geemap.read_lidar('Powerline_analysis_cl.laz') # only need x,y,z 
# sample_data = sample(list(zip(las.X, las.Y, las.Z)), 625) # list of 625 tuples, where each tuple is formatted (x, y, z)
# x_data, y_data, z_data = zip(*sample_data) # unzip into a (giant) tuple of respective coordinates

# # #* Pick the first 625 points (perfect squares work better for this demonstration)
# las = geemap.read_lidar('Powerline_analysis_cl.laz') # only need x,y,z 
# x_data = las.X[:625]
# y_data = las.Y[:625]
# z_data = las.Z[:625]

#! Test Sidney_fig_tree (takes a LONG time)
las = geemap.read_lidar('Sydney_fig_tree.laz') # only need x,y,z 

# Source: https://stackoverflow.com/a/72123309
X = np.array(las.X)
Y = np.array(las.Y)
Z = np.array(las.Z)

# 2d heightmap
nx = int(len(las.Z)**.5)
xg = np.linspace(X.min(), X.max(), nx)
yg = np.linspace(Y.min(), Y.max(), nx)
xgrid, ygrid = np.meshgrid(xg, yg)
ctr_f = griddata((X, Y), Z, (xgrid, ygrid), method='linear')
fig = plt.figure()
ax = fig.add_subplot(1, 1, 1) 
con = ax.contourf(xgrid, ygrid, ctr_f, cmap=cm.seismic)
fig.colorbar(con, shrink=0.5, aspect=5)
plt.show()
# plt.savefig("heightmap_v2.png", dpi=500) save png