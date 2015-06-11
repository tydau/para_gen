#!/usr/bin/python
#title			:para_gen.py
#description	:Generates paramter value list for COMSOL Cell Mechanics Cell Indent experiment.
#author			:T. Tyler Daugherty
#date			:20150611
#version		:01
#usage			:python para_gen.py
#notes			:
#python_version	:2.6.6
#==============================================================================

import sys
import numpy as np

start = float(raw_input("Starting point:\n"))
end = float(raw_input("Ending point:\n"))
int = float(raw_input("Inverval:\n"))
name = 'cellindent.txt'

para_vals = list(np.arange(start,end+int,int))
parra_vals_rev = list(reversed(np.arange(start,end,int)))
para_vals.append(parra_vals_rev)
para_vals = str(para_vals).strip('[]')
para_vals = para_vals.replace("[","")

file = open(name,'w')
file.write(para_vals)
file.close()
