from email.MIMEMultipart import MIMEMultipart
from email.MIMEText import MIMEText
from email.MIMEImage import MIMEImage
import smtplib

FROM = "kangk@onid.oregonstate.edu"
TO = "kangkabir@gmail.com"
msg = MIMEMultipart()
msg.attach(MIMEText(file("text.txt").read()))
mailer = smtplib.SMTP('mail.engr.oregonstate.edu')
mailer.ehlo()
mailer.starttls()
mailer.login('kangkabir@gmail.com','SPaP1903')
mailer.sendmail(msg['From'], msg['To'], msg.as_string())
mailer.close()
