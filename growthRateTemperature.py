# -*- coding: utf-8 -*-
"""
Created on Wed Jun 13 11:18:22 2018

@author: Anders
"""

import math
import numpy as np
import matplotlib.pyplot as plt



def growthRateTemperature(data):
    
    #Anders:
    #Plot til 'Growth rate by temperature'. Skaber et plot over de 4 forskellige bakterietypers
    #'Growth Rate' of tilhørende temperatur, sorteret efter en stigende temperatur. 
    #Input skal være en N x 3 matrix, med de maks 4 forskellige bakterietyper der er opgivet i opgaven.
    
    
    #Skaber en nulvektor for hver bakterietype til brug for T      
    x1 = np.zeros(np.size(data, axis = 0))
    x2 = np.zeros(np.size(data, axis = 0))
    x3 = np.zeros(np.size(data, axis = 0))
    x4 = np.zeros(np.size(data, axis = 0))
    
    #Skaber en nulvektor for hver bakterietype til brug for 'Growth rate'      
    y1 = np.zeros(np.size(data, axis = 0))
    y2 = np.zeros(np.size(data, axis = 0))
    y3 = np.zeros(np.size(data, axis = 0))
    y4 = np.zeros(np.size(data, axis = 0))
    
    #Hiver nu dataen ud og indsætter det i den rigtige nulvektor. Gælder kun
    #for fire forskellige bakterietyper
    
    i = 0
    for i in range(np.size(data, axis = 0)):
        
        if data[i, 2] == 1:
            x1[i] = data[i, 0]
            y1[i] = data[i, 1]
            
        elif data[i, 2] == 2:
            x2[i] = data[i, 0]
            y2[i] = data[i, 1]
            
        elif data[i,2] == 3:
            x3[i] = data[i, 0]
            y3[i] = data[i, 1]
            
        elif data[i,2] == 4:
            x4[i] = data[i, 0]
            y4[i] = data[i, 1]
            
        i = i + 1
        
    #Bruger nu kun de værdier der ikke er lig med 0 
    x1 = x1[x1 != 0]
    x2 = x2[x2 != 0]
    x3 = x3[x3 != 0]
    x4 = x4[x4 != 0]
    
    y1 = y1[y1 != 0]
    y2 = y2[y2 != 0]
    y3 = y3[y3 != 0]
    y4 = y4[y4 != 0]
   
    
    #Sorter y-værdierne efter en sortet x-værdi
    inds1 = x1.argsort()
    y1 = y1[inds1]
    
    inds2 = x2.argsort()
    y2 = y2[inds2]
    
    inds3 = x3.argsort()
    y3 = y3[inds3]
    
    inds4 = x4.argsort()
    y4 = y4[inds4]
    
    #Sorter xværdierne
    x1 = sorted(x1)
    x2 = sorted(x2)
    x3 = sorted(x3)
    x4 = sorted(x4)
    
    #En debug til at se, om listerne bleve sorteret, skal fjernes i det endelige program.
    #print(x1)
    #print(y1)
    
    #print(x2)
    #print(y2)

    #print(x3)
    #print(y3)

    #print(x4)
    #print(y4)
    
    #Følgende skal plotte de sorterede datapunkter
    
    #De forskellige plots med labels
    plt.plot(x1, y1, label="1. Salmonella enterica", linewidth = 3.5)
    plt.plot(x2, y2, label="2. Bacillus cereus", linewidth = 3.5)
    plt.plot(x3, y3, label="3. Listeria", linewidth = 3.5)
    plt.plot(x4, y4, label="4. Brochothrix thermosphacta", linewidth = 3.5)
    
    #Plot title
    plt.title("Growth Rate by Temperature")
    
    #Placeringen af 'legend' i plottet 
    plt.legend(loc="upper left", bbox_to_anchor=(1.02, 1), labelspacing = 3.95, prop = {'size': 12}, fancybox = True)
   
    #Akselabels
    plt.xlabel('Temperature')
    plt.ylabel('Growth Rate')
    
    
    #Limits på plottet
    plt.xlim([10, 60])
    plt.ylim(ymin=0)
    
    #Viser grafen. 
    plt.show()    
    