import sqlite3

db = sqlite3.connect('test_db.sqlite')
cursor = db.cursor()

candidates = []
header = True
for line in open('candidates.txt'):
    if header: 
        header = False; 
        continue
    else:     
        line = line.rstrip()
        candidate = line.split('|')
        candidates.append(candidate)

cursor.execute("DROP TABLE IF EXISTS candidates")
cursor.execute('''CREATE TABLE candidates (
               id INTEGER PRIMARY KEY NOT NULL, 
               first_name TEXT, 
               last_name TEXT, 
               middle_init TEXT, 
               party TEXT NOT NULL)''')

for candidate in candidates:
    cursor.execute('''INSERT INTO candidates
               (id, first_name, last_name, middle_init, party)
               VALUES (?, ?, ?, ?, ?)''', 
                (candidate[0], candidate[1], candidate[2], candidate[3], candidate[4]))

db.commit()
cursor.execute("SELECT * FROM candidates")
for i in cursor:
    print(i)