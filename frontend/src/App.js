import React, { useState, useEffect } from "react";
import axios from "axios";
import "./styles/App.css";

function App() {
    const [movies, setMovies] = useState([]);
    const [page, setPage] = useState(1);
    const [hasMore, setHasMore] = useState(true);

    useEffect(() => {
        fetchMovies(page);
    }, [page]);

    const fetchMovies = (pageNumber) => {
        axios
            .get(`http://127.0.0.1:5000/api/movies?page=${pageNumber}&per_page=20`)
            .then((response) => {
                if (response.data.length === 0) {
                    setHasMore(false);
                } else {
                    setMovies((prev) => {
                        const movieIds = new Set(prev.map((movie) => movie.movie_id));
                        const filteredMovies = response.data.filter((movie) => !movieIds.has(movie.movie_id));
                        return [...prev, ...filteredMovies];
                    });
                }
            })
            .catch((error) => console.error("Error fetching movies:", error));
    };

    return (
        <div className="app-container">
            <h1>Movie Recommendations</h1>
            <div className="movie-container">
                {movies.map((movie, index) => (
                    <div key={movie.movie_id || index} className="movie-card">
                        <img src={`https://image.tmdb.org/t/p/w200${movie.backdrop_image}`} alt={movie.title} />
                        <div className="movie-details">
                            <h2>{movie.title}</h2>
                            <p>Genres: {movie.genres}</p>
                            <p>Release Date: {movie.release_date}</p>
                            <p>Rating: {movie.rating ? movie.rating.toFixed(1) : "N/A"}</p>
                        </div>
                    </div>
                ))}
            </div>
            {hasMore && (
                <button onClick={() => setPage((prev) => prev + 1)} className="load-more">
                    Load More
                </button>
            )}
        </div>
    );
}

export default App;
