from db import *

name=input("Name: ")
email=input("Email: ")
password=input("Password: ")

sql="INSERT INTO users(name,email,password) VALUES(%s,%s,%s)"
val=(name,email,password)

cursor.execute(sql,val)
conn.commit()

print("Registration Successful")