#! /usr/bin/env python3
import os
import csv
import sys
import numpy as np
import codecs

import QFH


#check argument of command
if(len(sys.argv) <= 1):
    print("please set parameter file path (*.csv)")
    exit()

csvPath = sys.argv[1]

#open csv file
with open(csvPath) as f:
    parameterList = np.loadtxt(f,delimiter = ",", dtype = str, skiprows=1)

    print(parameterList.ndim)

    #Only 1 model data (dimension of List = 1)
    if parameterList.ndim == 1:
        parameter = parameterList
        QFH.generateModel(parameter)


    #read each parameter and generate a model data
    else:
        for parameter in parameterList:
            QFH.generateModel(parameter)



