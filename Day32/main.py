# import datetime
# import random
# import smtplib
# from email.mime.text import MIMEText

# def qoutes():
#     with open(r"Day32\quotes.txt", 'r', encoding="utf-8") as file:
#         # Read the entire contents of the file
#         file_contents = file.readlines()
#         # Return a random quote from the file
#         return random.choice(file_contents)

# def check_wed():
#     now = datetime.datetime.now()
#     weekday = now.weekday()
#     return weekday == 2

# if check_wed():
#     message = qoutes()

#     my_gmail = "jaipathak1972@gmail.com"
#     password = "kzzqaavynvrrgiyg"

#     reciver_mail = "jaipathak1978@gmail.com"

#     # Create a MIMEText message with UTF-8 encoding
#     msg = MIMEText(message, 'plain', 'utf-8')
#     msg = str(msg)
#     try:
#         # Connect to the SMTP server and send the email
#         connection = smtplib.SMTP("smtp.gmail.com", 587)
#         connection.starttls()
#         connection.login(my_gmail, password)
#         connection.sendmail(my_gmail, reciver_mail, msg)
#         connection.close()
#         print(f"Email has been sent to {reciver_mail}")
#     except Exception as e:
#         print(f"An error occurred: {str(e)}")



l=[]
def convert(b):
    if(b==0):
        return l
    dig=b%2
    l.append(dig)
    convert(b//2)
convert(6)
l.reverse()
for i in l:
    print(i,end="")

