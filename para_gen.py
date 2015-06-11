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

start = raw_input("Starting point:\n")
end = raw_input("Ending point:\n")
int = raw_input("Inverval:\n")
name = 'cellindent.txt'

para_vals = np.arange(start,end,int)

np.savetxt(name,para_vals)
