# def compute(num):
#     if num == 1:
#         return 1
#     else:
#         # apple = (num + compute(num-1))
#         # print(apple)

#         return (num + compute(num-1))

# last = 3

# sum = compute(last)
# print(sum)

last = 4
sum = 0  
for i in range(last+1):  
    sum += i  # Add 'i' to the sum

print(sum)

# print(string)