import pandas as pd 
import numpy as np

def sp51_availability(df):
    sp51_23_availability = df.loc[:, "sp51_23"] #pandas magic, returns the sp51_23 row
    sp51_23_list = [] # list to add the sp51_23 stuff into a list
    for i in sp51_23_availability: # loop to add all the stuff into list
        if i == 1:
            sp51_23_list.append(1)
        else:
            sp51_23_list.append(9)
    return sp51_23_list

def create_subject_list(df):
    subject_list = []
    subjects = df.loc[:, "subject_code"] # returns the stuff in subject_code
    for i in subjects: # adds all subject codes into a list
        subject_list.append(i)
    return subject_list

# def get_sp51_23_subjects(subject_counter, row_counter, subject_list, sp51_23_list, taken_subject_list):
#     current_sp_subjects = [] # subjects your taking in this sp
#     while subject_counter < 4: # end condition for loop
#         current_subject = str(subject_list[row_counter])
#         if current_subject in taken_subject_list:
#             row_counter += 1
#             pass
#         else:
#             if sp51_23_list[row_counter] == 1: # if there is 1 in the specific cell
#                 checked_subject = check_prerequisites(current_subject, taken_subject_list)
#                 if checked_subject == True:
#                     print("checking prerequisites")
#                     current_sp_subjects.append(current_subject) # add to taken subject list
#                     subject_counter += 1 # increase counter by 1
#                     row_counter += 1
#                 else:
#                     print("skip")
#                     row_counter += 1
#                     pass
#             else:
#                 row_counter += 1
#     return current_sp_subjects

def check_prerequisites(current_subject, taken_subject_list):
    if current_subject == "CP1404":
        print("1404 check")
        if "CP1401" in taken_subject_list:
            print("checked 1404")
            return True
        else:
            return False
        

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
    while subject_counter < 4: # end condition for loop
        current_subject = str(subject_list[row_counter])
        if current_subject in taken_subject_list:
            row_counter += 1
            continue
        else:
            if sp51_23_list[row_counter] == 1: # if there is 1 in the specific cell
                print(current_subject)
                if current_subject == "CP1404":
                    print("1404 check")
                    if "CP1401" in taken_subject_list:
                        print("checked 1404")
                        current_sp_subjects.append(current_subject)
                        subject_counter += 1
                        row_counter += 1
                    else:
                        print("skip")
                        row_counter += 1
                        pass
                else:
                    current_sp_subjects.append(current_subject) # add to taken subject list
                    subject_counter += 1 # increase counter by 1
                    row_counter += 1
            else:
                row_counter += 1 # if 0 skip to next row
    taken_subject_list.append(current_sp_subjects)
    # current_sp_subjects = get_sp51_23_subjects(subject_counter, row_counter, subject_list, sp51_23_list, taken_subject_list)
    print(current_sp_subjects)



main()              