# -*- coding: utf-8 -*-
"""
Created on Wed Jun 13 10:59:12 2018

@author: ander
"""

import math
import numpy as np
import matplotlib.pyplot as plt

def numberOfBacteria(data):
    
    #Denne funktion skaber et søjlediagram ud fra bakterietyperne.
    #Input skal være en N x 3 matrix, hvor bakterietypen står i tredje søjle.
    #Den finder ud af hvilke unikke tal, altså bakterie typer, der er, og hvor mange gange de optræder. 
    #Derefter plotter funktionen det i søjlediagrammet. 

    #Hiver kolonnen med målingens bakterie nummer ud.
    BacNum = data[:, 2]
    
    #Gemmer hvilke unikke tal der er i en vektor i variablen 'unique' og,
    #Gemmer hvor mange instanser der er af hver enkelt unikt tal i en vektor i variablen 'counts'.
    unique, counts = np.unique(BacNum, return_counts=True)
    
    
    #Plotter nu søjlediagrammet med værdierne fra 'unique' og 'counts'. 
    plt.bar(unique, counts, width=1/2)
    plt.xlabel("Bacterial Serial Number")
    plt.ylabel("Bacterial count")
    
    #Følgende to linjer ænder aksernes intervaller til 'hele' spring.
    plt.xticks(np.arange(min(unique), max(unique)+1, 1.0))
    plt.yticks(np.arange(min(counts), max(counts)+1, 1.0))
    
    #Til sidst vises søjle diagrammet. 
    plt.show()