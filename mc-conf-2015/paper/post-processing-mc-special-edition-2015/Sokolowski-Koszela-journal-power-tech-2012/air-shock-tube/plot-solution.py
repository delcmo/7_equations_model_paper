# This script aims at reading csv files and store the data for postprocessing in 1-D.

#### import python modules ####
import sys, os, math, csv
import numpy as np
import itertools as it
import matplotlib.pyplot as plt
from decimal import *
#### import python modules ####

#### define function ####
def plot_solution(x_num, y_num, x_anal, y_anal, x_label, y_label, label, nb_cells):
  plt.plot(x_num, y_num, '+-', markevery=30, markersize=8, label=r'$numerical \ solution$', linewidth=2.2)
#  plt.plot(x_anal, y_anal, 'o-', markevery=30, markersize=8, label=r'$exact \ solution$', linewidth=1.2)
#  plt.legend(loc='best', fontsize=20, frameon=False)
  plt.xlabel('%s' % x_label, fontsize=25)
  plt.ylabel('%s' % y_label, fontsize=25)
#  plt.ylim(float(min(y_num)), float(max(y_num)))
  plt.xlim(float(min(x_num)), float(max(x_num)))
  if float(min(y_num)) > 1e4:
    plt.ticklabel_format(style='sci', axis='y', scilimits=(0,0))
  plt.margins(0.1, 0.1)
  fig_name=out_file+'-'+label+'-nel-'+str(nb_cells)+'-plot.eps'
  plt.savefig(fig_name, bbox_inches='tight')
  print 'Saving plot using Matplotlib:', fig_name
  plt.clf()

def plot_visc_coeff(x_num, file, var_index, nb_cells):
  # open file and read first line
  visc_e = []
  visc_max = []
  file_data=open(file, 'r')
  line_head = file_data.readline()
  for line in file_data:
    row = line.split(',')
    visc_e.append(row[var_index[5]])
    visc_max.append(row[var_index[6]])
  x_num = [float(x) for x in x_num[:-1]]
  plt.plot(x_num, visc_max, '+-', markevery=30, markersize=8, label=r'$\kappa_{max}$', linewidth=2.2)
  plt.plot(x_num, visc_e, 'o-', markevery=30, markersize=8, label=r'$\kappa_e$', linewidth=2.2)
  plt.legend(loc='best', fontsize=25, frameon=False)
  plt.xlabel(r'$x$', fontsize=25)
  plt.ylabel(r'$\kappa$', fontsize=25)
  plt.ticklabel_format(style='sci', axis='y', scilimits=(0,0))
  plt.xlim(float(min(x_num)), float(max(x_num)))
  plt.margins(0.1, 0.1)
  fig_name=out_file+'-visc-nel-'+str(nb_cells)+'-plot.eps'
  plt.savefig(fig_name)
  print 'Saving plot using Matplotlib:', fig_name
  plt.clf()
#### define function ####

# READ EXACT SOLUTION
#file_exact_list = []
#path_to_exact_files = 'test'
## x-coordinates
#file_exact_list.append('x_data.txt')
#x_coord_exact = []
#file_data_exact=open(file_exact_list[-1], 'r')
#x_coord_exact[:] = [ line[:-1] for line in file_data_exact]
## material density
#file_exact_list.append('Density_data.txt')
#mat_density_exact = []
#file_data_exact=open(file_exact_list[-1], 'r')
#mat_density_exact[:] = [ line[:-1] for line in file_data_exact]
## radiation energy density
#file_exact_list.append('Er_data.txt')
#radiation_exact = []
#file_data_exact=open(file_exact_list[-1], 'r')
#radiation_exact[:] = [ line[:-1] for line in file_data_exact]
## mach number or fluid velocity
#file_exact_list.append('Mach_Data.txt')
#mach_nb_exact = []
#file_data_exact=open(file_exact_list[-1], 'r')
#mach_nb_exact[:] = [ line[:-1] for line in file_data_exact]
## material temperature
#file_exact_list.append('Tm_data.txt')
#mat_temp_exact = []
#file_data_exact=open(file_exact_list[-1], 'r')
#mat_temp_exact[:] = [ line[:-1] for line in file_data_exact]
#nb_nodes_exact = len(x_coord_exact)
#nb_exact_files = len(file_exact_list)

