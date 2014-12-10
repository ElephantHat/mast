"""
Here is a basic curses interface - so far it does nothing other than show a list of fake appointments.

Make sure to exit using 'q' and not CTRL-C
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


    #read advisor email from ~/.mastrc
    #commenting out for testing...
    #f = open(home+"/.mastrc", "r")
    #advisor_email = f.readline()
    #f.close()
    #advisor_email = advisor_email.rstrip("\n")

    advisor_email = "advisor1@oregonstate.edu"
    advisor_name = "default advisor"

    client = curses_interface.AppointmentsInterface(advisor_email, advisor_name)



if __name__ == "__main__":
    main()
