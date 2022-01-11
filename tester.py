import os
from cs50 import SQL



uri = os.getenv("DATABASE_URL")
if uri.startswith("postgres://"):
    uri = uri.replace("postgres://", "postgresql://")
db = SQL(uri)
db.execute("CREATE TABLE users (id SERIAL PRIMARY KEY, username TEXT NOT NULL, hash TEXT NOT NULL, breakfast TEXT NULL)")

