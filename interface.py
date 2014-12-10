"""
Here is a basic curses interface - so far it does nothing other than show a list of fake appointments.

Make sure to exit using 'q' and not CTRL-C
"""

import curses
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
    f = open(home+"/.mastrc", "r")
    advisor_email = f.readline()
    f.close()
    advisor_email = advisor_email.rstrip("\n")

    #put matching appointments in list
    number_of_appointments = 0
    raw_appointments = database.get_appointments(advisor_email)

    appointment_list = []

    for appointments in raw_appointments:
        new_apt = Appointment(appointments[4], appointments[3], appointments[1])
        appointment_list.append(new_apt)
        number_of_appointments += 1

    screen = curses.initscr()
    curses.noecho()
    curses.curs_set(0)
    screen.keypad(1)

    #print header
    screen.addstr("Current Appointments:\n")
    screen.addstr(1, 0, "DATE")
    screen.addstr(1, 15, "TIME")
    screen.addstr(1, 25, "STUDENT")
    #print out each appointment
    for x in range(0,number_of_appointments):
        screen.addstr((2+x), 0, appointment_list[x].date)
        screen.addstr((2+x), 15, appointment_list[x].time)
        screen.addstr((2+x), 25, appointment_list[x].student)

    #TODO: Add ability to select appointments with arrow keys
    while True:
       event = screen.getch()
       if event == ord("q"): break

    curses.endwin()

def signal_handler(signal, frame):
    print("CTRL-C: Goodbye...")
    curses.endwin()
    sys.exit(0)# Isn't this all the functionality needed for CTRL-C? --Kabir
signal.signal(signal.SIGINT,signal_handler)

if __name__ == "__main__":
    main()
