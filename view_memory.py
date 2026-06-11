import sqlite3

conn = sqlite3.connect("assistant.db")
cursor = conn.cursor()

cursor.execute("SELECT * FROM memory")
rows = cursor.fetchall()

for row in rows:
    print(row)

conn.close()