import pandas as pd 
import numpy as np

def check_prerequisites(current_subject, taken_subject_list, elective): # function to check prerequisites
    taken_subjects = str(taken_subject_list) # made life a bit easier by making this into a var
    credit_point = len(taken_subject_list) * 3 # calculate credit points: 1 subject = 3 credit points
    if current_subject == "CP1404":
        if "CP1401" in taken_subjects:
            return True
        else:
            return False
    elif current_subject == "MA1000":
        if "MA1020" in taken_subjects: # dont need to take if got MA1020 inside
            return False
    elif current_subject == "MA1020":
        if "MA1000" in taken_subjects: # dont need to take if got MA1000 inside
            return False
    elif current_subject == "MA1580":
        if "MA1000" or "MA1020" in taken_subjects:
            return True
        else:
            return False
    elif current_subject == "CP1410":
        if "CP1402" and "CP1409" in taken_subjects:
            return True
        else:
            return False
    elif current_subject == "CP2403":
        if credit_point >= 12:
            return True
        else:
            return False
    elif current_subject == "CP2406":
        if "CP1404" in taken_subjects:
            return True
        else:
            return False
    elif current_subject == "CP2409":
        if "CP1402" in taken_subjects:
            return True
        else:
            return False
    elif current_subject == "CP2421":
        if "CP1401" and "MA1580" in taken_subjects:
            return True
        else:
            return False
    elif current_subject == "CP2422":
        if "CP1401" in taken_subjects:
            return True
        else:
            return False
    elif current_subject == "CP2423":
        if "CP1401" and "CP1410" in taken_subjects:
            return True
        else:
            return False
    elif current_subject == "CP2424":
        if "CP1410" and credit_point >= 12:
            return True
        else:
            return False
    elif current_subject == "CP3403":
        if "CP2403" and "CP2404" in taken_subjects or credit_point >= 18:
            return True
        else:
            return False
    elif current_subject == "CP3405":
        if credit_point >= 18:
            return True
        else:
            return False
    elif current_subject == "CP3406":
        if "CP1404" in taken_subjects and credit_point >= 18:
            return True
        else:
            return False
    elif current_subject == "CP3407":
        if "CP1404" in taken_subjects and credit_point >= 18:
            return True
        else:
            return False
    elif current_subject == "CP3414":
        if "CP2422" and "CP2423" in taken_subjects:
            return True
        else:
            return False
    elif current_subject == "CP3415":
        if "CP2424" in taken_subjects:
            return True
        else:
            return False
    elif current_subject == "CP3416": # Behavioural Cybersecurity 
        if "CP3417" in taken_subjects: # Elective
            return False
        else:
            if credit_point >= 36:
                if elective == "CP3416" or elective == None:
                    return True
                else:
                    return False
            else:
                return False
    elif current_subject == "CP3417": # Operational Tech
        if "CP3416" in taken_subjects: # Elective
            return False
        else:
            if "CP2423" in taken_subjects:
                if elective == "CP3417" or elective == None:
                    return True
                else:
                    return False
            else:
                return False
    elif current_subject == "CP3418":
        if "CP3414" in taken_subjects:
            return True
        else:
            return False
    else:
        return "skip"

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

def get_sp51_23_subjects(subject_counter, row_counter, subject_list, sp51_23_list, taken_subject_list, current_sp_subjects, elective): # function to get sp51 2023 subjects
    while subject_counter < 4: # end condition for loop
        current_subject = str(subject_list[row_counter])
        if current_subject in str(taken_subject_list): # checks if current subjected has already been taken
            row_counter += 1
            continue
        else:
            if sp51_23_list[row_counter] == 1: # if there is 1 in the specific cell
                check = check_prerequisites(current_subject, taken_subject_list, elective)
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

def sp52_availability(df): 
    sp52_23_availability = df.loc[:, "sp52_23"] 
    sp52_23_list = [] 
    for i in sp52_23_availability: # loop to add all the stuff into list
        if i == 1:
            sp52_23_list.append(1)
        else:
            sp52_23_list.append(0)
    return sp52_23_list

def get_sp52_23_subjects(subject_counter, row_counter, subject_list, sp52_23_list, taken_subject_list, current_sp_subjects, elective): 
    current_sp_subjects = []
    try:
        while subject_counter < 4: # end condition for loop
            current_subject = str(subject_list[row_counter])
            if current_subject in str(taken_subject_list): # checks if current subjected has already been taken
                row_counter += 1
                continue
            else:
                if sp52_23_list[row_counter] == 1: # if there is 1 in the specific cell
                    check = check_prerequisites(current_subject, taken_subject_list, elective)
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
    except:
        return current_sp_subjects

def sp53_availability(df): 
    sp53_23_availability = df.loc[:, "sp53_23"] 
    sp53_23_list = [] 
    for i in sp53_23_availability: # loop to add all the stuff into list
        if i == 1:
            sp53_23_list.append(1)
        else:
            sp53_23_list.append(0)
    return sp53_23_list     

def get_sp53_23_subjects(subject_counter, row_counter, subject_list, sp53_23_list, taken_subject_list, current_sp_subjects, elective): 
    current_sp_subjects = []
    while subject_counter < 4: # end condition for loop
        current_subject = str(subject_list[row_counter])
        if current_subject in str(taken_subject_list): # checks if current subjected has already been taken
            row_counter += 1
            continue
        else:
            if sp53_23_list[row_counter] == 1: # if there is 1 in the specific cell
                check = check_prerequisites(current_subject, taken_subject_list, elective)
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

