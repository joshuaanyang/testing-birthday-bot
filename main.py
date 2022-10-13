import pandas
import random
import smtplib
import datetime as dt

now = dt.datetime.now()
month = now.month
day = now.day

email = "your_email_where_the_birthday_message_will_be_sent_from"
password = ""

new_dict = []

birthday_data = pandas.read_csv("birthdays.csv")
for (index, row) in birthday_data.iterrows():
    if row["month"] == month and row["day"] == day:
        new_dict.append({row["month"]: [row["name"], row["email"]]})

for x in new_dict:
    celebrant_name = x[month][0]
    celebrant_email = x[month][1]

    letter_list = ["letter_templates/letter_1.txt", "letter_templates/letter_2.txt", "letter_templates/letter_3.txt"]

    with open(random.choice(letter_list)) as letter_doc:
        letter_content = letter_doc.read()
        message = letter_content.replace("[NAME]", celebrant_name)

    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=email, password=password)
        connection.sendmail(from_addr=email, to_addrs=celebrant_email, msg=f"Subject: Happy Birthday\n\n{message}")
