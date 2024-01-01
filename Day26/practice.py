# number = "angela"

# new_list = [ n for n in number]
# print(new_list)


# range_list = [num *2 for num in range(1,5)]
# print(range_list)




# with open ("file1.txt" , "r") as file_1:
#     file1 = file_1.readlines()
# file1 =int(file1)





# with open ("file2.txt" , "r") as file_1:
#     file2 = file_1.readlines()
# file2 =int(file2)

# file3 = file_1 + file2







# result = [n for n in file1 and file2]                   

# # Write your code above 👆

# print(result)
# import random


# sentence = "What is the Airspeed Velocity of an Unladen Swallow?"
# # Don't change code above 👆

# # Write your code below:

# words = sentence.split()


# dict = {word:len(word) for word in words }
# print(dict)

# # print(result)

weather_c = {
    "Monday": 12,
    "Tuesday": 14,
    "Wednesday": 15,
    "Thursday": 14,
    "Friday": 21,
    "Saturday": 22,
    "Sunday": 24,
}
# 🚨 Don't change code above 👆


# Write your code 👇 below:

# weather_f = {day:(degree*9/5)+ 32 for (day, degree) in weather_c.items()}

# print(weather_f)
import pandas as pd

data = {
    "name": ["jai", "ayush", "suresh", "maya"],
    "number": [69, 76, 72, 93]
}

student_df = pd.DataFrame(data)

for (index,row) in student_df.iterrows():
    print(row["name"])

# You can display the DataFrame

# print(student_df)   

