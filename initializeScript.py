# -*- coding: utf-8 -*-
"""
Created on Wed Jun 13 11:42:18 2018

@author: loved
"""

def initializeScript():
    
    #import packages
    global np;
    import numpy as np;
    
    global plt;
    import matplotlib.pyplot as plt;
    
    global math;
    import math;
    
    
    #import functions
    global userInputMenu;
    global userInputNumber;
    from userInput import userInputMenu;
    from userInput import userInputNumber;
    
    global growthRateTemperature;
    from growthRateTemperature import growthRateTemperature;
    
    global numberOfBacteria;
    from numberOfBacteria import numberOfBacteria;
    
    global dataStatistics;
    from Statistik import dataStatistics;
    
    
    #global variables
    global regular_temp_range;
    regular_temp_range = np.array([10,60]);
    
    global chosen_bacteria;
    chosen_bacteria = np.arange(1,5);
    
    global growth_range;
    growth_range = np.array([0,1000000000]);

    