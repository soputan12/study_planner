import pandas as pd 
import numpy as np

def sp51_availability(df): # creates a list for sp51 2023 availability
    sp51_23_availability = df.loc[:, "sp51_23"] #pandas magic, returns the sp51_23 row
    sp51_23_list = [] # list to add the sp51_23 stuff into a list
    for i in sp51_23_availability: # loop to add all the stuff into list
        if i == 1:
            sp51_23_list.append(1)
        else:
            sp51_23_list.append(0)
    return sp51_23_list

def create_subject_list(df): # creates a list with subject codes for indexing
    subject_list = []
    subjects = df.loc[:, "subject_code"] # returns the stuff in subject_code
    for i in subjects: # adds all subject codes into a list
        subject_list.append(i)
    return subject_list

def get_sp51_23_subjects(subject_counter, row_counter, subject_list, sp51_23_list, taken_subject_list, current_sp_subjects): # function to get sp51 2023 subjects
    while subject_counter < 4: # end condition for loop
        current_subject = str(subject_list[row_counter])
        if current_subject in taken_subject_list: # checks if current subjected has already been taken
            row_counter += 1
            continue
        else:
            if sp51_23_list[row_counter] == 1: # if there is 1 in the specific cell
                check = check_prerequisites(current_subject, taken_subject_list)
                if check == True:
                    current_sp_subjects.append(current_subject)
                    subject_counter += 1
                    row_counter += 1
                elif check == False:
                    row_counter += 1
                    continue
                else:
                    current_sp_subjects.append(current_subject) # add to taken subject list
                    subject_counter += 1 # increase counter by 1
                    row_counter += 1
            else:
                row_counter += 1 # if 0 skip to next row
    return current_sp_subjects

def check_prerequisites(current_subject, taken_subject_list): # function to check prerequisites, only checking for CP1401 atm
    if current_subject == "CP1404":
        if "CP1401" in taken_subject_list:
            return True
        else:
            return False
    else:
        return "skip"

def sp52_availability(df): # creates a list for sp51 2023 availability
    sp52_23_availability = df.loc[:, "sp52_23"] #pandas magic, returns the sp51_23 row
    sp52_23_list = [] # list to add the sp51_23 stuff into a list
    for i in sp52_23_availability: # loop to add all the stuff into list
        if i == 1:
            sp52_23_list.append(1)
        else:
            sp52_23_list.append(0)
    return sp52_23_list

def get_sp52_23_subjects(subject_counter, row_counter, subject_list, sp52_23_list, taken_subject_list, current_sp_subjects): # function to get sp51 2023 subjects
    while subject_counter < 4: # end condition for loop
        current_subject = str(subject_list[row_counter])
        if current_subject in taken_subject_list: # checks if current subjected has already been taken
            row_counter += 1
            continue
        else:
            if sp52_23_list[row_counter] == 1: # if there is 1 in the specific cell
                if current_subject == "CP1404":
                    if "CP1401" in taken_subject_list:
                        current_sp_subjects.append(current_subject)
                        subject_counter += 1
                        row_counter += 1
                    else:
                        row_counter += 1
                        pass
                else:
                    current_sp_subjects.append(current_subject) # add to taken subject list
                    subject_counter += 1 # increase counter by 1
                    row_counter += 1
            else:
                row_counter += 1 # if 0 skip to next row
    return current_sp_subjects        

def main():
    data = pd.read_csv("subjects.csv")
    df = pd.DataFrame(data, columns=['subject_code', 'prerequisites', 'sp51_23', 'sp52_23', 'sp53_23', 'sp51_24', 'sp52_24', 'sp53_24'])
    subject_counter = 0 # how many subjects you're taking for 1 study period
    taken_subject_list = [] # subjects taken already
    study_period = 2 # which study period
    credit_point = 0
    row_counter = 0
    current_sp_subjects = [] # subjects your taking in this sp
    #if counter  [10]: SPECIAL CHECK FOR CREDIT POINT ROWS 
        #if row[1] in taken_subject_list and credit_point >= 12:

    # index = ['CP1401', 'CP1402', 'CP1404', 'CP1406', 'MA1000', 'MA1020', 'MA1580', 'CP1409', 'CP1410', 'CP2403', 'CP2404', 'CP2406', 'CP2409', 'CP2421', 'CP2422', 'CP2423', 'CP2424', 'CP3403', 'CP3405', 'CP3406', 'CP3407', 'CP3414', 'CP3415', 'CP3416', 'CP3417', 'CP3418']
    # df.index = index
    # print(df)

    sp51_23_list = sp51_availability(df)
    subject_list = create_subject_list(df)
    """ TODO: change subject checker to class in future """
    sp51_subjects = get_sp51_23_subjects(subject_counter, row_counter, subject_list, sp51_23_list, taken_subject_list, current_sp_subjects)
    taken_subject_list.append(sp51_subjects)
    #sp52_23_list = sp51_availability(df)
    print(taken_subject_list)



main()              