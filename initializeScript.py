# -*- coding: utf-8 -*-
"""
Created on Wed Jun 13 11:42:18 2018

@author: Ditlev
"""

def initializeScript():
    
    #import packages
    import numpy as np;
    import matplotlib.pyplot as plt;
    import math;
    
    
    #import functions
    from userInput import userInputMenu;
    from userInput import userInputNumber;
    
    from growthRateTemperature import growthRateTemperature;
    
    from numberOfBacteria import numberOfBacteria;
    
    from Statistik import dataStatistics;
    from initializeScript import initializeScript;
    
    
    #global variables
    global regular_temp_range;
    regular_temp_range = np.array([10,60]);
        
    global chosen_bacteria;
    chosen_bacteria = np.arange(1,5);
        
    global growth_range;
    growth_range = np.array([0,1000000000]);
    

    