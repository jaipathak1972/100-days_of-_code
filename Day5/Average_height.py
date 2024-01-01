# 🚨 Don't change the code below 👇
student_heights = input("Input a list of student heights ").split()
# for n in range(0, len(student_heights)):
#   student_heights[n] = int(student_heights[n])
  
# 🚨 Don't change the code above 👆


#Write your code below this row 👇


student_height = 0
for hight in student_heights:
  student_height += int(hight)
# print(student_height)


student_number = 0
for number in student_heights:
  student_number += 1

average = round(student_height / student_number)

print(average)
