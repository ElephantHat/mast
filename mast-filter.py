''' 
Develop mast-filter here

Receives email body piped from procmail:

    Advising Signup with <advisor> <confirmed|CANCELLED>
    Name: <name>
    Email: <student email address>
    Date: <Day>, <Month><date><st|nd|rd|th>, <year>
    Time: 1:00pm - 1:15pm

Creates new email with attachment MIMETYPE "text/calendar; method=REQUEST;"

'''


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
