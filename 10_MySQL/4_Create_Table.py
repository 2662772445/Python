import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    database="mydb"
)

mycursor = mydb.cursor()


mycursor.execute("""create table students 
        (name varchar(50),
        address varchar(255)
        )"""
)

'''
mycursor.execute("""create table customers 
        (name varchar(50),
        address varchar(255)
        )"""
)
'''