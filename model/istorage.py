from abc import ABC, abstractmethod


class IStorage(ABC):
    """
    An Abstract class to allow for more flexibility in our storage options.
    """
    @abstractmethod
    def list_movies(self):
        """
        list all movies in the app
        :return:
        """
        pass

    @abstractmethod
    def add_movie(self, title, year, rating, poster, imdbID, country):
        """
        add a movie into the app database
        :return:
        """
        pass

    @abstractmethod
    def delete_movie(self, title):
        """
        delete a movie from the app database
        :return:
        """
        pass

    @abstractmethod
    def update_movie(self, title, note):
        """
        update a movie that is currently in the app database
        :return:
        """
        pass

    @abstractmethod
    def _save_movies(self, movies):
        pass
