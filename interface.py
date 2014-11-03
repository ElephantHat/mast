"""
Here is a basic curses interface - so far it does nothing other than show a list of fake appointments.

Make sure to exit using 'q' and not CTRL-C
"""

import curses 

class Appointment:
	def __init__(self, time, date, student):
		self.time = time
		self.date = date
		#self.advisor = advisor
		self.student = student

def main():
	screen = curses.initscr()
	curses.noecho()
	curses.curs_set(0)
	screen.keypad(1)

	appointmentList = []

	a = Appointment("12:30pm", "01-01-2001", "Student's name")

	#Fill appointmentList with fake appointments
	#TODO use sql queries to get real data from database and format accordingly
	for x in range(0,10):
		appointmentList.append(Appointment("12:3"+str(x), "01-01-200"+str(x), "Student-"+str(x)))

	#print header
	screen.addstr("Current Appointments:\n") 
	screen.addstr(1, 0, "DATE")
	screen.addstr(1, 15, "TIME")
	screen.addstr(1, 25, "STUDENT")
	#print out each appointment
	for x in range(0,10):
		screen.addstr((2+x), 0, appointmentList[x].date)
		screen.addstr((2+x), 15, appointmentList[x].time)
		screen.addstr((2+x), 25, appointmentList[x].student)

	#TODO: Add ability to select appointments with arrow keys
	while True: 
	   event = screen.getch() 
	   if event == ord("q"): break 
	    
	curses.endwin()

if __name__ == "__main__":
    main()