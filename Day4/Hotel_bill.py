# Import the random module here
import random
# Split string method
names_string = input("Give me everybody's names, separated by a comma. ")
names = names_string.split(", ")
# 🚨 Don't change the code above 👆

x= len(names)

random_name= sorted(x)
Random_name = names[random_name] 

print(Random_name + " is going to buy the meal today!")
