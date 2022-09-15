import mysql.connector
try:
    conn= mysql.connector.connect(
        user='root',
        password='sharif',
        host='localhost',
        port='3306'
    )
    if(conn.is_connected()):
        print("Connected")
except:
    print("Unable to connect")
sql='Create Database pdb'
myc = conn.cursor()
myc.execute('Create Database pdb')

myc.close()
conn.close()