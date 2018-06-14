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


def dataStatistics(data, statistic):
    # Middelværdi for temperaturen
    if statistic == "Mean Temperature":
        MnTmp = np.mean(data[:,0])
        result = ("The mean temperature is {:.3f} degrees".format(MnTmp))
        print("You have chosen to see the average of the temperatures")
        
        
    # Middelværdi for vækstraten
    elif statistic == "Mean Growth rate":
        MnGrw = np.mean(data[:,1])
        result = ("The mean growth rate is {:.3f}".format(MnGrw))
        print("You have chosen to see the average of the growth rates")
        
        
    # Standard afvigelsen af temperaturen
    elif statistic == "Std Temperature":
        StdTmp = np.std(data[:,0])
        result = ("The standard deviation of the temperature is {:.3f}".format(StdTmp))
        print("You have chosen to see the standard deviation of the temperature")
        
        
    # Standard afvigelsen af vækstraten
    elif statistic == "Std Growth rate":
        StdGrw = np.std(data[:,1])
        result = ("The standard deviation of the growth rate is {:.3f}".format(StdGrw))
        print("You have chosen to see the standard deviation of the growth rate")
        
        
    # Antallet af rækker
    elif statistic == "Rows":
        Rows = np.size(data, axis = 0)
        result = ("There are {:.0f} {:s}".format(Rows, statistic))
        print("You have chosen to see the number of rows in the data set")
        
        
    # Middelværdi for vækstraten for temperaturer under 20 grader
    elif statistic == "Mean Cold Growth rate":
        Cold = np.mean(data[:,1][data[:,0] < 20])
        result = ("The {:s} is {:.3f}".format(statistic, Cold)) 
        print("You have chosen to see the average growth rate for temperatures under 20 degrees")
        
    
    # Middelværdi for vækstraten for temperaturer over 50 grader
    elif statistic == "Mean Hot Growth rate":
        Hot = np.mean(data[:,1][data[:,0] > 50])
        result = ("The {:s} is {:.3f}".format(statistic, Hot))
        print("You have chosen to see the average growth rate for temperatures over 50 degrees")
        
        
    # Hvis der er en fejl
    else:
        result = ("Error, not a valid option. Please try again")
   
    return result