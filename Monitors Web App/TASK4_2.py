# Task 4.2

import sqlite3

conn = sqlite3.connect('spectrum.db')

with open('TASK4_1.sql', 'r') as sql:
    sql_script = sql.read()

conn.executescript(sql_script)


with open('MonitorInfo.csv', 'r') as f:
    r = f.readlines()
    
    for i in range(len(r)):
        r[i] = r[i][:-1:].split(',')

        if i > 0:
            r[i][1] = int(r[i][1])
            r[i][2] = int(r[i][2])
            r[i][3] = int(r[i][3])

    for i in range(len(r)):
        if i > 0:
            conn.execute(f"INSERT OR IGNORE INTO MonitorInfo (ModelNo, Price, Promotion, ScreenSize, Resolution) VALUES ('{r[i][0]}', {r[i][1]}, {r[i][2]}, {r[i][3]}, '{r[i][4]}')")


with open('ProductInfo.csv', 'r') as f:
    r = f.readlines()

    for i in range(len(r)):
        r[i] = r[i][:-1:].split(',')

    for i in range(len(r)):
        if i > 0:
            conn.execute(f"INSERT OR IGNORE INTO ProductInfo (SerialNo, ModelNo, Status) VALUES ('{r[i][0]}', '{r[i][1]}', '{r[i][2]}')")


with open('CustomerInfo.csv', 'r') as f:
    r = f.readlines()

    for i in range(len(r)):
        r[i] = r[i][:-1:].split(',')

    for i in range(len(r)):
        if i > 0:
            conn.execute(f"INSERT OR IGNORE INTO CustomerInfo (Email, Name, Contact, Address) VALUES ('{r[i][0]}', '{r[i][1]}', '{r[i][2]}', '{r[i][3]}')")


with open('SalesRecord.csv', 'r') as f:
    r = f.readlines()

    for i in range(len(r)):
        r[i] = r[i][:-1:].split(',')

    for i in range(len(r)):
        if i > 0:
            conn.execute(f"INSERT OR IGNORE INTO SalesRecord (Email, SerialNo, OrderDate, DeliveryDate) VALUES ('{r[i][1]}', '{r[i][2]}', '{r[i][3]}', '{r[i][4]}')")

conn.commit()

conn.close()