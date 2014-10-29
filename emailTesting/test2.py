from email.MIMEMultipart import MIMEMultipart
from email.MIMEText import MIMEText
from email.MIMEImage import MIMEImage
import smtplib

FROM = "me"
TO = "kangkabir@gmail.com"
msg = MIMEMultipart()
msg.attach(MIMEText(file("text.txt").read()))
mailer = smtplib.SMTP('smtp.gmail.com',587)
mailer.ehlo()
mailer.starttls()
mailer.login('kangkabir@gmail.com','SPaP1903')
mailer.sendmail(FROM,TO,msg.as_string())
mailer.close()
