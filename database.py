import MySQLdb


def create_conn():
    db = MySQLdb.connect(host='mysql.eecs.oregonstate.edu',
                         user='cs419-group1',
                         passwd='RddS6d6jEvaEXY4J',
                         db='cs419-group1')
    return db

def get_appointments(advisor_email):
    db = create_conn()
    cur = db.cursor()
    cur.execute("SELECT advisor.email, student.name, student.email, apt_date, apt_time, apt_uid FROM appointment INNER JOIN advisor ON advisor.id=aid INNER JOIN student ON student.id=sid WHERE advisor.email='"+advisor_email+"'")
    appointments = cur.fetchall()
    db.close()
    return appointments

def delete_appointment(uid):
    db = create_conn()
    cur = db.cursor()

    cur.execute("DELETE FROM appointment WHERE apt_uid='"+uid+"'")

    db.commit()
    db.close()


def add_appointment(advisor_email, student_name, student_email, date, time, uid):
    db = create_conn()
    cur = db.cursor()

    #check for and add advisor
    cur.execute("SELECT email FROM advisor WHERE email='"+advisor_email+"'")
    print cur.rowcount
    if(cur.rowcount==0):
    #no advisor with this email, insert advisor info to DB
        cur.execute("INSERT INTO advisor(id, email) VALUES (DEFAULT,'"+advisor_email+"')")

        #check for and add student
    cur.execute("SELECT email FROM student WHERE email='"+student_email+"'")
    print cur.rowcount
    if(cur.rowcount==0):
        #no student with this email, insert student info to DB
        cur.execute("INSERT INTO student(id, email, name) VALUES (DEFAULT,'"+student_email+"','"+student_name+"')")

    #add appointment
    cur.execute("INSERT INTO appointment(apt_date, apt_time, apt_uid, aid, sid) VALUES ('"+date+"','"+time+"','"+uid+"',(SELECT id FROM advisor WHERE email='"+advisor_email+"'),(SELECT id FROM student WHERE email='"+student_email+"'))")

    db.commit()
    db.close()
