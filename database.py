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

def add_appointment(cur, advisor_name, student_name, )