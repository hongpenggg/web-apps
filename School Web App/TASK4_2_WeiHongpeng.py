# Task 4.2

import datetime
import sqlite3

conn = sqlite3.connect('school.db')

class Person:
    def __init__(self, full_name, date_of_birth="YYYY-MM-DD"):
        self.full_name = full_name
        self.date_of_birth = date_of_birth
    
    def get_name(self):
        return self.full_name
    
    def set_name(self, name):
        self.full_name = name
        return self.full_name
    
    def get_dob(self):
        return self.date_of_birth
    
    def set_dob(self, dob):
        self.date_of_birth = dob
        return self.date_of_birth
    
    def is_adult(self):
        date = str(datetime.date.today())

        date = date.split('-')
        dob = self.date_of_birth.split('-')

        if int(date[0]) - int(dob[0]) < 18:
            return False
        if int(date[0]) - int(dob[0]) == 18:
            if int(dob[1]) > int(date[1]):
                return False
            
            if int(dob[1]) == int(date[1]):
                if int(dob[2]) > int(date[2]):
                    return False
        
        return True
    
    def screen_name(self):
        name = ''

        for i in range(len(self.full_name)):
            if self.full_name[i] != " ":
                name += self.full_name[i]
        
        date = self.date_of_birth.split('-')

        name = name + date[1] + date[2]

        return name


class Staff(Person):
    def is_adult(self):
        return True
    
    def screen_name(self):
        name = super().screen_name()
        return name + 'Staff'


class Student(Person):
    def is_adult(self):
        return False


with open('people.txt') as f:
    r = f.readlines()

    for i in range(len(r)):
        if '\n' in r[i]:
            r[i] = r[i].rstrip('\n')
    
        r[i] = r[i].split(',')

'''
for i in range(len(r)):
    if r[2] == 'Person':
        temp = Person(r[0], r[1])
        sname = temp.screen_name()
        isadult = 0 if temp.is_adult() == False else 1

        conn.execute(f"""INSERT OR IGNORE INTO Person (FullName, DateOfBirth, ScreenName, IsAdult) VALUES ('{r[0]}', '{r[1]}', '{sname}', {isadult})""")
        print(f'{r[0]} added to database.')

    elif r[2] == 'Student':
        temp = Student(r[0], r[1])
        sname = temp.screen_name()

        conn.execute(f"""INSERT OR IGNORE INTO Person (FullName, DateOfBirth, ScreenName, IsAdult) VALUES ('{r[0]}', '{r[1]}', '{sname}', 0)""")
        print(f'{r[0]} added to database.')

    elif r[2] == 'Staff':
        temp = Staff(r[0], r[1])
        sname = temp.screen_name()

        conn.execute(f"""INSERT OR IGNORE INTO Person (FullName, DateOfBirth, ScreenName, IsAdult) VALUES ('{r[0]}', '{r[1]}', '{sname}', 1)""")
        print(f'{r[0]} added to database.')
'''

for i in range(len(r)):
    if r[i][2] == 'Person':
        temp = Person(r[i][0], r[i][1])
        sname = temp.screen_name()
        isadult = 0 if temp.is_adult() == False else 1

        conn.execute("INSERT OR IGNORE INTO People (FullName, DateOfBirth, ScreenName, IsAdult) VALUES (?, ?, ?, ?)", (r[i][0], r[i][1], sname, isadult))
        print(f'{r[i][0]} added to database.')

    elif r[i][2] == 'Student':
        temp = Student(r[i][0], r[i][1])
        sname = temp.screen_name()

        conn.execute("INSERT OR IGNORE INTO People (FullName, DateOfBirth, ScreenName, IsAdult) VALUES (?, ?, ?, 0)", (r[i][0], r[i][1], sname))
        print(f'{r[i][0]} added to database.')

    elif r[i][2] == 'Staff':
        temp = Staff(r[i][0], r[i][1])
        sname = temp.screen_name()

        conn.execute("INSERT OR IGNORE INTO People (FullName, DateOfBirth, ScreenName, IsAdult) VALUES (?, ?, ?, 1)", (r[i][0], r[i][1], sname))
        print(f'{r[i][0]} added to database.')


conn.commit()

conn.close()