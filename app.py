import pandas as pd

def group_duplicate_columns(df):
    grouped_columns = {}

    for index in range(len(df)):
        obj = {}

        for col in df.columns:
            obj[col] = df.loc[index, col]

        if(df.loc[index,"Employee ID"] not in grouped_columns):
            grouped_columns[df.loc[index, 'Employee ID']] = obj
        elif (df.loc[index, 'Employee ID'] in grouped_columns):
            if("variants" not in grouped_columns[df.loc[index, 'Employee ID']]):
                grouped_columns[df.loc[index, 'Employee ID']].update({"variants":[]})
            
            grouped_columns[df.loc[index, 'Employee ID']]["variants"].append(obj)

    return grouped_columns

users = pd.read_excel("Users.xlsx", engine='openpyxl')

grouped_df = group_duplicate_columns(users)


print(" Grouped DF: ",grouped_df)

# dataframe =   {
#     1: {'Employee ID': 1, 'Name': 'Raj Verma', 'Age': 27, 'Date Of Birth': datetime.datetime(1998, 3, 13, 0, 0), 'Email Id': 'Raj@gmail.com', 'Mobile Number': 9999999999}, 
#     2: {'Employee ID': 2, 'Name': 'Ajay Singh', 'Age': 25, 'Date Of Birth': datetime.datetime(1989, 11, 9, 0, 0), 'Email Id': 'Ajay@gmail.com', 'Mobile Number': 8999999990},
#     3: {'Employee ID': 3, 'Name': 'Satyam Rai', 'Age': 19, 'Date Of Birth': datetime.datetime(2003, 1, 3, 0, 0), 'Email Id': 'Satyam@gmail.com', 'Mobile Number': 7999999991}, 
#     4: {'Employee ID': 4, 'Name': 'Mamta Nishad', 'Age': 23, 'Date Of Birth': datetime.datetime(2000, 9, 5, 0, 0), 'Email Id': 'Mamta@gmail.com', 'Mobile Number': 6399999992}, 
#     5: {'Employee ID': 5, 'Name': 'Manoj Yadav', 'Age': 26, 'Date Of Birth': datetime.datetime(1996, 5, 2, 0, 0), 'Email Id': 'Manoj@gmail.com', 'Mobile Number': 6345991233}, 
#     6: {'Employee ID': 6, 'Name': 'Astha Verma', 'Age': 22, 'Date Of Birth': datetime.datetime(2001, 4, 21, 0, 0), 'Email Id': 'Astha@gmail.com', 'Mobile Number': 8345021233},
#     7: {'Employee ID': 7, 'Name': 'John Doe', 'Age': 36, 'Date Of Birth': datetime.datetime(1997, 6, 27, 0, 0), 'Email Id': 'John@gmail.com', 'Mobile Number': 9245021299}, 
#     8: {'Employee ID': 8, 'Name': 'Rafeh Qazi', 'Age': 32, 'Date Of Birth': datetime.datetime(1987, 3, 31, 0, 0), 'Email Id': 'Rafeh@gmail.com', 'Mobile Number': 9945021239}, 
#     9: {'Employee ID': 9, 'Name': 'Corey Schefer', 'Age': 49, 'Date Of Birth': datetime.datetime(1979, 7, 23, 0, 0), 'Email Id': 'Corey@gmail.com', 'Mobile Number': 9545021232}, 
#     10: {
#         'Employee ID': 10, 
#         'Name': 'Dennis Ivy', 
#         'Age': 37, 
#         'Date Of Birth': '29-02-1969', 
#         'Email Id': 'Dennis@gmail.com', 
#         'Mobile Number': 8745021233, 
#         'variants': [
#                         {'Employee ID': 10, 'Name': 'Kishor Kumar', 'Age': 78, 'Date Of Birth': datetime.datetime(1956, 1, 22, 0, 0), 'Email Id': 'kishor@gmail.com', 'Mobile Number': 8145021233}, 
#                         {'Employee ID': 10, 'Name': 'Akhil Verma', 'Age': 27, 'Date Of Birth': datetime.datetime(2001, 11, 17, 0, 0), 'Email Id': 'akhil@gmail.com', 'Mobile Number': 634502167}
#             ]
#         }
# }
