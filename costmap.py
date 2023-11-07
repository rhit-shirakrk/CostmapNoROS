"""
Generate an occupancy grid from an las/laz file with numerical values in each cell

WIP, not done
"""

import geemap
import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# #* Pick 625 random sample points (perfect squares work better for this demonstration)
# las = geemap.read_lidar('Powerline_analysis_cl.laz') # only need x,y,z 
# sample_data = sample(list(zip(las.X, las.Y, las.Z)), 625) # list of 625 tuples, where each tuple is formatted (x, y, z)
# x_data, y_data, z_data = zip(*sample_data) # unzip into a (giant) tuple of respective coordinates

#* Pick the first 625 points (perfect squares work better for this demonstration)
las = geemap.read_lidar('Powerline_analysis_cl.laz') # only need x,y,z 
x_data = las.X[:625]
y_data = las.Y[:625]
z_data = las.Z[:625]

# ! Test Sidney_fig_tree (takes a LONG time)
# las = geemap.read_lidar('Sydney_fig_tree.laz') # only need x,y,z 

# Create Pandas Dataframe from x, y, z data and split it into chunks of 25
df = pd.DataFrame({'x': x_data, 'y': y_data, 'z': z_data})
n = 25 
list_df = [df[i:i + n] for i in range(0, df.shape[0], n)] # create chunks of 25, source: https://stackoverflow.com/a/44729807

# Find the average z-value of each chunk, then assign that value to all (x,y,z) points
index = 0
for chunk in list_df: 
  avg_z_value = np.average(chunk.loc[:,'z'])
  list_df[index] = chunk.assign(z=avg_z_value)
  index += 1

df = pd.concat(list_df) # view split_and_reformed.xlsx for visual
ax = sns.heatmap(data=df, annot=True, fmt='d', cmap='RdYlGn', cbar=True, cbar_kws={'label': 'z'}, square=True) # unknown format code 'd' for object of type 'float'
ax.tick_params(labelrotation=0)
plt.show()