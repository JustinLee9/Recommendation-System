import sqlite3

conn = sqlite3.connect('movie_recommendations.db')
cursor = conn.cursor()

cursor.execute("SELECT * FROM Users")
rows = cursor.fetchall()
for row in rows:
    print(row)

conn.close()
