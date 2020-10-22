import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    database="mydb"
)

mycursor = mydb.cursor()

mycursor.execute("show tables")


for x in mycursor:
    print(x)
