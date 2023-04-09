import pandas as pd 
import numpy as np


data = pd.read_csv("subjects.csv")
df = pd.DataFrame(data, columns=['subject_code', 'prerequisites', 'sp51_23', 'sp52_23', 'sp53_23', 'sp51_24', 'sp52_24', 'sp53_24'])
subject_counter = 0 # how many subjects you're taking for 1 study period
taken_subject_list = [] # subjects taken already
study_period = 2 # which study period
credit_point = 0
row_counter = 0
#if counter  [10]: SPECIAL CHECK FOR CREDIT POINT ROWS 
    #if row[1] in taken_subject_list and credit_point >= 12:

# index = ['CP1401', 'CP1402', 'CP1404', 'CP1406', 'MA1000', 'MA1020', 'MA1580', 'CP1409', 'CP1410', 'CP2403', 'CP2404', 'CP2406', 'CP2409', 'CP2421', 'CP2422', 'CP2423', 'CP2424', 'CP3403', 'CP3405', 'CP3406', 'CP3407', 'CP3414', 'CP3415', 'CP3416', 'CP3417', 'CP3418']
# df.index = index
# print(df)
test = df.loc[:, "sp51_23"] #pandas magic, returns the sp51_23 row
test_list = [] # list to add the sp51_23 stuff into a list
for i in test: # loop to add all the stuff into list
    if i == 1:
        test_list.append(1)
    else:
        test_list.append(9)
print(len(test_list))

subject_list = [] 
taken_list = [] # subjects your taking in this sp
subjects = df.loc[:, "subject_code"] # returns the stuff in subject_code
for i in subjects: # adds all subject codes into a list
    subject_list.append(i)
print(len(subject_list))
while subject_counter < 4: # end condition for loop
    if test_list[row_counter] == 1: # if there is 1 in the specific cell
        taken_list.append(subject_list[row_counter]) # add to taken subject list
        subject_counter += 1 # increase counter by 1
        row_counter += 1
print(taken_list)

# while subject_counter <= 4:
#     print("while loop works")
#     for row in df:
#         print("row for loop works")        if row_counter == 0:
#             pass
#         # if row[0] not in taken_subject_list: # check whether subject has been taken before
#         #     print("subject code loop")
#         #     if row[study_period] == True: # check whether its available
#         #         print("study period check")
#         #         if row[1] in taken_subject_list: # check prerequisites
#         #             taken_subject_list.append(row[subject_counter])
#         #             subject_counter += 1
#         #             row_counter += 1
#         #             print("added to list")
# else:
#     print("done!")
#     print(taken_subject_list)
                    