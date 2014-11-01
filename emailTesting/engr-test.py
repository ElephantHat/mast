#!/usr/bin/env python

import smtplib

FROM = "test@onid.oregonstate.edu"
TO = ["bryonb@gmail.com"]

SUBJECT = "Hello!"

TEXT = "This message was sent with Python's smtplib."

message = """\
From: %s
To: %s
Subject: %s

%s
""" % (FROM, ", ".join(TO), SUBJECT, TEXT)

server = smtplib.SMTP("mail.engr.oregonstate.edu")
#server.ehlo()
#server.starttls()
#server.login('kangkabir@gmail.com','SPaP1903')
server.sendmail(FROM, TO, message)
server.close()
