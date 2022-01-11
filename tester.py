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
db.execute("CREATE TABLE users (id SERIAL PRIMARY KEY, username TEXT NOT NULL, hash TEXT NOT NULL, breakfast TEXT NULL)")

