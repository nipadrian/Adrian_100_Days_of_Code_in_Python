import pandas as pd

import smtplib

MY_EMAIL = "adrian.nip@yahoo.com"
MY_PASSWORD = "ffasnfffqftiqrtu"
#
# with smtplib.SMTP("smtp.mail.yahoo.com") as connection:
#     connection.starttls()
#     connection.login(user=my_email, password=password)
#     connection.sendmail(from_addr=my_email,
#                         to_addrs= "nip.adrian@gmail.com",
#                         msg = "Subject: Hello\n\n This is the body of my email."
#                         )
# connection.close()


import datetime as dt
import random

now = dt.datetime.now()
year = now.year
weekday = now.weekday()

# date_of_birth = dt.datetime(year = 1993, month = 11, day = 13)
#
# print(date_of_birth)


# ---------------------------- Import Data ------------------------------- #

#quotes = pd.read_csv("/Birthday Wisher (Day 32) start/ quotes.txt")
quotes = []

with open("C:/Users/Adrian/PycharmProjects/day-32/Birthday Wisher (Day 32) start/quotes.txt") as f:
    for line in f:
        line = line.strip()
        if line:
            #print(line)
            quotes.append(line)

#print(quotes)

random_quote = random.randint(0,len(quotes))

if weekday == 2:
    print(quotes[random_quote])
    quote = quotes[random_quote]
    with smtplib.SMTP("smtp.mail.yahoo.com") as connection:
        connection.starttls()
        connection.login(MY_EMAIL, MY_PASSWORD)
        connection.sendmail(
            from_addr = MY_EMAIL,
            to_addrs = MY_EMAIL,
        msg = f"Subject:Monday Motivation \n\n {quote}"
        )