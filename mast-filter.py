#!/usr/bin/env python
''' 
Receives email body piped from procmail:

    Advising Signup with <advisor> <confirmed|CANCELLED>
    Name: <name>
    Email: <student email address>
    Date: <Day>, <Month><date><st|nd|rd|th>, <year>
    Time: 1:00pm - 1:15pm

Creates new email with attachment MIMETYPE "text/calendar; method=<REQUEST|CANCEL>;"



This will successfully send an email via engr servers, but only if it is run 
ON an engr server. For example, you should not be able to successfuly run 
this script locally.

Big thanks to Masahide Kanzaki who took RFC 2445 and made it accessible to humans
at his site.
http://www.kanzaki.com/docs/ical/

Additional thanks to the maintainers of Python documentation. 
https://docs.python.org/2/library/email-examples.html 


TODO:
    Allow for appointment cancellation
    integrate database functionality
'''


import smtplib
import time
import socket
import fileinput
import string
import re
from pprint import pformat
from pprint import pprint
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

debugs = True

# Parse body of email
mailArray = []
for line in fileinput.input():
	mailArray.append(line.split())

id=mailArray[0][0]
body=[]

for i in range(3, len(mailArray)):
    if (len(mailArray[i+1])==0):
        mailArray[i+1].append("\n")

    if (mailArray[i+1][0]==id):
        break
    else:
        body.append(mailArray[i])
        print mailArray[i]

# Get email address from .mastrc
toAddys=[]
for line in fileinput.input(".mastrc"):
    toAddys.append(line.rstrip("\n"))

# Debugging stuff
if (debugs):
    f=open("./output.txt", "w")
    f.write(pformat(body))
    f.write(id)
    f.write("\n")
    f.write(pformat(toAddys))
    f.write("\n")
    f.close()



# me == my email address
# you == recipient's email address
me = "do.not.reply@oregonstate.edu"
you = "; ".join(toAddys)

# Create message container - the correct MIME type is multipart/alternative (maybe? it works, anyways)  
msg = MIMEMultipart('alternative')
msg['Subject'] = "New Advising Session"
msg['From'] = me
msg['To'] = you

# Start building attributes for calendar request object
timecreated = time.strftime('%Y%m%dT%H%M%SZ', time.gmtime())
uid = timecreated + "@" + socket.gethostname()

# Build the DTSTART and DTEND time objects
body[3][3]=re.sub(r'[a-z]', "", body[3][3])
date = " ".join(body[3][1:])
date=date.replace(",","")
dateStart = dateEnd = date

# DTSTART   
ampm=re.sub(r'[0-9]*:[0-9]*', '', body[4][1])
aptStartHr = re.sub(r':[0-9]*[A-z]*', '', body[4][1])
aptStartMin  = re.sub(r'[0-9]*:', '', body[4][1])
aptStartMin = re.sub(r'[A-z]*', '', aptStartMin)

if ampm.lower() == "pm":
    aptStartHr = str(int(aptStartHr) + 12)

dateStart+=" "+aptStartHr+" "+aptStartMin+" 00"
timestart = time.strftime('%Y%m%dT%H%M%S', time.strptime(dateStart, '%A %B %d %Y %H %M %S'))

# DTEND   
ampm=re.sub(r'[0-9]*:[0-9]*', '', body[4][3])
aptEndHr = re.sub(r':[0-9]*[A-z]*', '', body[4][3])
aptEndMin  = re.sub(r'[0-9]*:', '', body[4][3])
aptEndMin = re.sub(r'[A-z]*', '', aptEndMin)

if ampm.lower() == "pm":
    aptEndHr = str(int(aptEndHr) + 12)

dateEnd+=" "+aptEndHr+" "+aptEndMin+" 00"
print dateEnd
timeend = time.strftime('%Y%m%dT%H%M%S', time.strptime(dateEnd, '%A %B %d %Y %H %M %S'))



# Create the body of the message for the email, as well as the description in the calendar request
mimeText = ""
calText = ""
for x in body:
	mimeText += " ".join(x) + "\n"
	calText += " ".join(x) + "\\n" #Description of calReq needs escaped \n

'''
Below is the calendar request object

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
DESCRIPTION:%s
SEQUENCE:0
STATUS:CONFIRMED
TRANSP:OPAQUE
END:VEVENT
END:VCALENDAR
""" % (timecreated, timecreated, timestart, timeend, timecreated, uid, calText)


# Record the MIME types of both parts - text/plain and text/calendar.
part1 = MIMEText(mimeText, 'plain')
part2 = MIMEText(calReq, 'calendar')
part2.add_header('Content-Disposition', 'attachment', method='REQUEST')

# Attach parts into message container.
msg.attach(part1)
msg.attach(part2)

# Send the message via local SMTP server.
s = smtplib.SMTP('mail.engr.oregonstate.edu')
s.sendmail(me, you, msg.as_string())
s.quit()
