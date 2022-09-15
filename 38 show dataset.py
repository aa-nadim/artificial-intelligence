import sqlite3

conn = sqlite3.connect('database_diabetes')
c = conn.cursor()
print('Age   Weight  Height          BP     Job       MS       Family_history  Other_Disease')
c.execute("SELECT * FROM patient")

myresult = c.fetchall()

for x in myresult:
  print(x)
