# This script aims at reading csv files and store the data for postprocessing in 1-D.

#### import python modules ####
import sys, os, math, csv, itertools
import numpy as np
import itertools as it
import matplotlib.pyplot as plt
from decimal import *
#### import python modules ####

#### define function ####
def plot_solution(x_num, y_num, x_label, y_label, label, legend_plot):
  marker_list = itertools.cycle(('x', '+', '.', 'o', '*'))
  x_min, x_max, y_min, y_max = 1.e10, 0.0, 1.e10, 0.0
  for i in xrange(0, len(x_num)):
    nb_cells = len(x_num[i])-1
    plt.plot(x_num[i], y_num[i], '-', marker=marker_list.next(), markevery=nb_cells/(10+i), markersize=10, label=r'$%s$' % str(legend_plot[i]), linewidth=2.2)
    x_min = min(float(min(x_num[i])), x_min)
    x_max = max(float(max(x_num[i])), x_max)
    y_min = min(float(min(y_num[i])), y_min)
    y_max = max(float(max(y_num[i])), y_max)
  plt.legend(loc='best', fontsize=20, frameon=False)
  plt.xlabel('%s' % x_label, fontsize=25)
  plt.ylabel('%s' % y_label, fontsize=25)
#  plt.ylim(float(y_min), float(y_max)) # conflict with plt.margins(0.1, 0.1)
  plt.xlim(float(x_min), float(x_max))
  if float(y_max) > 1e4:
    print '    Use scientific notation for y-axis'
    plt.ticklabel_format(style='sci', axis='y', scilimits=(0,0))
  plt.margins(0.1, 0.1)
  fig_name=out_file+'-'+label+'-plot.eps'
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
var_index = [1,2,3,4,5]
var_index[:] = [i -1 for i in var_index] # convert to python index
file_exact_list = 'exact.csv'
file_data=open(file_exact_list, 'r')
# read remaining of the file and store data
x_exact, pressure_exact, density_exact, velocity_exact, temperature_exact = [], [], [], [], []
for line in file_data:
  row = line.split(',')
  x_exact.append(row[var_index[0]])
  pressure_exact.append(row[var_index[1]])
  density_exact.append(row[var_index[2]])
  velocity_exact.append(row[var_index[3]])
  temperature_exact.append(row[var_index[4]])
file_data.close()
x_left=x_exact[0]
x_exact[:] = [float(x)-float(x_left) for x in x_exact]
                           
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
var_index = [10, 11, 20, 21, 24, 9, 11] # [pressure, density, temperature, velocity, x, visc max, kappa, mu]
var_index[:] = [i -1 for i in var_index] # convert to python index

file_list = []
#file_list.append('air-shock-tube-pts.csv')
for input in xrange(1, len(sys.argv)-1):
  file_list.append(sys.argv[input])
nb_files = len(file_list)

# OUTPUT SOME INFORMATION
print '------------------------------'
#print 'Number of files with exact solution to read:', nb_exact_files
#print 'Number of nodes in exact solution:', nb_nodes_exact
print 'Number of files to read:', nb_files
print 'Index of variables in each file:', var_index

# VARIABLES TO STORE DATA
nb_cells = []

#nb_files = 2
#x_offset = np.zeros((1,nb_files))

#print x_offset, len(x_offset)
#x_offset = np.append(x_offset, np.array([[1,2]]), axis=0)
#print x_offset, len(x_offset), x_offset[0], x_offset[1]

pressure = []
density = []
temperature = []
velocity = []
x_coord = []
legend_plot = []

#test = [0,1,2,3]
#cells = [np.array(a) for a in [[0,1,2,3], [2,3,4]]]
#print cells, cells[0], cells[1]
#cells = [np.array(a) for a in [test, [2,3,4]]]
#print cells, cells[0], cells[1]
#test = cells
#cells = [np.array(a) for a in [test, [2,3,4]]]
#print cells, cells[0], cells[1]
#cells = []
#cells.append([0,1,2,3])
#cells.append([0,1,2,3, 4])
#print cells, cells[0], cells[1]
#sys.exit()

out_file = sys.argv[-1]

# LOOP OVER FILES TO COMPUTE L2 and L1 norms
for file in file_list:
  print '------------------------------'
  print 'Name of the input file:', file
  # set/reset data
  pressure_tmp = []
  density_tmp = []
  temperature_tmp = []
  velocity_tmp = []
  x_coord_tmp = []
  # open file and read first line
  file_data=open(file, 'r')
  line_head = file_data.readline()
  print 'Variables in file', file,':', line_head[:-1]
  # read remaining of the file and store data
  for line in file_data:
    row = line.split(',')
    pressure_tmp.append(row[var_index[0]])
    density_tmp.append(row[var_index[1]])
    temperature_tmp.append(row[var_index[2]])
    velocity_tmp.append(row[var_index[3]])
    x_coord_tmp.append(row[var_index[4]])
  
  pressure.append(pressure_tmp)
  density.append(density_tmp)
  temperature.append(temperature_tmp)
  velocity.append(velocity_tmp)
  x_coord.append(x_coord_tmp)
  nb_cells.append(len(x_coord_tmp)-1)
  # legend 1
#  legend_plot.append(str(nb_cells[-1])+' \ cells')
  # legend 2
  legend_plot.append(str(nb_cells[-1])+' \ cells')
  print'Number of cells in file', file, ':', nb_cells[-1]

  file_data.close()

pressure.append(pressure_exact)
density.append(density_exact)
temperature.append(temperature_exact)
velocity.append(velocity_exact)
x_coord.append(x_exact)
legend_plot.append('exact')
# legend FOV vs EVM
#legend_plot.append(str(nb_cells[-1])+' \ cells \ FOV')
#legend_plot.append(str(nb_cells[-1])+' \ cells \ EVM')

## legend FOV vs EVM
#legend_plot.append(str(nb_cells[-1])+' \ cells \ cfl \ 0.1')
#legend_plot.append(str(nb_cells[-1])+' \ cells \ cfl \ 0.5')
#legend_plot.append(str(nb_cells[-1])+' \ cells \ cfl \ 1.0')

plot_solution(x_coord, density, r'$x \ (m)$', r'$\rho \ (kg/m^3)$', 'density', legend_plot)
plot_solution(x_coord, pressure, r'$x \ (m)$', r'$P \ (Pa)$', 'pressure', legend_plot)
plot_solution(x_coord, velocity, r'$x \ (m)$', r'$u \ (m/s)$', 'velocity', legend_plot)
plot_solution(x_coord, temperature, r'$x \ (m)$', '$T \ (K)$', 'temperature', legend_plot)

#  plot_visc_coeff(x_coord, 'air-shock-tube-cells0.csv', var_index, nb_cells[-1])

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