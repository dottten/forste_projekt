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



#Dette er den overordnede dataplot funktion. Den består af to underfunktioner,
#growthRateTemperature og numberOfBacteria, og derudover en menufunktion, altså totalt 3 funktioner. 
# 

def dataPlot(data_matrix, data_loaded):

        
    while True: 
        print();
    
    
        #Menu 
        plot_choice = userInputMenu(np.array(["Create a bar chart of the different number of bacteria and how often they occur.", "Create a plot over the differnet bacterias growth rate as a function of temperature", "Create both plots.", "Go back"]), "Choose one of the above options")
    
        # Go back
        if plot_choice == 4:
            print();
            print('Going back to main menu.');
            break;
    
        try: 
            isinstance(data_loaded,float);
    
            # Bar chart
            if plot_choice == 1:
                numberOfBacteria(data_matrix)
                print();
                
            # Growth rate
            if plot_choice == 2:
                growthRateTemperature(data_matrix)
                print();
            
            # Both plots
            if plot_choice == 3:
                numberOfBacteria(data_matrix)
                growthRateTemperature(data_matrix)
                print();

        # Fejlkode
        except NameError:
            print();
            print('Please read a valid data-file first. Optionally set new ranges for the current data file.')
            print();
            break;
