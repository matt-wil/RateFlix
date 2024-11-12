import os.path
import random
from os.path import join
from matplotlib import pyplot as plt
from datetime import datetime


class MovieManager:
    """
    A class for managing movies, including operations like sorting, filtering, and creating visualizations.

    Methods:
        __init__(storage):
            Initializes the MovieManager with a storage object for movie data.

        random_movie():
            Returns a random movie from the list of stored movies.

        sort_by_rating():
            Sorts the movies by rating in descending order and returns the sorted dictionary.

        create_histogram(filename="movies_histogram.png"):
            Creates and saves a histogram of movie ratings as a PNG file.

        sort_chronologically_latest_first():
            Sorts the movies by their release year in descending order and returns the sorted dictionary.

        sort_chronologically_earliest_first():
            Sorts the movies by their release year in ascending order and returns the sorted dictionary.

        filter_movies(min_rating_input, start_year_input, end_year_input):
            Filters movies based on the provided rating and release year range.
    """

    def __init__(self, storage):
        """
        Initializes the MovieManager instance with a storage object for managing movie data.
        :arg:
            storage: An instance of a storage class responsible for movie data persistence.
        """
        self._storage = storage

    def random_movie(self):
        """
        Returns a random movie from the list of stored movies.
        :return: (tuple): A tuple containing the movie title and its details (rating, year, etc.).
        """
        movies = self._storage.list_movies()
        the_random_movie, details = random.choice(list(movies.items()))
        return the_random_movie, details

    def sort_by_rating(self):
        """
        Sorts the movies by their rating in descending order and returns the sorted dictionary.
        :return: (dict): A dictionary of movies sorted by rating in descending order.
        """
        movies = self._storage.list_movies()
        return dict(sorted(movies.items(), key=lambda item: item[1]["rating"], reverse=True))

    def create_histogram(self, filename="movies_histogram.png"):
        """
        Creates and saves a histogram of movie ratings as a PNG file in the 'histograms' directory.
        :arg:
            filename (str): The name of the file to save the histogram as. Default is "movies_histogram.png".
        """
        movies = self._storage.list_movies()
        movie_ratings = [val["rating"] for val in movies.values()]

        if not os.path.exists("histograms"):
            os.makedirs("histograms")

        plt.hist(movie_ratings, bins=5, color='blue', edgecolor='black')
        plt.title("Movie Ratings Histogram")
        plt.xlabel("Rating")
        plt.ylabel("Number of Movies")

        plt.savefig(join("histograms", filename))

        plt.show()

    def sort_chronologically_latest_first(self):
        """
        Sorts the movies by their release year in descending order and returns the sorted dictionary.
        :return: (dict): A dictionary of movies sorted by release year from latest to earliest.
        """
        movies = self._storage.list_movies()
        return dict(sorted(movies.items(), key=lambda item: item[1]["year"], reverse=True))

    def sort_chronologically_earliest_first(self):
        """
        Sorts the movies by their release year in ascending order and returns the sorted dictionary.
        :return: (dict): A dictionary of movies sorted by release year from earliest to latest.
        """
        movies = self._storage.list_movies()
        return dict(sorted(movies.items(), key=lambda item: item[1]["year"], reverse=False))

    def filter_movies(self, min_rating_input, start_year_input, end_year_input):
        """
        Filters movies based on the provided rating and release year range.
        :arg:
            min_rating_input (str): The minimum rating to filter movies by (between 0 and 10).
            start_year_input (str): The start year for filtering movies.
            end_year_input (str): The end year for filtering movies.
        :return: (tuple): A tuple containing a list of filtered movies (or an empty list if no movies match) and
                   an error message (or None if no error).
        """
        current_year = datetime.now().year
        try:
            min_rating = float(min_rating_input) if min_rating_input else None
            if min_rating is not None and (min_rating < 0 or min_rating > 10):
                return [], "Rating should be between 0 and 10"
        except ValueError:
            return [], "Invalid input for minimum rating. Please enter a number or leave it blank"
        try:
            start_year = int(start_year_input) if start_year_input else None
            if start_year is not None and (start_year < 1888 or start_year > current_year):
                return [], f"Start year must be between 1888 and {current_year}"
        except ValueError:
            return [], "Invalid input for the start year. Please enter a number or leave it blank"
        try:
            end_year = int(end_year_input) if end_year_input else None
            if end_year is not None and (end_year < 1888 or end_year > current_year):
                return [], f"End year must be between 1888 and {current_year}"
        except ValueError:
            return [], "Invalid input for the end year. Please enter a number or leave it blank"
        movies = self._storage.list_movies()
        filtered_movies = [
            (
                movie,
                int(details['year']),
                float(details['rating']),
                details['poster'],
                details.get('note')
            )
            for movie, details in movies.items() if (min_rating is None or float(details['rating']) >= min_rating)
            and (start_year is None or int(details['year']) >= start_year)
            and (end_year is None or int(details['year']) <= end_year)
        ]
        return filtered_movies, None
