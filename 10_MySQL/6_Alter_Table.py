import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    database="mydb"
)

mycursor = mydb.cursor()

mycursor.execute("ALTER table customers ADD COLUMN id int AUTO_INCREMENT PRIMARY Key ")
