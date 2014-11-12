import email
import sys

"""
Hey, so here is a parser, at the moment it converts email text files to a string, and then
parses them. It should be easy to modify to use stdin. It works with email.txt and cancel_email.txt
which I will upload when I put this up.
"""

#should move this to a different file, so it can be shared by other parts of program
class Appointment:
    def __init__(self, time, date, student):
        self.time = time
        self.date = date
        self.advisor = advisor
        self.student = student

raw_email = file('cancel_email.txt', 'r')
message = ""
message_body = ""
appointment_status = ""
advisor_name = ""

for row in raw_email:
    message+=row
   
message = email.message_from_string(message)
message_body = message.get_payload()

emails = message['to'].split('; ')
emails[0] = emails[0].strip("; ")
message_info = message_body.split('\n')

"""
the filter here at the moment only parses names if the appointment is being created, which is 
when we might need to add students/advisors to the database. if the appointment is a cancellation,
it only parses the emails, date, and time of the appointment which will be enough to id an appointment

"""
names_info = message['subject'].split(' ')
if names_info[0] == "Advising" and names_info[1] == "Signup" and names_info[2] == "with":
    advisor_name = names_info[3] + " " + names_info[4];
    if names_info[5] != "confirmed":
        advisor_name += " " + names_info[5]
        appointment_status = names_info[6]
    else:
        appointment_status = names_info[5]
        
if names_info[0] == "Advising" and names_info[1] == "Signup" and names_info[2] == "Cancellation":
    #nothing needed, we should only need both emails, date, and time to cancel an appointment
    appointment_status = "cancelled"
        
student_name = message_info[1].split("Name: ")[1]
date = message_info[3].split("Date: ")[1]
time = message_info[4].split("Time: ")[1]

print emails[0]
print emails[1]
print advisor_name
print student_name
print appointment_status
print date
print time

