# This python script should be run with the following command line:
# 'pvpython script-csv-write-from-exodus-paraview.py exodus-file'

#### import the simple module from the paraview
from paraview.simple import *
#### disable automatic camera reset on 'Show'
paraview.simple._DisableFirstRenderCameraReset()

import os, glob, sys

print '#### Check current path: ####'
path_in=os.path.realpath('.')
print 'Current path:', path_in
  
input_filename=sys.argv[1]
output_filename_pts=input_filename[:-2]+'-pts.csv'
output_filename_cells=input_filename[:-2]+'-cells.csv'
print 'Exodus file to read with paraview:', input_filename
print 'Excel output files:', output_filename_pts, ' and ', output_filename_cells
# create a new 'ExodusIIReader'
print '#### Open Paraview and read exodus file: ####'
reader = ExodusIIReader(FileName=os.path.join(path_in, input_filename))
# get animation scene
animationScene1 = GetAnimationScene()
# update animation scene based on data timesteps
animationScene1.UpdateAnimationUsingDataTimeSteps()
# select all variables
reader.SelectAllVariables()
renderView1 = GetActiveViewOrCreate('RenderView')
Show(reader, renderView1)
# go to last time step
animationScene1.GoToLast()
#  animationScene1.GoToPrevious()
# save data
print '#### Saving data: ####'
SaveData(os.path.join(path_in, output_filename_pts), proxy=reader, Precision=20, FieldAssociation='Points')
SaveData(os.path.join(path_in, output_filename_cells), proxy=reader, Precision=20, FieldAssociation='Cells')

# remove all files finishing with '1.csv', '2.csv', '3.csv' and '4.csv'
print '#### Removing all unecessary files (*1.csv, *2.csv, *3.csv and *4.csv) ####'
file1csv=glob.glob(os.path.join(path_in, '*1.csv'))
file2csv=glob.glob(os.path.join(path_in, '*2.csv'))
file3csv=glob.glob(os.path.join(path_in, '*3.csv'))
file4csv=glob.glob(os.path.join(path_in, '*4.csv'))
file5csv=glob.glob(os.path.join(path_in, '*5.csv'))
file6csv=glob.glob(os.path.join(path_in, '*6.csv'))
dirlist = file1csv + file2csv + file3csv + file4csv + file5csv + file6csv
for file_csv in dirlist:
  os.remove(file_csv)

print '#### Done removing all unecessary files (*1.csv, *2.csv, *3.csv and *4.csv) ####'

# move the file to a specified directory TODO
#for file_csv in dirlist
#os.rename(os.path.join(path_in), os.path.join(path_out,))

del file1csv, file2csv, file3csv, file4csv, dirlist
