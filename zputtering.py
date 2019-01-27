import smtplib

host = "smtp.gmail.com"
port = 587
user = "afordeal88@gmail.com"
password = "Olawale@1"
fromm = user
to = ["jessicahaze2017@gmail.com"]

email_com = smtplib.SMTP(host, port)
email_com.ehlo()
email_com.starttls()
email_com.login(user, password)
email_com.sendmail(fromm, to, "How are you buddy?")

