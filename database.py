import MySQLdb

def create_cursor():
    db = MySQLdb.connect(host='mysql.eecs.oregonstate.edu',
                         user='cs419-group1',
                         passwd='RddS6d6jEvaEXY4J',
                         db='cs419-group1')
    #create db cursor object
    cur = db.cursor()
    return cur

def get_appointments(cur, advisor_name):
	cur.execute("SELECT * FROM appointment INNER JOIN advisor ON advisor.id=aid INNER JOIN student ON student.id=sid WHERE advisor.name='"+advisor_name+"'")

def add_appointment(cur, advisor_name, advisor_email, student_name, student_email, date, time):

	#check for and add advisor
	cur.execute("SELECT * FROM advisor WHERE email='"+advisor_email+"'")
	if(cur.rowcount==0):
		#no advisor with this email, insert advisor info to DB
		cur.execute("INSERT INTO advisor(id, email, name) VALUES (DEFAULT,'"+advisor_email+"','"+advisor_name+"')")	

	#check for and add student
	cur.execute("SELECT * FROM student WHERE email='"+student_email+"'")
	if(cur.rowcount==0):
		#no student with this email, insert student info to DB
		cur.execute("INSERT INTO student(id, email, name) VALUES (DEFAULT,'"+student_email+"','"+student_name+"')")

	#add appointment
	cur.execute("INSERT INTO appointment(apt_date, apt_time, aid, sid) VALUES ('"+date+"','"+time+"',(SELECT id FROM advisor WHERE email='"+advisor_email+"'),(SELECT id FROM student WHERE email='"+student_email+"'))")
