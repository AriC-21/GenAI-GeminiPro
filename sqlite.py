import sqlite3

connection = sqlite3.connect('students.db')
curser = connection.cursor()

table_info = """
Create table STUDENTS(NAME VARCHAR(25), CLASS VARCHAR(25),
SECTION VARCHAR(25));
"""

curser.execute(table_info)

curser.execute("INSERT INTO STUDENTS VALUES('Ari', 'Gen AI', 'A')")
curser.execute("INSERT INTO STUDENTS VALUES('Sudipta', 'WebD', 'B')")
curser.execute("INSERT INTO STUDENTS VALUES('Arnab', 'DevOps', 'C')")
curser.execute("INSERT INTO STUDENTS VALUES('Raj', 'AI', 'A')")
curser.execute("INSERT INTO STUDENTS VALUES('Rahul', 'ML', 'B')")
curser.execute("INSERT INTO STUDENTS VALUES('Rohit', 'Gen AI', 'C')")

print("The inserted records are:\n")
data = curser.execute("SELECT * FROM STUDENTS")
for row in data:
    print(row)

connection.commit()
connection.close()