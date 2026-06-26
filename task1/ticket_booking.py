from db import *
import uuid

user_id=int(input("User ID: "))
source=input("Source: ")
destination=input("Destination: ")
date=input("Date(YYYY-MM-DD): ")

fare=200

ticket_number=str(uuid.uuid4())[:8]

sql="""
INSERT INTO bookings
(user_id,source,destination,journey_date,fare,ticket_number)
VALUES(%s,%s,%s,%s,%s,%s)
"""

cursor.execute(sql,
(user_id,source,destination,date,fare,ticket_number))

conn.commit()

print("Ticket Booked")
print("Ticket Number:",ticket_number)