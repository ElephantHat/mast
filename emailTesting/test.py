import smtplib

FROM = "kangk@onid.oregonstate.edu"
TO = ["kangkabir@gmail.com"]

SUBJECT = "Hello!"

TEXT = "This message was sent with Python's smtplib."

message = """\
From: %s
To: %s
Subject: %s

%s
""" % (FROM, ", ".join(TO), SUBJECT, TEXT)

server = smtplib.SMTP('smtp.gmail.com', 587)
server.ehlo()
server.starttls()
server.login('kangkabir@gmail.com','SPaP1903')
server.sendmail(FROM, TO, message)
server.close()
