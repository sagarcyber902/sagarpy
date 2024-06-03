import mysql.connector

myconn=mysql.connector.connect(host="localhost",user="root",passwd="",database="PVG")

cur=myconn.cursor()

try:
    #creating a table with name employee having four columns i.e name,id,salary and department
    dbs=cur.execute("create table students(name vchar(20) not null,id int(20)")
except:
    myconn.rollback()

myconn.close()