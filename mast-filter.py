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


