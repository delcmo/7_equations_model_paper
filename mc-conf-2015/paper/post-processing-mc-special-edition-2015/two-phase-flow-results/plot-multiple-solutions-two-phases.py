# This script aims at reading csv files and store the data for postprocessing in 1-D.

#### import python modules ####
import sys, os, math, csv, itertools
import numpy as np
import itertools as it
import matplotlib.pyplot as plt
from decimal import *
#### import python modules ####

#### define function ####
def plot_solution(x_num, y_num_vapor, y_num_liquid, x_label, y_label_vap, y_label_liq, label, legend_plot):
  marker_list = itertools.cycle(('x', '+', '.', '|', '2', '3', '4', 'o'))
  color_list = itertools.cycle(['b', 'g', 'r', 'c', 'm', 'y', 'k'])
  x_min, x_max, y_min_vapor, y_max_vapor, y_min_liquid, y_max_liquid = 1.e10, 0.0, 1.e10, 0.0, 1.e10, 0.0
  fig, ax1 = plt.subplots()
  ax2 = ax1.twinx()
  lgd1, lgd2 = [], []
  for i in xrange(0, len(x_num)):
    nb_cells = len(x_num[i])-1
    color = color_list.next()
    lx1 = ax1.plot(x_num[i], y_num_vapor[i], '--', marker=marker_list.next(), markevery=nb_cells/10+i, markersize=10, label=r'$%s \ vapor$' % str(legend_plot[i]), linewidth=1, mfc="None", mew=1.2, c=color, markeredgecolor=color)
    color = color_list.next()
    lx2 = ax2.plot(x_num[i], y_num_liquid[i], '-', marker=marker_list.next(), markevery=nb_cells/10+i, markersize=10, label=r'$%s \ liquid$' % str(legend_plot[i]), linewidth=1, mfc="None", mew=1.2, c=color, markeredgecolor=color)
    lgd1+=lx1
    lgd2+=lx2
    x_min = min(float(min(x_num[i])), x_min)
    x_max = max(float(max(x_num[i])), x_max)
    y_min_vapor = min(float(min(y_num_vapor[i])), y_min_vapor)
    y_min_liquid = min(float(min(y_num_liquid[i])), y_min_liquid)
    y_max_vapor = max(float(max(y_num_vapor[i])), y_max_vapor)
    y_max_liquid = max(float(max(y_num_liquid[i])), y_max_liquid)

  labs1 = [l.get_label() for l in lgd1]
  labs2 = [l.get_label() for l in lgd2]
  ax1.legend(lgd1, labs1, loc='upper left', frameon=False, fontsize=15, ncol=1, bbox_to_anchor=(0.5, 1.+0.07*len(x_num)), borderaxespad=0.)
  ax2.legend(lgd2, labs2, loc='upper right', frameon=False, fontsize=15, ncol=1, bbox_to_anchor=(0.5, 1.+0.07*len(x_num)), borderaxespad=0.)
#  ax1.legend(lgd, labs, loc='upper center', frameon=False, fontsize=15, ncol=2, bbox_to_anchor=(0.5, 1.+0.07*len(x_num)),  mode="expand", borderaxespad=0.)
#  location_leg = 'center right'
#  ax1.legend(loc=location_leg, fontsize=15, frameon=False, ncol=len(x_num))
#  ax2.legend(loc='best', fontsize=15, frameon=False)
  ax1.set_xlabel('%s' % x_label, fontsize=25)
  ax1.set_ylabel('%s' % y_label_vap, fontsize=25)
  ax2.set_ylabel('%s' % y_label_liq, fontsize=25)
  ax1.set_xlim(float(x_min), float(x_max))

  if float(y_max_vapor) > 1e4:
    print '    Use scientific notation for y-axis'
    ax1.ticklabel_format(style='sci', axis='y', scilimits=(0,0))
  if float(y_max_liquid) > 1e4:
    print '    Use scientific notation for y-axis'
    ax2.ticklabel_format(style='sci', axis='y', scilimits=(0,0))
#  ax1.set_margins(0.1, 0.1)
  fig_name=out_file+'-'+label+'-plot.eps'
  fig.savefig(fig_name, bbox_inches='tight')
  print 'Saving plot using Matplotlib:', fig_name
  fig.clf()

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
var_index = [27, 15, 33, 37, 12, 25, 14, 32, 36, 5, 40 ] # [pressure, density, temperature, velocity, alpha, x]
var_index[:] = [i -1 for i in var_index] # convert to python index

file_list = []
for input in xrange(1, len(sys.argv)-1):
  file_list.append(sys.argv[input])
#else:
#  file_list.append(sys.argv[1])

nb_files = len(file_list)

if len(sys.argv) > 2:
  out_file = sys.argv[-1]
