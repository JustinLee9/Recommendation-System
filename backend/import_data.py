import sqlite3
import csv

csv_file_path = "tmdb_dataset.csv"

conn = sqlite3.connect('movie_recommendations.db')
cursor = conn.cursor()

cursor.execute('''
CREATE TABLE IF NOT EXISTS Movies (
    movie_id INTEGER PRIMARY KEY,
    title TEXT NOT NULL,
    genres TEXT NOT NULL,
    age_rating TEXT NOT NULL,
    rating REAL,
    release_date TEXT
)
''')

with open(csv_file_path, newline='', encoding='utf-8') as csvfile:
    reader = csv.DictReader(csvfile)
    
    movies = []
    for row in reader:
        movies.append({
            "movie_id": row["id"],
            "title": row["title"],
            "genres": row["genres"],
            "age_rating": "Adult" if row["adult"].lower() == "true" else "General",
            "rating": float(row["vote_average"]) if row["vote_average"] else None,
            "release_date": row["release_date"]
        })
    
    cursor.executemany('''
    INSERT OR REPLACE INTO Movies (movie_id, title, genres, age_rating, rating, release_date)
    VALUES (:movie_id, :title, :genres, :age_rating, :rating, :release_date)
    ''', movies)

conn.commit()
conn.close()

print('CSV data imported successfully!')
