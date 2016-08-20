# This script aims at reading csv files and store the data for postprocessing in 1-D.

#### import python modules ####
import sys, os, math, csv, itertools
import numpy as np
import itertools as it
import matplotlib.pyplot as plt
from decimal import *
#### import python modules ####

#### define function ####
def plot_solution(x_num, y_num, label, xposition, yposition, init_value, legend_plot):
  marker_list = itertools.cycle(('x', '+', '.', '|', '2', '3', '4', 'o'))
  x_min, x_max = 1e10, 0.0
  for i in xrange(0, len(x_num)):
    nb_cells = len(x_num[i])-1
    plt.plot(x_num[i], y_num[i], '-', markevery=nb_cells/10, markersize=8, label=r'$transient \ pressure \ %s$ ' % str(legend_plot[i]), linewidth=2, marker=marker_list.next())
    x_min = min(float(min(x_num[i])), x_min)
    x_max = max(float(max(x_num[i])), x_max)

  plt.axhline(y=init_value, color='k', linewidth=2, label=r'$initial \ pressure$', marker=marker_list.next())
  plt.xlabel(r'$t \ (s)$', fontsize=20)
  plt.ylabel(r'$%s$' % label, fontsize=20)
#  plt.ylim(float(min(y_num)), float(max(y_num)))
  plt.margins(0.1, 0.1)
  for xc in xposition:
    plt.axvline(x=xc, color='k', linestyle='--')
  for yc in yposition:
    plt.axhline(y=yc, color='k', linestyle='--')
  plt.annotate ('', (xposition[0]/4, yposition[0]), (xposition[0]/4, yposition[1]), arrowprops={'arrowstyle':'<->'})
  plt.text(xposition[0]/4, init_value, r'$\Delta P = %d \ Pa$' % (yposition[1]-yposition[0]), fontsize=20)
  plt.annotate ('', (xposition[0], init_value*0.95), (xposition[1], init_value*0.95), arrowprops={'arrowstyle':'<->'})
  plt.text((xposition[0]+xposition[1])/2.2, init_value*0.96, r'$\Delta t = %s \ s$' % str(xposition[0]), fontsize=20)
  plt.legend(loc='upper center', fontsize=20, frameon=False, bbox_to_anchor=(0.5, 1.+0.1*(len(x_num)+0.5)), borderaxespad=0.)
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
for input in xrange(1, len(sys.argv)-1):
  file_list.append(sys.argv[input])

#file_list.append('cathare-code.3.eqn_pps_csv_out.csv')
#file_list.append('cathare-code.3.eqn_pps_csv_out.csv')

# OUTPUT SOME INFORMATION
print '------------------------------'
print 'Index of variables in each file:', var_index

# VARIABLES TO STORE DATA
variable = []
time_x = []
nb_pts = []
legend_plot = []
out_file = sys.argv[-1]

# LOOP OVER FILES TO COMPUTE L2 and L1 norms
for file in file_list:
  print '------------------------------'
  print 'Name of the input file:', file
  # set/reset data
  variable_tmp = []
  time_x_tmp = []
  # open file and read first line
  file_data=open(file, 'r')
  line_head = file_data.readline()
  print 'Variables in file', file,':', line_head[:-1]
  # read remaining of the file and store data
  for line in file_data:
    row = line.split(',')
    time_x_tmp.append(row[var_index[0]])
    variable_tmp.append(row[var_index[1]])
  
  variable.append(variable_tmp)
  time_x.append(time_x_tmp)
  nb_pts.append(len(time_x)-1)

  print'Number of time points in file', file, ':', nb_pts[-1]
  file_data.close()

# legend 1
#legend_plot.append('36 \ cells')
#legend_plot.append('72 \ cells')
#legend_plot.append('144 \ cells')

# legend 2
legend_plot.append('cfl \ 0.1')
legend_plot.append('cfl \ 0.2')
legend_plot.append('cfl \ 0.4')
legend_plot.append('cfl \ 0.8')

plot_solution(time_x, variable, 'P \ (Pa)', [0.1125, 2*0.1125], [3.e6-302633.1504, 3e6+302633.1504], 3.e6, legend_plot)