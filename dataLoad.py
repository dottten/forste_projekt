# -*- coding: utf-8 -*-
"""
Created on Tue Jun 12 11:53:39 2018

@author: loved
"""

import numpy as np;

#dataLoad er en funktion, som henter en txt-fil, hvorpå data er indskrevet med mellemrum og linebreak.
    #Den konverterer hver gyldig (eller relevant) linje til en array og stacker dem til en matrix.
    #outputtet er en N x 3 matrix, hvor N er antallet af gyldige/relevante linjer.
#input:    
    #filename er en string med filnavnet på filen der skal behandles.
    #temprange er et NumPy array med den laveste og højeste temp i den rækkefølge.
    #bacteria er et NumPy array med de relevante bakterier (1,2,3,4).
    #growth er et NumPy array med et grow-rate-interval fra mindst til højest.
def dataLoad(filename,temprange,bacteria,growth):
    
    #brug kun relevante bakterier
    bacteria = bacteria[bacteria != 0];
    
    #indlæs filen og lav string
    filein = open(filename,"r");
    lines = filein.readlines();
    txt = "".join(lines);
    
    #til fejlstreng
    lineno = 0;
    errorstring = '';
    
    #behandling af data-fil ('txt').
    for i in range(len(txt)):
        
        
        #check hvorvidt det i'de element er et tal
        try:
            
            isinstance(int(txt[i]),int)
           
            #tilføj det til string
            try:
                number = ''.join((number,txt[i]));
            
            #skab string hvis den ikke eksisterer
            except NameError:
                number = txt[i];
        
        #hvis det i'de element ikke er et tal
        except ValueError:
            
            #tilføj også punktummet til tallet
            if txt[i] == '.':
                
                number = ''.join((number,txt[i]));
                
            #tilføj også minusset til tallet
            elif txt[i] == '-':
                
                number = txt[i];
                
            #Når tallet er afsluttet
            elif (txt[i]) == ' ':
                
                #return number;
                try:
                    row = np.insert(row , np.size(row) , float(number));
                
                except NameError:
                    row = np.array([float(number)]);
                
                del number;
            
            #når tal og linje er afsluttet
            elif (txt[i] == '\n') :
                
                lineno = lineno + 1;
                row = np.insert(row , np.size(row) , int(number));
                
                del number;
                
                #konstruer specificeret errorstring
                count = 0;
                
                if (row[0] > temprange[1]):
                    errorstring = ''.join((errorstring,'Temperature is over {:.2f} degrees in line {:d}. '.format(temprange[1],lineno)));
                if (row[0] < temprange[0]):
                    errorstring = ''.join((errorstring,'Temperature is under {:.2f} degrees in line {:d}. '.format(temprange[0],lineno)));
                    
                if (row[1] < growth[0]):
                    errorstring = ''.join((errorstring,'Growth-rate is lower than {:.2f} in line {:d}. '.format(growth[0],lineno)));
                if (row[1] > growth[1]):
                    errorstring = ''.join((errorstring,'Growth-rate is larger than {:.2f} in line {:d}. '.format(growth[1],lineno)));
                    
                if (row[2] < 1) or (row[2] > 4):
                    errorstring = ''.join((errorstring,'Bacteria not defined in line {:d}. '.format(lineno)));
                    count = -1;
                for i in range(np.size(bacteria)):
                    if (row[2] != bacteria[i]):
                        count = count + 1;
                    if count == np.size(bacteria):
                        errorstring = ''.join((errorstring,'Bacteria not chosen in line {:d}. '.format(lineno)));
                    
                if np.size(row) != 3:
                    errorstring = ''.join((errorstring,'The amount of elements in line {:d} is out bounds. '.format(lineno)));
                
                #test hvorvidt temperaturen og growth-raten i rækken er i det specificerede interval.
                if (row[0] <= temprange[1]) and (row[0] >= temprange[0]) and (row[1] <= growth[1]) and (row[1] >= growth[0]) and (row[1] > 0) and np.size(row) == 3:
                    
                    #test hvorvidt bakterien i rækkenen er specificeret
                    for i in range(np.size(bacteria)):
                        
                        if (row[2] == bacteria[i]):
                            
                            #hvis alt er tilfældet, stackes rækken nederst på data-matricen
                            try:
                                data = np.vstack((data,row))
                                
                            except NameError:
                                data = np.copy(row);
                                
                    del row;
                    
                else:
                    del row;
    
    print();
    print('Data has been succesfully loaded.');
    print();
    print('The following lines of the data-file has not been included:');        
    print(errorstring);
    return data