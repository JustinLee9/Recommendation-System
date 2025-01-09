import sqlite3

conn = sqlite3.connect('movie_recommendations.db')

cursor = conn.cursor()

# Users table
cursor.execute('''
CREATE TABLE IF NOT EXISTS Users (
    user_id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    age INTEGER NOT NULL
)
''')

# Movies table
cursor.execute('''
CREATE TABLE IF NOT EXISTS Movies (
    movie_id INTEGER PRIMARY KEY AUTOINCREMENT,
    title TEXT NOT NULL,
    genres TEXT NOT NULL,
    age_rating TEXT NOT NULL,
    rating REAL,
    release_date TEXT,
    backdrop_image TEXT
)
''')

# Ratings table
cursor.execute('''
CREATE TABLE IF NOT EXISTS Ratings (
    rating_id INTEGER PRIMARY KEY AUTOINCREMENT,
    user_id INTEGER NOT NULL,
    movie_id INTEGER NOT NULL,
    rating INTEGER NOT NULL,
    FOREIGN KEY (user_id) REFERENCES Users(user_id),
    FOREIGN KEY (movie_id) REFERENCES Movies(movie_id)
)
''')

conn.commit()
conn.close()

print('Database setup completed!')