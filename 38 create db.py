import sqlite3
#sqlite3.connect('database_diabetes') #database create
conn = sqlite3.connect('database_diabetes')
c = conn.cursor()
c.execute("CREATE TABLE patient (age VARCHAR(255), weight VARCHAR(255), height VARCHAR(255),blood_pressure VARCHAR(255),working_status VARCHAR(255)" \
     ",martial_status VARCHAR(255),family_history VARCHAR(255),other_diseases VARCHAR(255))") #table create



c.execute('''
         CREATE TABLE patient2 (age TEXT, weight TEXT, height TEXT,blood_pressure TEXT,working_status TEXT" \
     ",martial_status TEXT,family_history TEXT,other_diseases TEXT)
          ''')


c.execute('''INSERT INTO patient VALUES('18','55','5.3feet','130','teacher','married','Do not have any','No')
          ''')


conn.commit()
