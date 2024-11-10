import model.movie_api


class MovieCrud:
    def __init__(self, storage):
        self._storage = storage

    def list_movies(self):
        """Returns a dictionary of the movies model"""
        return self._storage.list_movies()

    def update_movie(self, movie_name, notes):
        movies = self._storage.list_movies()
        if movie_name in movies:
            self._storage.update_movie(movie_name, notes)
            return {"success": True, "message": f" {notes} added to {movie_name}"}
        else:
            return {"success": False, "error": f"{movie_name} not found in the library"}

    def add_movie(self, movie_name):
        if not movie_name:
            return {"success": False, "error": "Movie name cannot be empty"}

        movies = self._storage.list_movies()
        if movie_name in movies:
            return {"success": False, "error": "Movie is already in the library"}

        try:
            movie, rating, year, poster_url, imdb_full_link, country = model.movie_api.api_extraction(movie_name)
        except Exception as e:
            return {"success": False, "error": f"API Error: {str(e)}"}

        if not movie:
            return {"success": False, "error": "Movie not found in the database"}

        self._storage.add_movie(movie_name, rating, year, poster_url, imdb_full_link, country)
        return {"success": True, "message": f"{movie_name} added successfully to the library"}

    def delete_movie(self, movie_name):
        movies = self._storage.list_movies()
        if movie_name in movies:
            self._storage.delete_movie(movie_name)
            return {"success": True, "message": f"{movie_name} deleted from the library"}
        else:
            return {"success": False, "error": f"{movie_name} was not found in the library"}




