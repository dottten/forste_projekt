#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jun 12 12:10:28 2018

@author: Lasse
"""

import numpy as np

# Funktionen laver forskellige statistiske beregninger
# Input er en Nx3 matrix med datapunkter
# Temperatur er første kolonne, Growth rate er anden kolonne
# Tredje kolonne er bakterietypen, men der bruges kun de to 
# første kolonner til udregning 
# Statistic er den ønskede statistik, der er 7 muligheder

# data = np.array([[12, 4, 5], [15, 2, 9], [18, 2, 8], [20, 4, 10], [22, 3, 12]])
def dataStatistics(data, statistic):
    # Middelværdi for temperaturen
    if statistic == "Mean Temperature":
        MnTmp = np.mean(data[:,0])
        result = ("The {:s} is {:.3f} degrees".format(statistic, MnTmp))
        
        
    # Middelværdi for vækstraten
    elif statistic == "Mean Growth rate":
        MnGrw = np.mean(data[:,1])
        result = ("The {:s} is {:.3f}".format(statistic, MnGrw))
        
        
    # Standard afvigelsen af temperaturen
    elif statistic == "Std Temperature":
        StdTmp = np.std(data[:,0])
        result = ("The {:s} is {:.3f}".format(statistic, StdTmp))
        
        
    # Standard afvigelsen af vækstraten
    elif statistic == "Std Growth rate":
        StdGrw = np.std(data[:,1])
        result = ("The {:s} is {:.3f}".format(statistic, StdGrw))
        
        
    # Antallet af rækker
    elif statistic == "Rows":
        Rows = np.size(data, axis = 0)
        result = ("There are {:.0f} {:s}".format(Rows, statistic))
        
        
    # Middelværdi for vækstraten for temperaturer under 20 grader
    elif statistic == "Mean Cold Growth rate":
        Cold = np.mean(data[:,1][data[:,0] < 20])
        result = ("The {:s} is {:.3f}".format(statistic, Cold)) 
  
    
    # Middelværdi for vækstraten for temperaturer over 50 grader
    elif statistic == "Mean Hot Growth rate":
        Hot = np.mean(data[:,1][data[:,0] > 50])
        result = ("The {:s} is {:.3f}".format(statistic, Hot))
        
        
    # Hvis der er en fejl
    else:
        result = ("Error, please try again")
   
    return result
#print(dataStatistics(data, "Rows"))