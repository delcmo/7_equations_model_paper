#!/bin/sh

## air shock tube
python plot-multiple-solutions.py air-shock-tube_out_displaced.100-pts0.csv air-shock-tube_out_displaced.200-pts0.csv air-shock-tube_out_displaced.400-pts0.csv air-shock-tube_out_displaced.800-pts0.csv air-shock-tube

# FOV vs EVM 100 cells cfl 0.1
#python plot-multiple-solutions.py air-shock-tube_out_displaced.100-cells-cfl-0.1-pts0.csv air-shock-tube_out_displaced.100-cells-cfl-0.1-fo-pts0.csv

# FOV vs EVM 200 cells cfl 0.1
#python plot-multiple-solutions.py air-shock-tube_out_displaced.200-cells-cfl-0.1-pts0.csv air-shock-tube_out_displaced.200-cells-cfl-0.1-fo-pts0.csv

## FOV vs EVM 400 cells cfl 0.1
#python plot-multiple-solutions.py air-shock-tube_out_displaced.400-cells-cfl-0.1-pts0.csv air-shock-tube_out_displaced.400-cells-cfl-0.1-fo-pts0.csv

## FOV vs EVM 800 cells cfl 0.1
#python plot-multiple-solutions.py air-shock-tube_out_displaced.800-cells-cfl-0.1-pts0.csv air-shock-tube_out_displaced.800-cells-cfl-0.1-fo-pts0.csv

## EVM for cfl 0.1 0.5 and 1 400 cells
#python plot-multiple-solutions.py air-shock-tube_out_displaced.200-cells-cfl-0.1-pts0.csv air-shock-tube_out_displaced.200-cells-cfl-0.5-pts0.csv air-shock-tube_out_displaced.200-cells-cfl-1.0-pts0.csv
### liquid shock tube
#python plot-multiple-solutions.py liquid-shock-tube_out_displaced.100-pts0.csv liquid-shock-tube_out_displaced.200-pts0.csv liquid-shock-tube_out_displaced.400-pts0.csv liquid-shock-tube_out_displaced.800-pts0.csv
#
### vapor shock tube
#python plot-multiple-solutions.py vapor-shock-tube_out_displaced.100-pts0.csv vapor-shock-tube_out_displaced.200-pts0.csv vapor-shock-tube_out_displaced.400-pts0.csv vapor-shock-tube_out_displaced.800-pts0.csv