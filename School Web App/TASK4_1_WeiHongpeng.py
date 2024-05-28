import sqlite3

conn = sqlite3.connect('school.db')

with open('TASK4_1_WeiHongpeng.sql', 'r') as f:
    sql_script = f.read()

conn.executescript(sql_script)

conn.commit()
conn.close()