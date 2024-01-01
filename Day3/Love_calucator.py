# 🚨 Don't change the code below 👇
print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

True_love='True_love'

combine= name1 + name2
combine = combine.lower()


t = combine.count("t")
r = combine.count("r")
u = combine.count("u")
e = combine.count("e")

true= t+r+u+e

l = combine.count("l")
o = combine.count("o")
v = combine.count("v")
e = combine.count("e")

love= l+o+v+e



percentage = int(str(true) + str(love))
print(percentage)



if 10 >= percentage or percentage >=90 :
     print(f"Your score is {percentage}, you go together like coke and mentos.")
elif 40 :
    print(f"Your score is {percentage}, you are alright together.")
else:
     print(f"Your score is {percentage}.")

