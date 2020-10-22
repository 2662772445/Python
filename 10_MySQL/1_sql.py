import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="root"
)

mycursor = mydb.cursor()

mycursor.execute("create database mydb")
