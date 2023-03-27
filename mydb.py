import mysql.connector

dataBase = mysql.connector.connect(
    host = "localhost",
    user = "root",
    passwd = "kani2002",
)

# prepare a cursor object
cursorObject = dataBase.cursor()

cursorObject.execute("CREATE DATABASE elderco")

print("All Done!")
 