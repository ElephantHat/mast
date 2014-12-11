#!/usr/bin/env python
"""
Here is a basic curses interface - so far it does nothing other than show a list of appointments.

Use arrow keys to select appointments.

Delete appointments by pressing 'd'

Quit program by hitting 'q'
"""

import MySQLdb
import database
import signal
import sys
from os.path import expanduser

import curses
import curses_interface




def main():
    home = expanduser("~")


    #read advisor name and mail from ~/.mastrc
    f = open(home+"/.mastrc", "r")
    advisor_info = f.readline().split()
    f.close()
    advisor_email = advisor_info[0]
    advisor_name = ""
    for i in range(1, len(advisor_info)):
        advisor_name+=advisor_info[i]
        if i < len(advisor_info)-1:
            advisor_name+=" "


    client = curses_interface.AppointmentsInterface(advisor_email, advisor_name)



if __name__ == "__main__":
    main()
