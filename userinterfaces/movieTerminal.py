
from userinterfaces.Base_UI import BaseUI


class MovieAppTerminalUI(BaseUI):
    def __init__(self, app_functionality):
        self.app_functionality = app_functionality

    def display_all(self):
        """
        receive a dictionary of movies in the storage
        displays the name, imdb rating, the year of release and notes if a movie has some.
        :return:
        """
        movies = self.app_functionality.list_movies()

    def add(self):
        pass

    def delete(self):
        pass

    def update(self):
        pass

    def display_stats(self):
        pass

    def display_random(self):
        pass

    def search(self):
        pass

    def display_sorted(self):
        pass

    def create_histogram(self):
        pass

    def display_chronologically(self):
        pass

    def filter(self):
        pass

    def generate_website(self):
        pass
