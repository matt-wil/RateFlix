from abc import ABC, abstractmethod


class IStorage(ABC):
    """
    An Abstract class to allow for more flexibility in our storage options.
    """
    @abstractmethod
    def list_movies(self):
        """
        list all movies in the RateFlix app
        :return:
        """
        pass

    @abstractmethod
    def add_movie(self, title, year, rating):
        """
        add a movie into the RateFlix app database
        :return:
        """
        pass

    @abstractmethod
    def delete_movie(self, title):
        """
        delete a movie from the RateFlix app database
        :return:
        """
        pass

    @abstractmethod
    def update_movie(self, title, rating):
        """
        update a movie that is currently in the RateFlix app database
        :return: 
        """
        pass

    @abstractmethod
    def save_movies(self, movies):
        pass

