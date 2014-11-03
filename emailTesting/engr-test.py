#!/usr/bin/env python

'''
This will successfully send an email via engr servers, but only if it is run 
ON an engr server. For example, you should not be able to successfuly run 
this script locally.
'''


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
server.sendmail(FROM, TO, message)
server.close()
