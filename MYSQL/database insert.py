import mysql.connector

myconn=mysql.connector.connect(host="localhost",user="root",passwd="",database="sagar")

cur=myconn.cursor()