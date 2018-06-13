# -*- coding: utf-8 -*-
"""
Created on Wed Jun 13 10:23:24 2018

@author: loved
"""

import numpy as np;

#userInputMenu printer en menu til brugeren og beder om en valgmulighed.
#options er et NumPy array, der indeholder de strings, som skal være brugerens muligheder.
#showstring er den streng som vises til brugeren, og forklarer hvad der skal inputtes.
def userInputMenu(options,showstring):
    
    #option-list
    for i in range(len(options)):
        print("{:d}. {:s}".format(i+1, options[i]))
    
    # Get a valid menu choice
    choice = -12345675364131245;
    
    #undersøger om choice er en af de viste muligheder
    while not(np.any(choice == np.arange(len(options))+1)):
        if choice != -12345675364131245:
            print("Input must have one of the displayed id's. Please try again.")
        while True:
            try:
                choice = float(input("{:s}: ".format(showstring.capitalize())));
                break;
            except ValueError:
                print('Input is not valid. Please try again.')
                pass
    
    return choice


# userInputNumber printer en forespørgsel om et talinput fra brugeren
    
# input:
    # showstring er den forespørgsel, der vises til brugeren
    # limit er et NumPy array der indeholder to værdier; henholdsvis et minimum og et maksimum for inputtet.
        # hvis der ikke ønskes et max eller min inputtes værdien False.
        # Ex: Hvis man kun vil have et max på 60.
        # limit = np.array([False,60]);
def userInputNumber(showstring,limit):
    while True:
            
            try:
                
                choice = float(input("{:s}: ".format(showstring.capitalize())));
                
                if (limit[0] != False):
                    
                    if (limit[0] <= choice):
                        condition = 1;
                    
                    else:
                        print('Input is below the desired minimum of {:f}. Please try again.'.format(limit[0]));
                        condition = 0;
                
                else:
                    condition = 1;
                    
                if (condition == 1):
                    
                    if (limit[1] != False):
                    
                        if (limit[1] >= choice):
                            break;
                    
                        else:
                            print('Input is higher than the desired maximum of {:f}. Please try again.'.format(limit[1]));
                            condition = 0;
                    else:
                        break;
                        
            except ValueError:
                print("Not valid number. Please try again.")
    
    return choice