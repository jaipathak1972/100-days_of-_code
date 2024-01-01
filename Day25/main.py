import csv

with open("Day25/name_data.csv", mode= "r") as file_name:
    paraghaph=csv.reader(file_name)
    temp = []
    for row in paraghaph:
        temp.append(int(row[1]))

    print(temp)
    
# with open("Day25/name_file.csv", mode="w") as name_file:
#     # Join the lines into a single string
#     content =''.join(lines)
#     name_file.write(content)