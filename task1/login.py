from db import *

email=input("Email: ")
password=input("Password: ")

sql="SELECT * FROM users WHERE email=%s AND password=%s"

cursor.execute(sql,(email,password))

if cursor.fetchone():
    print("Login Successful")
else:
    print("Invalid Login")