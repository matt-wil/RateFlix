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
            return True
        else:
            return False

    def add_movie(self, movie_name, rating, year, poster, imdb_link, country):
        movies = self._storage.list_movies()
        if movie_name in movies:
            return False
        else:
            self._storage.add_movie(movie_name, rating, year, poster, imdb_link, country)
            return True

    def delete_movie(self, movie_name):
        if movie_name in self._storage:
            self._storage.delete_movie(movie_name)
            return True

