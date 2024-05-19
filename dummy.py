import sqlite3

con = sqlite3.connect('students.db') 
cur = con.cursor()

rows = cur.execute("SELECT * FROM ELECTION WHERE CONSTITUENCY='Karimganj' AND YEAR='2014'")

for row in rows:
    print(row)