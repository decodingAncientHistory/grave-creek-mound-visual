#!/usr/bin/python3
import os
import sys
# pip3 install laspy
# pip3 install "laspy[laszip]"
import laspy
import numpy as np
import matplotlib.pyplot as plt
import warnings

from lidar import lidar
from matplotlib.pylab import *

THIS_SCRIPT = sys.argv[0]
USAGE = f'$ python3 {THIS_SCRIPT} <lidar_filename*.laz>'
warnings.filterwarnings('ignore')

def usage(error_msg: str) -> None:
  print(f'Unable to run script. Error is: {error_msg}')
  print(USAGE)
  sys.exit(1)

def visualize_mound(x, y, z, outname):
  '''
  Take in 3 NumPy arrays for x, y, and z coordinates for points.
  Create a PNG showing the surface in 3D.

  Args:
    x (numpy.ndarray): x coordinates
    y (numpy.ndarray): y coordinates
    z (numpy.ndarray): z coordinates
    outname (str): output PNG name.
  '''
  fig = plt.figure()
  ax = fig.add_subplot(111, projection = '3d')

  surf = ax.plot_trisurf(
          x, y, z, cmap = plt.cm.terrain, linewidth = 0, 
          antialiased = True, shade = False) 
  ax.set_xlabel('longitude', fontsize = 4)
  ax.set_ylabel('latitude', fontsize = 4)
  ax.set_zlabel('height, Z', fontsize = 8)
  ax.tick_params(axis = 'both', which = 'major', labelsize = 4)

  fig.colorbar(surf)
  plt.savefig(outname, dpi = 200)
  plt.close()

def main():

  # get input filename (.laz file) that contains
  # lidar data
  # -------------------------------------------
  try:
    laz_filename = sys.argv[1]
  except Exception as e:
    usage(str(e))

  # make sure input file is lidar (.laz)
  # ------------------------------------
  if not laz_filename.lower().endswith('.laz'):
    usage('Input filename should be .laz file.')
  elif not os.path.isfile(laz_filename):
    usage(f'Not a file: {laz_filename}')

  lidar_ob = lidar(laz_filename)
  (lons_lats, z) = lidar_ob.xyz_to_wgs84()

  # define bounding box around the mound in Moundsville, WV
  # -------------------------------------------------------
  left, bottom, right, top = -80.745140, 39.916365, -80.744137, 39.917044 
  bbox_indices = lidar.filter_lng_lats_to_bbox(
          lons_lats, [left, bottom, right, top])
  
  # get only those points centered around the mound
  # -----------------------------------------------
  X, Y = lons_lats[:, 0], lons_lats[:, 1]
  X = X[bbox_indices]
  Y = Y[bbox_indices]
  z = z[bbox_indices]
  visualize_mound(X, Y, z, 'out.png')

if __name__ == '__main__':
  main()