else:
  out_file = 'plot'

# OUTPUT SOME INFORMATION
print '------------------------------'
#print 'Number of files with exact solution to read:', nb_exact_files
#print 'Number of nodes in exact solution:', nb_nodes_exact
print 'Number of files to read:', nb_files
print 'Index of variables in each file:', var_index
print 'Ouput file:', out_file

# VARIABLES TO STORE DATA
nb_cells = []

#nb_files = 2
#x_offset = np.zeros((1,nb_files))

#print x_offset, len(x_offset)
#x_offset = np.append(x_offset, np.array([[1,2]]), axis=0)
#print x_offset, len(x_offset), x_offset[0], x_offset[1]

pressure_vapor, pressure_liquid = [], []
density_vapor, density_liquid = [], []
temperature_vapor, temperature_liquid = [], []
velocity_vapor, velocity_liquid = [], []
alpha_vapor, alpha_liquid = [], []
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

# LOOP OVER FILES TO COMPUTE L2 and L1 norms
for file in file_list:
  print '------------------------------'
  print 'Name of the input file:', file
  # set/reset data
  pressure_vap_tmp, pressure_liq_tmp = [], []
  density_vap_tmp, density_liq_tmp = [], []
  temperature_vap_tmp, temperature_liq_tmp = [], []
  velocity_vap_tmp, velocity_liq_tmp = [], []
  alpha_vap_tmp, alpha_liq_tmp = [], []
  x_coord_tmp = []
  # open file and read first line
  file_data=open(file, 'r')
  line_head = file_data.readline()
  print 'Variables in file', file,':', line_head[:-1]
  # read remaining of the file and store data
  for line in file_data:
    row = line.split(',')
    pressure_vap_tmp.append(row[var_index[0]])
    density_vap_tmp.append(row[var_index[1]])
    temperature_vap_tmp.append(row[var_index[2]])
    velocity_vap_tmp.append(row[var_index[3]])
    alpha_vap_tmp.append(row[var_index[4]])
    pressure_liq_tmp.append(row[var_index[5]])
    density_liq_tmp.append(row[var_index[6]])
    temperature_liq_tmp.append(row[var_index[7]])
    velocity_liq_tmp.append(row[var_index[8]])
    alpha_liq_tmp.append(row[var_index[9]])
    x_coord_tmp.append(row[var_index[10]])

  pressure_vapor.append(pressure_vap_tmp)
  density_vapor.append(density_vap_tmp)
  temperature_vapor.append(temperature_vap_tmp)
  velocity_vapor.append(velocity_vap_tmp)
  alpha_vapor.append(alpha_vap_tmp)
  pressure_liquid.append(pressure_liq_tmp)
  density_liquid.append(density_liq_tmp)
  temperature_liquid.append(temperature_liq_tmp)
  velocity_liquid.append(velocity_liq_tmp)
  alpha_liquid.append(alpha_liq_tmp)
  x_coord.append(x_coord_tmp)
  nb_cells.append(len(x_coord_tmp)-1)
  # legend 1
  legend_plot.append(str(nb_cells[-1])+' \ cells')
  print'Number of cells in file', file, ':', nb_cells[-1]

  file_data.close()

## legend FOV vs EVM
#legend_plot.append(str(nb_cells[-1])+' \ cells \ FOV')
#legend_plot.append(str(nb_cells[-1])+' \ cells \ EVM')

## legend FOV vs EVM
#legend_plot.append(str(nb_cells[-1])+' \ cells \ cfl \ 0.1')
#legend_plot.append(str(nb_cells[-1])+' \ cells \ cfl \ 0.5')
#legend_plot.append(str(nb_cells[-1])+' \ cells \ cfl \ 1.0')

plot_solution(x_coord, density_vapor, density_liquid, r'$x \ (m)$', r'$\rho_{vap} \ (kg/m^3)$', r'$\rho_{liq} \ (kg/m^3)$', 'density', legend_plot)
plot_solution(x_coord, pressure_vapor, pressure_liquid, r'$x \ (m)$', r'$P_{vap} \ (Pa)$', r'$P_{liq} \ (Pa)$', 'pressure', legend_plot)
plot_solution(x_coord, velocity_vapor, velocity_liquid, r'$x \ (m)$', r'$u_{vap} \ (m/s)$', r'$u_{liq} \ (m/s)$', 'velocity', legend_plot)
plot_solution(x_coord, temperature_vapor, temperature_liquid, r'$x \ (m)$', r'$T_{vap} \ (K)$', r'$T_{liq} \ (K)$', 'temperature', legend_plot)
plot_solution(x_coord, alpha_vapor, alpha_liquid, r'$x \ (m)$', r'$\alpha_{vap}$', r'$\alpha_{liq}$', 'vf', legend_plot)

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