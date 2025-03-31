import json
from pathlib import Path

movies = [
    {"id": 1, "title": "Terminator", "year": 1984},
    {"id": 2, "title": "Alien", "year": 1979},
]

data = json.dumps(movies)
# [{"id": 1, "title": "Temninator", "year": 1984}, {"id": 2, "title": "Alien", "year": 1979}]
print(data)

movies_json = Path("movies.json")

# Write to the JSON file
movies_json.write_text(data)

# Read from JSON file
data = movies_json.read_text()
movies_parsed = json.loads(data)

# [{'id': 1, 'title': 'Temninator', 'year': 1984}, {'id': 2, 'title': 'Alien', 'year': 1979}]
print(movies_parsed)  # Will print parsed json of movies
print(movies_parsed[0]["title"])  # Temninator
