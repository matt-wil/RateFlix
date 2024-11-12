import model.movie_api


class MovieCrud:
    """
    A class that provides Create, Read, Update, and Delete (CRUD) operations for managing movies in the app's storage.
    Methods:
        __init__(storage):
            Initializes the MovieCrud instance with a storage object that handles movie data persistence.

        list_movies():
            Returns a dictionary of all movies stored in the database.

        update_movie(movie_name, notes):
            Updates the movie's notes in the database. Returns a success or error message.

        add_movie(movie_name):
            Adds a new movie to the database by fetching data from an external API.
            Returns a success or error message.

        delete_movie(movie_name):
            Deletes a movie from the database. Returns a success or error message.
    """
    def __init__(self, storage):
        """Initialise the MovieCrud instance with a storage object
        :arg:
            storage: An instance of a storage class"""
        self._storage = storage

    def list_movies(self) -> dict:
        """Returns a dictionary of the movies from the storage
        :return: (dict) {"title": {
                                    "rating": rating,
                                    "year": year,
                                    "poster": poster,
                                    "imdbID": imdbID,
                                    "country": country,
                                    "note": note
                                    }
                            }"""
        return self._storage.list_movies()

    def update_movie(self, movie_name: str, notes: str) -> dict:
        """
        Adds a note to the dictionary and returns a dictionary to be used inside the View class
        :param movie_name: Title of the movie
        :param notes: Notes to be added to the give movie_name
        :return: (dict)
                    Success: {"success": True, "message": f" {notes} added to {movie_name}"}
                    Error: {"success": False, "error": f"{movie_name} not found in the library"}
        """
        movies = self._storage.list_movies()
        if movie_name in movies:
            self._storage.update_movie(movie_name, notes)
            return {"success": True, "message": f"{notes} added to {movie_name}"}
        else:
            return {"success": False, "error": f"{movie_name} not found in the library"}

    def add_movie(self, movie_name: str) -> dict:
        """
        Adds a new movie to the storage by fetching the data from the OMDB API
        :param movie_name: title of the movie
        :return: (dict)
                    Success: {"success": True, "message": f"{movie_name} added successfully to the library"}
                    Error: {"success": False, "error": (The relevant error message)}
        """
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

    def delete_movie(self, movie_name: str) -> dict:
        """
        Delete a movie from the storage
        :param movie_name: title of the movie
        :return: (dict)
                    Success: {"success": True, "message": f"{movie_name} deleted from the library"}
                    Error: {"success": False, "error": f"{movie_name} was not found in the library"}
        """
        movies = self._storage.list_movies()
        if movie_name in movies:
            self._storage.delete_movie(movie_name)
            return {"success": True, "message": f"{movie_name} deleted from the library"}
        else:
            return {"success": False, "error": f"{movie_name} was not found in the library"}




