"""
Here is a basic curses interface - so far it does nothing other than show a list of fake appointments.

Make sure to exit using 'q' and not CTRL-C
"""

import curses
import MySQLdb
import database

class Appointment:
    def __init__(self, time, date, student):
        self.time = time
        self.date = date
        #self.advisor = advisor
        self.student = student

def main():
    appointment_list = []
    advisor_name = raw_input("Enter your name: ")

    #create a cursor to perform database actions with
    cur = database.create_cursor()

    #perform query on db
    
    """
    A quick note: these values will not work if ran again, to test with new values,
    change at least the time, date, or advisor, then it should work
    """
    database.add_appointment(cur, "John Doe", "advisor1@oregonstate.edu", "New student", "new student email", "12-04-2013", "1:00am")
    
    database.get_appointments(cur, advisor_name)

    #put matching appointments in list
    number_of_appointments = 0
    appointment_list = []
    for row in cur.fetchall():
        apt = Appointment(row[1], row[0], row[9])
        appointment_list.append(apt)
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

if __name__ == "__main__":
    main()