def sp51_24_availability(df): 
    sp51_24_availability = df.loc[:, "sp51_24"] 
    sp51_24_list = [] 
    for i in sp51_24_availability: # loop to add all the stuff into list
        if i == 1:
            sp51_24_list.append(1)
        else:
            sp51_24_list.append(0)
    return sp51_24_list     

def get_sp51_24_subjects(subject_counter, row_counter, subject_list, sp51_24_list, taken_subject_list, current_sp_subjects, elective): 
    current_sp_subjects = []
    try:
        while subject_counter < 4: # end condition for loop
            current_subject = str(subject_list[row_counter])
            if current_subject in str(taken_subject_list): # checks if current subjected has already been taken
                row_counter += 1
                continue
            else:
                if sp51_24_list[row_counter] == 1: # if there is 1 in the specific cell
                    check = check_prerequisites(current_subject, taken_subject_list, elective)
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
    except:
        return current_sp_subjects

def sp52_24_availability(df): 
    sp52_24_availability = df.loc[:, "sp52_24"] 
    sp52_24_list = [] 
    for i in sp52_24_availability: # loop to add all the stuff into list
        if i == 1:
            sp52_24_list.append(1)
        else:
            sp52_24_list.append(0)
    return sp52_24_list   

def get_sp52_24_subjects(subject_counter, row_counter, subject_list, sp52_24_list, taken_subject_list, current_sp_subjects, elective): 
    current_sp_subjects = []
    try:
        while subject_counter < 5: # end condition for loop
            current_subject = str(subject_list[row_counter])
            if current_subject in str(taken_subject_list): # checks if current subjected has already been taken
                row_counter += 1
                continue
            else:
                if sp52_24_list[row_counter] == 1: # if there is 1 in the specific cell
                    check = check_prerequisites(current_subject, taken_subject_list, elective)
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
    except:
        return current_sp_subjects

def sp53_24_availability(df): 
    sp53_24_availability = df.loc[:, "sp53_24"] 
    sp53_24_list = [] 
    for i in sp53_24_availability: # loop to add all the stuff into list
        if i == 1:
            sp53_24_list.append(1)
        else:
            sp53_24_list.append(0)
    return sp53_24_list   

def get_sp53_24_subjects(subject_counter, row_counter, subject_list, sp53_24_list, taken_subject_list, current_sp_subjects, elective): 
    current_sp_subjects = []
    while subject_counter < 4: # end condition for loop
        if row_counter == 26:
            break
        current_subject = str(subject_list[row_counter])
        if current_subject in str(taken_subject_list): # checks if current subjected has already been taken
            row_counter += 1
            continue
        else:
            if sp53_24_list[row_counter] == 1: # if there is 1 in the specific cell
                check = check_prerequisites(current_subject, taken_subject_list, elective)
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

def main(taken_subjects, electives):
    data = pd.read_csv("subjects.csv")
    df = pd.DataFrame(data, columns=['subject_code', 'prerequisites', 'sp51_23', 'sp52_23', 'sp53_23', 'sp51_24', 'sp52_24', 'sp53_24'])
    subject_counter = 0 # how many subjects you're taking for 1 study period
    taken_subject_list = taken_subjects # subjects taken already
    subject_timetable = []
    row_counter = 0
    current_sp_subjects = [] # subjects your taking in this sp
    elective = electives

    sp51_23_list = sp51_availability(df)
    subject_list = create_subject_list(df)
    sp51_subjects = get_sp51_23_subjects(subject_counter, row_counter, subject_list, sp51_23_list, taken_subject_list, current_sp_subjects, elective)
    taken_subject_list.extend(sp51_subjects)
    subject_timetable.append(sp51_subjects)
    sp52_23_list = sp52_availability(df)
    sp52_subjects = get_sp52_23_subjects(subject_counter, row_counter, subject_list, sp52_23_list, taken_subject_list, current_sp_subjects, elective)
    taken_subject_list.extend(sp52_subjects)
    subject_timetable.append(sp52_subjects)
    sp53_23_list = sp53_availability(df)
    sp53_subjects = get_sp53_23_subjects(subject_counter, row_counter, subject_list, sp53_23_list, taken_subject_list, current_sp_subjects, elective)
    taken_subject_list.extend(sp53_subjects)
    subject_timetable.append(sp53_subjects)
    sp51_24_list = sp51_24_availability(df)
    sp51_24_subjects = get_sp51_24_subjects(subject_counter, row_counter, subject_list, sp51_24_list, taken_subject_list, current_sp_subjects, elective)
    taken_subject_list.extend(sp51_24_subjects)
    subject_timetable.append(sp51_24_subjects)
    sp52_24_list = sp52_24_availability(df)
    sp52_24_subjects = get_sp52_24_subjects(subject_counter, row_counter, subject_list, sp52_24_list, taken_subject_list, current_sp_subjects, elective)
    taken_subject_list.extend(sp52_24_subjects)
    subject_timetable.append(sp51_24_subjects)
    sp53_24_list = sp53_24_availability(df)
    sp53_24_subjects = get_sp53_24_subjects(subject_counter, row_counter, subject_list, sp53_24_list, taken_subject_list, current_sp_subjects, elective)
    taken_subject_list.extend(sp53_24_subjects)
    subject_timetable.append(sp51_24_subjects)
    
    return subject_timetable


# main()              