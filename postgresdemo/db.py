

import psycopg2
from datetime import datetime,date

sqlinsert = """INSERT INTO attandance (name,time,date,subcode) values(%s,%s,%s,%s)"""
con = psycopg2.connect(host = 'localhost', database = 'abc', user = 'user1', password = 'user1')
cur = con.cursor()

def removestudents(usn):
    con = psycopg2.connect(host = 'localhost', database = 'abc', user = 'user1', password = 'user1')
    cur = con.cursor()
    deleteQuery = '''delete from student where usn = %s'''
    value = (usn,)
    cur.execute(deleteQuery,value)
    con.commit()
    cur.close()
    con.close()



def studentdb(name,usn,course):
    con = psycopg2.connect(host = 'localhost', database = 'abc', user = 'user1', password = 'user1')
    cur = con.cursor()
    sqlQ = ''' INSERT INTO student values(%s,%s,%s) '''
    value = ([name,usn,course])
    cur.execute(sqlQ,value)
    con.commit()
    cur.close()
    con.close()

def getStudentAttendance(date):
    con = psycopg2.connect(host = 'localhost',database= 'abc',user = 'user1', password = 'user1')
    cur = con.cursor()
    getdataQ = ''' select * from attandance where date = %s '''
    date = (date,)
    cur.execute(getdataQ,date)
    rows = cur.fetchall()
    return rows
    cur.close()
    con.close()


# remove staff by admin code goes here
def removestaffdb(name):
    con = psycopg2.connect(host = 'localhost',database= 'abc',user = 'user1', password = 'user1')
    cur = con.cursor()
    deleteQuery = '''delete from staff where name = %s'''
    name = (name,)
    cur.execute(deleteQuery,name)
    con.commit()
    cur.close()
    con.close()


def viewORremovestaff():
    con = psycopg2.connect(host = 'localhost',database= 'abc',user = 'user1', password = 'user1')
    cur = con.cursor()
    sqlselectQuery = '''SELECT * FROM staff'''
    cur.execute(sqlselectQuery)
    rows = cur.fetchall()
    for r in rows:
        print(f"{r[0]}   {r[1]}    {r[2]}")
    sqldeleteQuery = '''DELETE * FROM staff where name = %s'''
    cur.close()
    con.close()


def InsertStaffData(name,phone,email,username,password):
    con = psycopg2.connect(host = 'localhost', database = 'abc', user = 'user1', password = 'user1')
    cursor = con.cursor()
    sqlinsertstaffdata = """ INSERT INTO staff (name,phone,email,username,password) values(%s,%s,%s,%s,%s) """
    value = ([name,phone,email,username,password])
    cursor.execute(sqlinsertstaffdata,value)
    con.commit()
    cursor.close()
    con.close()

def staffauthenication(username,password):
    flag = 0
    con = psycopg2.connect(host = 'localhost', database = 'abc', user = 'user1', password = 'user1')
    cursor = con.cursor()
    select = """SELECT name,username,password,email,phone FROM staff WHERE username = %s and password = %s"""
    value = ([username,password])
    cursor.execute(select,value)
    rows = cursor.fetchall()
    for r in rows:
        #print(r[3])
        #print(r[4])
        if (username == r[1] and password == r[2]):
            flag = 1
        else:
            flag = 0
    cursor.close()
    con.close()
    if(flag==0):
        return False,False
    else:
        return True,r[0],r[3],r[4]




def insertQuery(subcode):
    now = date.today()
    now =now.strftime('%d-%m-%y')
    con = psycopg2.connect(host = 'localhost', database = 'abc', user = 'user1', password = 'user1')
    cur = con.cursor()
    student=[]
    stulist = []
    students = []
    with open(now+".csv","r+") as f:
        student = f.readlines()
        
    for eachstudent in student:
        students.append(eachstudent.strip().split(","))
    students.pop(0)

    for line in students:
        print(subcode)
        studentname = line[0]
        studenttime  = line[1]
        studentdate = line[2]
        print(studentname)
        value = tuple([studentname,studenttime,studentdate,subcode])
        cur.execute(sqlinsert,value)
        con.commit()
    cur.close()
    con.close()
    return


def Display():
    con = psycopg2.connect(host = 'localhost', database = 'abc', user = 'user1', password = 'user1')
    cur = con.cursor()
    cur.execute("select * from attandance")
    rows = cur.fetchall()
    for r in rows:
        print(f"NAME {r[0]} DATE  {r[1]} TIME {r[2]}")
        #
    cur.close()
    con.close()

def getdata():
    con = psycopg2.connect(host = 'localhost', database = 'abc', user = 'user1', password = 'user1')
    cur = con.cursor()
    cur.execute("select * from attandance")
    rows = cur.fetchall()
    return rows
    cur.close()
    con.close()




#insertQuery()
#Display()
cur.close()
#close the connection
con.close()


