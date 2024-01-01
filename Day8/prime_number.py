#Write your code below this line 👇

def prime_checker(number):
    if number < 2:
       print("its a prime number") 

    
    is_prime =True
    for i in range(2,number):
        if i % number == 0:
          is_prime =False
    
    if is_prime :
       print("its  prime")
    else:
       print("its not prime") 
      

    

       

#Write your code above this line 👆
    
#Do NOT change any of the code below👇
n = int(input("Check this number: "))
prime_checker(number=n)

