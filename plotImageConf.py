# -*- coding: utf-8 -*-
"""
Created on Thu Jun 14 11:03:35 2018

@author: Ditlev
"""
from userInput import userInputMenu;
from userInput import userInputNumber;
import numpy as np;
import os;
from dataLoad import dataLoad;
from Statistik import dataStatistics;

regular_temp_range = np.array([10,60]);
chosen_bacteria = np.arange(1,5);
growth_range = np.array([0,1000000000]);

def plotImageConf():
    
    import time;
    
    
    while True:
        try:
            del ch;
            print();
            print('Better try again');
            print('You done diddely goofed it up');
            print();
        except UnboundLocalError:
            print();
            print('Welcome');
            print('You done diddely goofed it up');
            print();
            
        ch = userInputMenu(np.array(['Always','Never','Only the relevant bacteria','Only the temperature and growth-range']),'Is it possible to filter data before loading the data file?');
    
        if ch == 2:
            print();
            print('Alright, keep going...');
            ch = userInputMenu(np.array(['Anders','Ditlev','Lasse']),'Who is the tallest of the creators of this program?');
            
            if ch == 2:
                print();
                print('Alright, keep going...');
                ch = userInputMenu(np.array(['15.42 km','10000 chains','2e+14 nanometer','220 American football fields','6.52e-15 parasec']),'How much is 100 furlongs?');
                
                if ch == 4:
                    print();
                    print('Alright, keep going...');
                    ch = userInputMenu(np.array(['Drake','Beoynce & Jay Z','Roy Wood$','Frank Ocean','Reo Cragun']),'What concert am I going to tonight?');
                    
                    if ch == 3:
                        print();
                        print('Alright, keep going...');
                        ch = userInputMenu(np.array(['The Milky Way','The Large Magellanic Cloud','NGC 2787','Messier 83',"Bode's Galaxy"]),'Which of the above is a spiral galaxy?');
                        
                        if ch == 5:
                            print();
                            print('Alright, keep going...');
                            userInputMenu(np.array(['Yes']),'For this next question, you have 10 seconds to answer. Are you ready?');
                            print();
                            time_start = time.perf_counter();
                            ch = userInputMenu(np.array(['A mouse','An elephant','This annoying quiz']),'Which is the largest?');
                            time_used = time.perf_counter() - time_start;
                            
                            if (ch == 3) and (time_used <= 10):
                                print();
                                print('Alright, keep going...');
                                userInputMenu(np.array(['Yes']),'You have 10 seconds to answer. Are you ready?');
                                print();
                                time_start = time.perf_counter();
                                ch = userInputMenu(np.array(['The Inflation Period','The Planck Time','Hawking Radiation','Dark Matter','String Theory']),'What theory solves the fact that two locations outside eachothers cosmic lighthorizon is isotropic?');
                                time_used = time.perf_counter() - time_start;
                                
                                if (ch == 1) and (time_used <= 10):
                                    print();
                                    print('Alright, keep going...');
                                    userInputMenu(np.array(['Yes']),'You have 8 seconds to answer. Are you ready?');
                                    print();
                                    time_start = time.perf_counter();
                                    ch = userInputMenu(np.array(['Bring Real Book','Be Right Back','Bollocks, Rude Boy','Boy, Remember Boltzmann']),'What does the abbreviation brb mean?');
                                    time_used = time.perf_counter() - time_start;    
                                    
                                    if (ch == 4) and (time_used <= 8):
                                        print();
                                        print('Alright, keep going...');
                                        file_list_q = np.asarray(os.listdir());
                                        while True:
                                            file_choice_q = userInputMenu(file_list_q,'Select the data-file you want to use for the next question');
                                            
                                            #Success
                                            try:
                                                data_matrix_q = dataLoad(file_list_q[int(file_choice_q) - 1],regular_temp_range,chosen_bacteria,growth_range);
                                                print();
                                                print('Data has now been read. Aforementioned faulty lines are not included.');
                                                print();
                                                print();
                                                break;
                                               
                                            # Fejlkoder
                                            except:
                                                print();
                                                print('Invalid file. Please try again');
                                                print();
                                        
                                        
                                        userInputMenu(np.array(['Yes']),'You have 8 seconds to answer. Are you ready?');
                                        print();
                                        time_start = time.perf_counter();
                                        ch = userInputNumber('What is the number of valid rows in the data-set?',np.array([False,False]));
                                        time_used = time.perf_counter() - time_start;
                                        
                                        rows = dataStatistics(data_matrix_q, "Rows")
                                        nm ='';
                                        
                                        for i in range(len(rows)):
                                            try:
                                                int(rows[i]);
                                                nm = ''.join((nm,rows[i]));
                                            except ValueError:
                                                ##nothing
                                                something = 'has to happen';
                                        
                                        row_check = int(nm);
                                        
                                        if ch == row_check and (time_used <= 8):
                                            
                                            ch = userInputMenu(np.array(['Yes','No']),'Do you want to escape the quiz?');
                                            
                                            if ch == 2:
                                                print();
                                                print('Alright, last question...')
                                                userInputMenu(np.array(['Yes']),'You have 3 seconds to answer. Are you ready?');
                                                print();
                                                time_start = time.perf_counter();
                                                ch = userInputNumber('What is the sum of cosinus squared and sinus squared?',np.array([False,False]));
                                                time_used = time.perf_counter() - time_start;
                                                
                                                if (int(ch) == 1) and (time_used <= 3.5):
                                                    print();
                                                    print('Please select at least one bacteria type.');
                                                    break;
                               
                                
        print();
        print('Oh no...')
        