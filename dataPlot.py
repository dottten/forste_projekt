# -*- coding: utf-8 -*-
"""
Created on Wed Jun 13 11:50:58 2018

@author: ander
"""

from growthRateTemperature import growthRateTemperature
from numberOfBacteria import numberOfBacteria
from userInput import userInputMenu
import numpy as np
import matplotlib.pyplot as plt

#Testarray, skal fjernes i den endelige version. 
testarray = np.array([[96, 0.353, 1], [20, 0.096, 2], [15, 0.517, 3], [35, 1.086, 4], [40, 0.934, 2], [35, 0.109, 1], [50, 0.859, 3], [48, 0.654, 2], [10, 0.124, 4], [55, 0.065, 1], [60, 1.321, 2], [60, 2.545, 3], [55, 1.524, 4]])

#Dette er den overordnede dataplot funktion. Den består af to underfunktioner,
#growthRateTemperature og numberOfBacteria, og derudover en menufunktion, altså totalt 3 funktioner. 
# 

def dataPlot(data):
    
    choice = userInputMenu(np.array(["Create a bar chart of the different number of bacteria and how often they occur.", "Create a plot over the differnet bacterias growth rate as a function of temperature", "Create both plots."]), "Choose one of the above options.")
    
     
    
    if choice == 1 :
        numberOfBacteria(data)
        
    elif choice == 2:
        growthRateTemperature(data)
            
    elif choice == 3:
        numberOfBacteria(data)
        growthRateTemperature(data)
