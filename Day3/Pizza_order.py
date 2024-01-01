# 🚨 Don't change the code below 👇
print("Welcome to Python Pizza Deliveries!")
size = input("What size pizza do you want? S, M, or L ").upper()
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

Output = int()

if size == "S":
   
    Output += 15
    add_pepperoni = input("Do you want pepperoni? Y or N ").upper()
    if add_pepperoni == "Y":
        Output += 2
        extra_cheese = input("Do you want extra cheese? Y or N ").upper()
        if extra_cheese == "Y":
            Output += 1
        
elif size == "M":
    add_pepperoni = input("Do you want pepperoni? Y or N ").upper()

    Output += 20
    if add_pepperoni == "Y":
        Output += 3

        extra_cheese = input("Do you want extra cheese? Y or N ").upper()

        
        if extra_cheese == "Y":
            Output += 1

elif size == "L":
    add_pepperoni = input("Do you want pepperoni? Y or N ").upper()

    Output += 25
    if add_pepperoni == "Y":
        Output += 3
        extra_cheese = input("Do you want extra cheese? Y or N ").upper()

        if extra_cheese == "Y":
            Output += 1

else:
    print("Wrong")

print(f"${Output}")


