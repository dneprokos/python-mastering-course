import sqlite3
import json
from pathlib import Path

movies = json.loads(Path("movies.json").read_text())

db_name = "db.sqlite3"

# Write data to database
with sqlite3.connect(db_name) as conn:
    command = "INSERT INTO Movies VALUES(?, ?, ?)"
    for movie in movies:
        conn.execute(command, tuple(movie.values()))
    conn.commit()

# Read data from database
with sqlite3.connect(db_name) as conn:
    command = "SELECT * FROM MOVIES"
    cursor = conn.execute(command)
    for row in cursor:
        print(row)
    movies = cursor.fetchall()
    print(movies)

# NOTE: This one will not work in you don't have table setup
