import os
from cs50 import SQL

"""
This is used for the initial creation of the databse.
It can also be used to test a specific function
"""

uri = os.getenv("DATABASE_URL")
if uri.startswith("postgres://"):
    uri = uri.replace("postgres://", "postgresql://")
db = SQL(uri)

""" Creates user database """
# db.execute("CREATE TABLE users (id SERIAL PRIMARY KEY, username  TEXT NOT NULL UNIQUE, hash TEXT NOT NULL, sun TEXT NULL, mon TEXT NULL, tue TEXT NULL, wed TEXT NULL, thu TEXT NULL)")
#[selection] = db.execute("SELECT sun, mon, tue, wed, thu FROM users WHERE id = (?)", 1)
# Get Breakfast Choice

menu = {}

for day in ['sun', 'mon', 'tue', 'wed', 'thu']:
    temp = db.execute(f"SELECT {day}, count({day}) FROM users GROUP BY {day}")
    for dic in temp:
        choice = dic[day]
        amount = dic['count']
        menu[day] = menu[day], (choice, amount)

print(menu)
