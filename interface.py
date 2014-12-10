"""
Here is a basic curses interface - so far it does nothing other than show a list of fake appointments.

Make sure to exit using 'q' and not CTRL-C
"""

import curses
import curses_interface
import MySQLdb
import database
import signal
import sys
from os.path import expanduser

class Appointment:
    def __init__(self, time, date, student):
        self.time = time
        self.date = date
        self.student = student

def main():
    home = expanduser("~")
    appointment_list = []

    #read advisor email from ~/.mastrc
    #commenting out for testing...
    #f = open(home+"/.mastrc", "r")
    #advisor_email = f.readline()
    #f.close()
    #advisor_email = advisor_email.rstrip("\n")

    advisor_email = "advisor1@oregonstate.edu"

    client = curses_interface.AppointmentsInterface(advisor_email)


if __name__ == "__main__":
    main()
