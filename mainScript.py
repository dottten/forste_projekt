# -*- coding: utf-8 -*-
"""
Created on Wed Jun 13 12:11:44 2018

@author: Anders, Ditlev & Lasse
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

from dataLoad import dataLoad;

from plotImageConf import plotImageConf;


#global variables
regular_temp_range = np.array([10,60]);
chosen_bacteria = np.arange(1,5);
growth_range = np.array([0,1000000000]);
bacterias = np.array(['Salmonella enterica','Bacillus cereus','Listeria','Brochothrix thermosphacta']);


while True:
    
    print();
    
    ## Hovedmenu
    choice = userInputMenu(np.array(['Read Data','Filter Data','Show Statistics','Create Plots','Quit']),'Please select an option');
    
    
    ####   Read data option  ####
    if (choice == 1):
        
        print();

        
        #Liste over tilgængelige filer i mappen
        file_list = np.asarray(os.listdir());
        complete_list = np.insert(file_list,np.size(file_list),'Cancel')
        
        #Vælge data-fil
        while True:
            file_choice = userInputMenu(complete_list,'Select the data-file you want to use');
            
            
            if file_choice == np.size(complete_list):
                print();
                print('Going back to main menu.');
                
                break;
                
                
            ##  Reset af data inden ny fil oploades, hvis der allerede er loaded en fil
            if ('data_loaded' in locals()) and ((regular_temp_range[0] != 10) or (regular_temp_range[1] != 60) or (chosen_bacteria[0] != 1) or (chosen_bacteria[1] != 2) or (chosen_bacteria[2] != 3) or (chosen_bacteria[3] != 4) or (growth_range[0] != 0) or  (growth_range[1] != 1000000000)): 
                print();
                    
                while True:
                    reset_choice = userInputMenu(np.array(['Yes', 'No']), 'Do you want to reset your filters before uploading file');
                        
                    if reset_choice == 1:
                        regular_temp_range = np.array([10,60]);
                        chosen_bacteria = np.arange(1,5);
                        growth_range = np.array([0,1000000000]);
                        data_matrix = dataLoad(complete_list[int(file_choice) - 1],regular_temp_range,chosen_bacteria,growth_range);
                        print();
                        break;
                            
                    if reset_choice == 2:
                        print();
                        break;
                        
                # Den nye fil med værdier bliver brugt
                try:
                    data_matrix = dataLoad(complete_list[int(file_choice) - 1],regular_temp_range,chosen_bacteria,growth_range);
                
                    
                    print();
                    print('Data has now been read. Aforementioned faulty lines are not included.')
                    
                    data_loaded = file_choice;
                    break;
               
                # Fejlkoder
                except IndexError:
                    print();
                    print('Invalid file. Please try again');
                except PermissionError:
                    print();
                    print('Invalid file. Please try again');
                except UnboundLocalError:
                    print();
                    print('Invalid file. Please make sure data is within the given ranges');
                except IsADirectoryError:
                    print();
                    print('Invalid file. Please try again');
                except UnicodeDecodeError:
                    print();
                    print('Invalid file. Please try again');
                    
                    
                    
            # Første fil kan bruges
            else:
                try:
                    data_matrix = dataLoad(complete_list[int(file_choice) - 1],regular_temp_range,chosen_bacteria,growth_range);
                
                    
                    print();
                    print('Data has now been read. Aforementioned faulty lines are not included.')
                    
                    data_loaded = file_choice;
                    break;
               
                # Fejlkoder
                except IndexError:
                    print();
                    print('Invalid file. Please try again');
                except PermissionError:
                    print();
                    print('Invalid file. Please try again');
                except UnboundLocalError:
                    print();
                    print('Invalid file. Please try again');
                except IsADirectoryError:
                    print();
                    print('Invalid file. Please try again');
                except UnicodeDecodeError:
                    print();
                    print('Invalid file. Please try again');
    
    ####   Filtrér data option   ####
    if (choice == 2):
        print();
        
        while True:
            filter_choice = userInputMenu(np.array(['Edit temperature range','Specify relevant bacteria','Edit Growth-rate-range','Reset','Show Filters','Go back']),'Please select an option');
                    
            
            ##  Go back
            if filter_choice == 6:
                print();
                print('Going back to main menu.');
                break;
            
            ## See filters
            if filter_choice == 5:
                print();
                print('The temperature range is from {:.3f} to {:.3f}.'.format(regular_temp_range[0],regular_temp_range[1]));
                
                for i in range(np.size(chosen_bacteria)):
                    if np.any(i+1 == chosen_bacteria):
                        print('{:s} has been chosen.'.format(bacterias[i]));
                
                if growth_range[1] == 1000000000:
                    print('The growth-rate range is all positive growth-rate values.');
                else:
                    print('The growth-rate range is from {:.3f} to {:.3f}.'.format(growth_range[0],growth_range[1]));
                print();
                
            try: 
                isinstance(data_loaded,float);
                
                
                ##  Temperature range
                if filter_choice == 1:
                    
                    t_lower_limit = userInputNumber('Please input the lower limit of the temperature',np.array([10,False]));
                    t_upper_limit = userInputNumber('Please input the upper limit of the temperature',np.array([t_lower_limit,60]));
                    regular_temp_range = np.array([t_lower_limit,t_upper_limit]);
                    data_matrix = dataLoad(complete_list[int(file_choice) - 1],regular_temp_range,chosen_bacteria,growth_range);
                    print();
                    
                
                ##  Selceting bacteriatypes
                if filter_choice == 2:
                     
                    
                    while True:
                        print();
                        
                        
                        ##  Naming of variable options in menu
                        if chosen_bacteria[0] != 0:
                            Bacteria_1 = 'Remove Salmonella enterica'
                        
                        else:
                            Bacteria_1 = 'Add Salmonella enterica'
                            
                            
                            
                        if chosen_bacteria[1] != 0:
                            Bacteria_2 = 'Remove Bacillus cereus'
                        
                        else:
                            Bacteria_2 = 'Add Bacillus cereus'
                            
                            
                            
                        if chosen_bacteria[2] != 0:
                            Bacteria_3 = 'Remove Listeria'
                        
                        else:
                            Bacteria_3 = 'Add Listeria'
                            
                            
                            
                        if chosen_bacteria[3] != 0:
                            Bacteria_4 = 'Remove Brochothrix thermosphacta'
                        
                        else:
                            Bacteria_4 = 'Add Brochothrix thermosphacta'
                            
                       
                        
                        ## Menu 
                        Bacteria_choice = userInputMenu(np.array([Bacteria_1, Bacteria_2, Bacteria_3, Bacteria_4, 'Go back']),'Please select an option');
                        
                        ##  Remove/add bacteria 1
                        if Bacteria_choice == 1:
                            if chosen_bacteria[0] != 0:
                                chosen_bacteria[0] = 0;
                                
                            
                            else:
                                chosen_bacteria[0] = 1;
                        
                        
                        ##  Remove/add bacteria 2
                        if Bacteria_choice == 2:
                            if chosen_bacteria[1] != 0:
                                chosen_bacteria[1] = 0;
                                
                            
                            else:
                                chosen_bacteria[1] = 2;
                            
                            
                            
                        ##  Remove/add bacteria 3
                        if Bacteria_choice == 3:
                            if chosen_bacteria[2] != 0:
                                chosen_bacteria[2] = 0;
                                
                            
                            else:
                                chosen_bacteria[2] = 3;
                            
                            
                            
                        ##  Remove/add bacteria 4
                        if Bacteria_choice == 4:
                            if chosen_bacteria[3] != 0:
                                chosen_bacteria[3] = 0;
                                
                            
                            else:
                                chosen_bacteria[3] = 4;
                            
                            
                        
                        
                        ##  Go back
                        if Bacteria_choice == 5:
                            if (chosen_bacteria[0] + chosen_bacteria[1] + chosen_bacteria[2] + chosen_bacteria[3]) != 0:
                                data_matrix = dataLoad(complete_list[int(file_choice) - 1],regular_temp_range,chosen_bacteria,growth_range);
                                print();
                                print('Going back.');
                                print();
                                break;
                            
                            else:
                                print();
                                plotImageConf();

                
                
                
                ##  Growth rate range
                if filter_choice == 3:
                    
                    g_lower_limit = userInputNumber('Please input the lower limit of the growth-rate',np.array([1e-10,False]));
                    g_upper_limit = userInputNumber('Please input the upper limit of the growth-rate',np.array([g_lower_limit,False]));
                    growth_range = np.array([g_lower_limit,g_upper_limit]);
                    data_matrix = dataLoad(complete_list[int(file_choice) - 1],regular_temp_range,chosen_bacteria,growth_range);
                    print();
                    
                    
                ##  Reset all ranges    
                if filter_choice == 4:
                    regular_temp_range = np.array([10,60]);
                    chosen_bacteria = np.arange(1,5);
                    growth_range = np.array([0,1000000000]);
                    data_matrix = dataLoad(complete_list[int(file_choice) - 1],regular_temp_range,chosen_bacteria,growth_range);
                    print();
                    
 
            except NameError:
                print();
                print('Please read a valid data-file first. Optionally set new ranges for the current data file.')
                print();
                break;
      
        
    ####    Statistics   ####
    if (choice == 3):
        while True:
            print();
            
            statistic_choice = userInputMenu(np.array(['Mean temperature','Mean growth rate','Standard deviation of temperature', 'Standard deviation of growth rate', 'Number of valid rows', 'Mean growth rate for temperatures under 20 degrees', 'Mean growth rate for temperatures over 50 degrees', 'Go back']),'Please select an option');
            
            
            
            ##  Go back
            if statistic_choice == 8:
                print();
                print('Going back to main menu.');
                break;
                
            
            try: 
                isinstance(data_loaded,float);
                
                
                ##  Mean temperature
                if statistic_choice == 1:
                    print(dataStatistics(data_matrix, "Mean Temperature"))
                    
                
                
                ##  Mean growth rate
                if statistic_choice == 2:
                    print(dataStatistics(data_matrix, "Mean Growth rate"))
                    
                
                
                ##  Standard deviation of temperature
                if statistic_choice == 3:
                    print(dataStatistics(data_matrix, "Std Temperature"))
                    
                    
                    
                ##  Standard deviation of growth rate    
                if statistic_choice == 4:
                    print(dataStatistics(data_matrix, "Std Growth rate"))
                    
                    
                    
                ##  Number of valid rows   
                if statistic_choice == 5:
                    print(dataStatistics(data_matrix, "Rows"))
                    
            
            
                ##  Mean growth rate for cold temperatures    
                if statistic_choice == 6:
                    print(dataStatistics(data_matrix, "Mean Cold Growth rate"))
                    
                    
                    
                ##  Mean growth rate for hot temperatures    
                if statistic_choice == 7:
                    print(dataStatistics(data_matrix, "Mean Hot Growth rate"))
                    
                    
 
            except NameError:
                print();
                print('Please read a valid data-file first. Optionally set new ranges for the current data file.')
                print();
                break;
   
    
    
    ####    Plots   ####
    if (choice == 4):
        while True: 
            print();
            
            
            # Plot menu
            plot_choice = userInputMenu(np.array(['Create a bar chart of the different number of bacteria and how often they occur.','Create a plot over the differnet bacterias growth rate as a function of temperature', 'Create both plots.', 'Go back']),'Please select an option');
            
            
            # Go back
            if plot_choice == 4:
                print();
                print('Going back to main menu.');
                print();
                break;
         
            
            # Sikrer der er en fil uploaded
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
        
        
            except NameError:
                print();
                print('Please read a valid data-file first. Optionally set new ranges for the current data file.')
                print();
                break;
                
    
    
    
    ####    Quit program   ####
    if (choice == 5):
        print();
        print('Program shutting down.');
        try:
            del data_loaded;
        except NameError:
            del choice;
        break;
    