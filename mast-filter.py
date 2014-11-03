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

Big thanks to Masahide Kanzaki who took RFC 2445 and made it accessible to humans
at his site.
http://www.kanzaki.com/docs/ical/

Additional thanks to the maintainers of Python documentation. 
https://docs.python.org/2/library/email-examples.html 
'''


import smtplib
import time
import socket
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText



# me == my email address
# you == recipient's email address
me = "SomeGuy@oregonstate.edu"
you = "burleigb@engr.oregonstate.edu"

# Create message container - the correct MIME type is (maybe?) multipart/alternative 
msg = MIMEMultipart('alternative')
msg['Subject'] = "Link"
msg['From'] = me
msg['To'] = you

now = time.localtime()

timecreated = time.strftime('%Y%m%dT%H%M%SZ', time.gmtime())
timestart = time.strftime('%Y%m%dT%H%M%S', now)
timeend = time.strftime('%Y%m%dT', now) + str(now.tm_hour + 1) + time.strftime('%M%S', now)
uid = timecreated + "@" + socket.gethostname()

# Create the body of the message
text = "Here is where we can include the original text of the email if we want to."

'''
The following date-time attributes must be UTC:
    CREATED
    DTSTAMP
    LAST-MODIFIED

The UID attribute must be globally unique in the calendar system
'''

calReq = """\
BEGIN:VCALENDAR
METHOD:REQUEST
PRODID:MAST
VERSION:2.0
BEGIN:VEVENT
CREATED:%s
DTSTAMP:%s
DTSTART:%s
DTEND:%s
LAST-MODIFIED:%s
SUMMARY:EECS Advising Session
UID:%s
DESCRIPTION:learn some stuff
SEQUENCE:0
STATUS:CONFIRMED
TRANSP:OPAQUE
END:VEVENT
END:VCALENDAR
""" % (timecreated, timecreated, timestart, timeend, timecreated, uid)

# Record the MIME types of both parts - text/plain and text/calendar.
part1 = MIMEText(text, 'plain')
part2 = MIMEText(calReq, 'calendar')
part2.add_header('Content-Disposition', 'attachment', method='REQUEST')

# Attach parts into message container.
msg.attach(part1)
msg.attach(part2)

# Send the message via local SMTP server.
s = smtplib.SMTP('mail.engr.oregonstate.edu')
s.sendmail(me, you, msg.as_string())
s.quit()
