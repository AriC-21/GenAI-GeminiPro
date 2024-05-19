import csv, sqlite3

con = sqlite3.connect('students.db') 
cur = con.cursor()

table_info = """
Create table ELECTION(STATE VARCHAR(25), YEAR INTEGER, CONSTITUENCY VARCHAR(25), 
CONSTITUENCY_NO INTEGER, CONSTITUENCY_TYPE VARCHAR(25), CANDIDATE_NAME VARCHAR(50), 
CANDIDATE_SEX VARCHAR(1), PARTY VARCHAR(50), PARTY_ABBREVIATION VARCHAR(25), 
TOTAL_VOTES INTEGER, ELECTORS INTEGER);
"""
cur.execute(table_info)
with open('na.csv','r') as fin: 
    dr = csv.DictReader(fin)
    to_db = [(i['st_name'], i['year'],i['pc_name'],i['pc_no'],i['pc_type'],i['cand_name'],i['cand_sex'],i['partyname'],i['partyabbre'],i['totvotpoll'],i['electors']) for i in dr]

cur.executemany("INSERT INTO ELECTION(STATE,YEAR,CONSTITUENCY,CONSTITUENCY_NO,CONSTITUENCY_TYPE,CANDIDATE_NAME,CANDIDATE_SEX,PARTY,PARTY_ABBREVIATION,TOTAL_VOTES,ELECTORS) VALUES (?,?,?,?,?,?,?,?,?,?,?);", to_db)
con.commit()
con.close()