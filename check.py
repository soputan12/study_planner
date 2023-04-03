import pandas as pd
import numpy as np


df = pd.read_csv("subjects.csv")
subject_counter = 0 # how many subjects you're taking for 1 study period
taken_subject_list = [] # subjects taken already
study_period = 2 # which study period
credit_point = 0
row_counter = 0
#if counter  [10]: SPECIAL CHECK FOR CREDIT POINT ROWS 
    #if row[1] in taken_subject_list and credit_point >= 12:

while subject_counter <= 4:
    for row in df:
        if row[0] not in taken_subject_list: # check whether subject has been taken before
            if row[study_period] == True: # check whether its available
                if row[1] in taken_subject_list: # check prerequisites
                    taken_subject_list.append(row[subject_counter])
                    subject_counter += 1
                    row_counter += 1
                    