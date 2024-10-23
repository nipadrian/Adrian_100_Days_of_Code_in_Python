import smtplib

# my_email = "adrian.nip@yahoo.com"
# password = "ffasnfffqftiqrtu"
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

now = dt.datetime.now()
year = now.year


date_of_birth = dt.datetime(year = 1993, month = 11, day = 13)

print(date_of_birth)