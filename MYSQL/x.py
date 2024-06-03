import mysql.connector

#Create the connection object
myconn=mysql.connector.connect(host="localhost",user="root",passwd="")

#Creating the cursor
cur=myconn.cursor()

try:
    dbs=cur.execute("create database PVG")
except:
    myconn.rollback()

for x in cur:
    print(x)
myconn.close()