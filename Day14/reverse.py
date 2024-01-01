user= input("Enter number to check if it a paradone or not")
mid = len(user)/2
mid = int(mid)
reversed_user = user[::-1]



if user == reversed_user:
    print("its a paradon")
        
else:
    print("nothing")
        
    