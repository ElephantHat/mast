from email.mime.text import MIMEText
import smtplib

me = "do.not.reply@engr.orst.edu"
you = "kangk@engr.orst.edu"

msg_text = '''
Advising Signup with McGrath, D Kevin Confirmed
Name: Kabir Kang 
Email: kangk@orst.edu
Date: Saturday, December 27th, 2014
Time: 11:00am - 11:15am

Please contact support@engr.oregonstate.edu if you experience problems
'''

msg = MIMEText(msg_text)
msg['Subject'] = 'Advising Signup Confirmation'
msg['From'] = me
msg['To'] = you

s = smtplib.SMTP('mail.engr.oregonstate.edu')
s.sendmail(me, you, msg.as_string())
s.quit()

