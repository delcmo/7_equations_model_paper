# This script aims at reading csv files and store the data for postprocessing in 1-D.

#### import python modules ####
import sys, os, math, csv
import numpy as np
import itertools as it
import matplotlib.pyplot as plt
from decimal import *
#### import python modules ####

#### define function ####
def plot_solution(x_num, y_num, label, xposition, yposition, init_value):
  plt.plot(x_num, y_num, '+-', markevery=30, markersize=8, label=r'$transient \ pressure$', linewidth=2)
  plt.axhline(y=init_value, color='r', linewidth=2, label=r'$initial \ pressure$')
  plt.xlabel(r'$t \ (s)$', fontsize=20)
  plt.ylabel(r'$%s$' % label, fontsize=20)
#  plt.ylim(float(min(y_num)), float(max(y_num)))
  plt.xlim(float(min(x_num)), float(max(x_num)))
  plt.margins(0.1, 0.1)
  for xc in xposition:
    plt.axvline(x=xc, color='k', linestyle='--')
  for yc in yposition:
    plt.axhline(y=yc, color='k', linestyle='--')
  plt.annotate ('', (xposition[0]/4, yposition[0]), (xposition[0]/4, yposition[1]), arrowprops={'arrowstyle':'<->'})
  plt.text(xposition[0]/4, init_value, r'$\Delta P = %d \ Pa$' % (yposition[1]-yposition[0]), fontsize=20)
  plt.annotate ('', (xposition[0], init_value*0.95), (xposition[1], init_value*0.95), arrowprops={'arrowstyle':'<->'})
  plt.text((xposition[0]+xposition[1])/2.2, init_value*0.96, r'$\Delta t = %s \ s$' % str(xposition[0]), fontsize=20)
  plt.legend(loc=(0.4,0.8), fontsize=20, frameon=False)
  fig_name=out_file+'-nel-plot.eps'
  plt.savefig(fig_name, bbox_inches='tight')
  print 'Saving plot using Matplotlib:', fig_name
  plt.clf()

#### end define function ####

# SET SOME VARIABLES
dir_path = os.getcwd()
var_index = [1, 3] # [pressure, density, temperature, velocity, x, visc max, kappa, mu]
var_index[:] = [i -1 for i in var_index] # convert to python index

file_list = []
file_list.append('cathare-code.3.eqn_pps_csv_out.csv')

# OUTPUT SOME INFORMATION
print '------------------------------'
print 'Index of variables in each file:', var_index

# VARIABLES TO STORE DATA
variable = []
time_x = []
nb_pts = []

# LOOP OVER FILES TO COMPUTE L2 and L1 norms
for file in file_list:
  print '------------------------------'
  print 'Name of the input file:', file
  # set/reset data
  out_file = file[:-6]
  variable[:] = []
  time_x[:] = []
  # open file and read first line
  file_data=open(file, 'r')
  line_head = file_data.readline()
  print 'Variables in file', file,':', line_head[:-1]
  # read remaining of the file and store data
  for line in file_data:
    row = line.split(',')
    time_x.append(row[var_index[0]])
    variable.append(row[var_index[1]])

  nb_pts.append(len(time_x)-1)
  print'Number of time points in file', file, ':', nb_pts[-1]

  plot_solution(time_x, variable, 'P \ (Pa)', [0.1125, 2*0.1125], [3.e6-302633.1504, 3e6+302633.1504], 3.e6)

  file_data.close()