# SET SOME VARIABLES
dir_path = os.getcwd()
#nb_files = len(file_list)
var_index = [10, 11, 20, 21, 24, 9, 11] # [pressure, density, temperature, velocity, x, visc max, kappa, mu]
var_index[:] = [i -1 for i in var_index] # convert to python index

file_list = []
#file_list.append('air-shock-tube-pts.csv')
file_list.append(sys.argv[1])

# OUTPUT SOME INFORMATION
print '------------------------------'
#print 'Number of files with exact solution to read:', nb_exact_files
#print 'Number of nodes in exact solution:', nb_nodes_exact
#print 'Number of files to read:', nb_files
print 'Index of variables in each file:', var_index

# VARIABLES TO STORE DATA
nb_cells = []
x_offset = []

pressure = []
density = []
temperature = []
velocity = []
x_coord = []

# LOOP OVER FILES TO COMPUTE L2 and L1 norms
for file in file_list:
  print '------------------------------'
  print 'Name of the input file:', file
  # set/reset data
  out_file = file[:-5]
  pressure[:] = []
  density[:] = []
  temperature[:] = []
  velocity[:] = []
  x_coord[:] = []
  # open file and read first line
  file_data=open(file, 'r')
  line_head = file_data.readline()
  print 'Variables in file', file,':', line_head[:-1]
  # read remaining of the file and store data
  for line in file_data:
    row = line.split(',')
    pressure.append(row[var_index[0]])
    density.append(row[var_index[1]])
    temperature.append(row[var_index[2]])
    velocity.append(row[var_index[3]])
    x_coord.append(row[var_index[4]])
  
  nb_cells.append(len(x_coord)-1)
  print'Number of cells in file', file, ':', nb_cells[-1]

  plot_solution(x_coord, density, x_coord, density, r'$x \ (m)$', r'$\rho \ (kg/m^3)$', 'density', nb_cells[-1])
  plot_solution(x_coord, pressure, x_coord, pressure, r'$x \ (m)$', r'$P \ (Pa)$', 'pressure', nb_cells[-1])
  plot_solution(x_coord, velocity, x_coord, velocity, r'$x \ (m)$', r'$u \ (m/s)$', 'velocity', nb_cells[-1])
  plot_solution(x_coord, temperature, x_coord, temperature, r'$x \ (m)$', '$T \ (K)$', 'temperature', nb_cells[-1])

  plot_visc_coeff(x_coord, 'air-shock-tube-cells0.csv', var_index, nb_cells[-1])

  file_data.close()

#def plot_error_norms(nb_cells, L1_norm, L2_norm, variable):
#  nb_cells_log = [math.log(x) for x in nb_cells]
#  L1_norm_log = [math.log(x) for x in L1_norm]
##  L2_norm_log= [math.log(x) for x in L2_norm]
#  plt.plot(nb_cells_log, L1_norm_log, '+-', label=r'$L_1^{error} norm$')
#  x1 = [math.log(nb_cells[0]), math.log(nb_cells[-1])]
#  y1 = [-math.log(nb_cells[0])+math.log(L1_norm[-1])+math.log(nb_cells[-1]), math.log(L1_norm[-1])]
#  plt.plot(x1, y1, '-', label=r'$line \ of  \ slope \ 1$')
##  plt.plot(nb_cells_log, L2_norm_log, 'o-', label=r'$L_2^{error} norm$')
##  y2 = [-math.log(nb_cells[0])+math.log(L2_norm[-1])+math.log(nb_cells[-1]), math.log(L2_norm[-1])]
##  plt.plot(x1, y2, '-', label=r'$line \ of  \ slope \ 2$')
#  plt.legend(loc='best', fontsize=20, frameon=False)
#  plt.xlabel(r'$\log (cells)$', fontsize=20)
#  if variable=='density':
#    y_label=r'$\rho$'
#  elif variable=='mat-temp':
#    y_label=r'$T$'
#  elif variable=='radiation':
#    y_label=r'$T_r$'
#  elif variable=='mach-number':
#    y_label=r'$Mach$'
#  else:
#    print 'ERROR: unvalid variable name'
#    sys.exit()
#  plt.ylabel(r'$\log (L_{1,2}^{error}($'+y_label+'$))$', fontsize=20)
#  fig_name=out_file+'-'+variable+'-convergence.eps'
#  plt.savefig(fig_name)
#  plt.clf()