import sqlite3

conn = sqlite3.connect('sanitisers.db')

with open('sanitisers.txt', 'r') as f:
    r = f.readlines()

    for i in range(len(r)):
        if '\n' in r[i]:
            r[i] = r[i].rstrip('\n')
        
        r[i] = r[i].split(',')

        if i != 0:
            r[i] = r[i][:-2:]
        else:
            r[i] = r[i][:-1:]

    print(r)

with open('TASK1_WeiHongpeng.sql', 'r') as sql:
    sql_script = sql.read()
    # print(sql_script)

    conn.executescript(sql_script)

for i in range(1, len(r)):
    conn.execute(f"""
INSERT OR IGNORE INTO Sanitisers (product_name, active_ingredient, alcohol_based) VALUES ('{r[i][0]}', '{r[i][1]}', '{r[i][2]}')
""")
    print(r[i])

conn.commit()
conn.close()