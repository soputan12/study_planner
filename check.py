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

print(df.iloc[1])

# while subject_counter <= 4:
#     print("while loop works")
#     for row in df:
#         print("row for loop works")
#         if row_counter == 0:
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
                    