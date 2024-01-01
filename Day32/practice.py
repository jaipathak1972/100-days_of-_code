# import smtplib
import pandas

# email = input("Sender email :")
# reciver = input("reciver email :")
# message = input("message :")
# password = "kzzqaavynvrrgiyg"


# connection = smtplib.SMTP("smtp.gmail.com", 587)
# connection.starttls()

# connection.login( email, password)
# connection.sendmail(email,reciver,message)
# connection.close

data = pandas.read_csv("Day32/birthday_wisher/birthdays.csv")
aaple = {(info['month'],info["day"] ): info   for numbers, info in data.iterrows()}
   
print(aaple)