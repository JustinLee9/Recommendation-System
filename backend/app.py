from flask import Flask, request, jsonify
from flask_cors import CORS
import sqlite3

app = Flask(__name__)

def get_db_connection():
    conn = sqlite3.connect('movie_recommendations.db')
    conn.row_factory = sqlite3.Row
    return conn

@app.route('/api/add-user', methods=['POST'])
def add_user():
    data = request.get_json()
    name = data['name']
    age = data['age']

    if not name or not age:
        return jsonify({"error": "Please provide both name and age"}), 400
    
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("INSERT INTO Users (name, age) VALUES (?, ?)", (name, age))
    conn.commit()
    conn.close()

    return jsonify({"message": "User added successfully!"}), 201

@app.route('/api/add-movie', methods=['POST'])
def add_movie():
    data = request.get_json()
    title = data['title']
    genre = data['genre']
    age_rating = data['age_rating']
    average_rating = data['average_rating']

    if not title or not genre or not age_rating or not average_rating:
        return jsonify({"error": "Please provide all movie details"}), 400
    
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("INSERT INTO Movies (title, genre, age_rating, average_rating) VALUES (?, ?, ?, ?)", (title, genre, age_rating, average_rating))
    conn.commit()
    conn.close()

    return jsonify({"message": "Movie added successfully!"}), 201

@app.route('/api/add-rating', methods=['POST'])
def add_rating():
    data = request.get_json()
    user_id = data['user_id']
    movie_id = data['movie_id']
    rating = data['rating']

    if not user_id or not movie_id or not rating:
        return jsonify({"error": "Please provide all rating details"}), 400
    
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("INSERT INTO Ratings (user_id, movie_id, rating) VALUES (?, ?, ?)", (user_id, movie_id, rating))
    conn.commit()
    conn.close()

    return jsonify({"message": "Rating added successfully!"}), 201

@app.route('/api/movies', methods=['GET'])
def get_movies():
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM Movies")
    movies = cursor.fetchall()
    conn.close()

    movies_list = [dict(movie) for movie in movies]
    return jsonify({movies_list})

@app.route('/api/users', methods=['GET'])
def get_users():
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM Users")
    rows = cursor.fetchall()
    users = [{"id": row[0], "name": row[1], "age": row[2]} for row in rows]
    return jsonify(users)


@app.route('/')
def hello():
    return "Backend is working!"

@app.route('/api/test')
def test():
    return {"message": "Hello from Flask!"}

if __name__ == '__main__':
    app.run(debug=True)