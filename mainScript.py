# -*- coding: utf-8 -*-
"""
Created on Wed Jun 13 12:11:44 2018

@author: loved
"""

#import packages
import numpy as np;
import matplotlib.pyplot as plt;
import math;
import os;


#import functions
from userInput import userInputMenu;
from userInput import userInputNumber;

from growthRateTemperature import growthRateTemperature;

from numberOfBacteria import numberOfBacteria;

from Statistik import dataStatistics;
from initializeScript import initializeScript;

from dataLoad import dataLoad;


#global variables
regular_temp_range = np.array([10,60]);
chosen_bacteria = np.arange(1,5);
growth_range = np.array([0,1000000000]);

while True:
    
    ## Hovedmenu
    choice = userInputMenu(np.array(['Read Data','Filter Data','Show Statistics','Create Plots','Quit']),'Please select an option');
    
    #### Read data option
    if (choice == 1):
        
        #Liste over tilgængelige filer i mappen
        file_list = np.asarray(os.listdir());
        complete_list = np.insert(file_list,np.size(file_list),'Cancel')
        
        #Vælge data-fil
        while True:
            file_choice = userInputMenu(complete_list,'Select the data-file you want to use');
            
            if file_choice == np.size(complete_list):
                print();
                print('Going back to main menu.');
                print();
                
                break;
                
            #Success
            try:
                data_matrix = dataLoad(complete_list[int(file_choice) - 1],regular_temp_range,chosen_bacteria,growth_range);
                print();
                print('Data has now been read. Aforementioned faulty lines are not included.')
                print();
                
                data_loaded = file_choice;
                break;
                
            except IndexError:
                print('Invalid file. Please try again');
            except PermissionError:
                print('Invalid file. Please try again');
            except UnboundLocalError:
                print('Invalid file. Please try again');
    
    #### Filtrer data option
    if (choice == 2):
        while True:
            filter_choice = userInputMenu(np.array(['Edit temperature range','Specify relevant bacteria','Edit Growth-rate-range','Reset','Cancel']),'Please select an option: ');
            
            if filter_choice == 5:
                print();
                print('Going back to main menu.');
                print();
                break;
            
            try: 
                isinstance(data_loaded,float);
                
                if filter_choice == 4:
                    regular_temp_range = np.array([10,60]);
                    chosen_bacteria = np.arange(1,5);
                    growth_range = np.array([0,1000000000]);
                    data_matrix = dataLoad(complete_list[int(file_choice) - 1],regular_temp_range,chosen_bacteria,growth_range);
                    
                if filter_choice == 3:
                    
                    g_lower_limit = userInputNumber('Please input the lower limit of the growth-rate: ',np.array([1e-10,False]));
                    g_upper_limit = userInputNumber('Please input the upper limit of the growth-rate: ',np.array([g_lower_limit,False]));
                    growth_range = np.array([g_lower_limit,g_upper_limit]);
                    data_matrix = dataLoad(complete_list[int(file_choice) - 1],regular_temp_range,chosen_bacteria,growth_range);
                    
            except NameError:
                print();
                print('Please read data-file first.')
                print();
                break;
        
    
    if (choice == 5):
        print();
        print('Program shutting down.');
        break;