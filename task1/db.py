import mysql.connector

conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Prity@2005",
    database="bus_pass_system"
)

cursor=conn.cursor()