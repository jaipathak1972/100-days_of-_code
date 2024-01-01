import pandas
import smtplib
import datetime
import random

# 1. Update the birthdays.csv
data = pandas.read_csv("Day32/birthday_wisher/birthdays.csv")
letter_list = [r'Day32\birthday_wisher\letter_templates\letter_1.txt',
               r'Day32\birthday_wisher\letter_templates\letter_2.txt',
               r'Day32\birthday_wisher\letter_templates\letter_3.txt']

# Iterate through each row in the CSV
for index, row in data.iterrows():
    name = row['name']
    email = row['email']
    year = row['year']
    month = row['month']
    day = row['day']

    # 2. Check if today matches the current individual's birthday
    def check_birthday():
        now = datetime.datetime.now()
        today_month = now.month
        today_day = now.day
        return int(today_month) == int(month) and int(today_day) == int(day)

    # 3. If step 2 is true, pick a random letter from letter templates and replace the [NAME] with the person's actual name
    if check_birthday():
        with open(random.choice(letter_list), 'r') as letter_file:
            bday_letter = letter_file.read()
            bday_letter = bday_letter.replace('[NAME]', name)

        # Add a subject to the email
        subject = "Happy Birthday Wishes"

        # 4. Send the letter generated in step 3 to that person's email address.
        my_gmail = "jaipathak1972@gmail.com"
        password = "kzzqaavynvrrgiyg"
        receiver_mail = email  # Use the recipient's email from the CSV
        try:
            connection = smtplib.SMTP("smtp.gmail.com", 587)
            connection.starttls()
            connection.login(my_gmail, password)

            # Construct the email message with subject
            email_message = f"Subject: {subject}\n\n{bday_letter}"

            connection.sendmail(my_gmail, receiver_mail, email_message)
            connection.close()
            print(f"Birthday email sent to {name} at {email}")
        except Exception as e:
            print(f"Error happened: {str(e)}")
