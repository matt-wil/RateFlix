import os.path
import random
from os.path import join
from matplotlib import pyplot as plt
from datetime import datetime


class MovieManager:
    def __init__(self, storage):
        self._storage = storage

    def random_movie(self):
        movies = self._storage.list_movies()
        the_random_movie, details = random.choice(list(movies.items()))
        return the_random_movie, details

    def sort_by_rating(self):
        movies = self._storage.list_movies()
        return dict(sorted(movies.items(), key=lambda item: item[1]["rating"], reverse=True))

    def create_histogram(self, filename="movies_histogram.png"):
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
        movies = self._storage.list_movies()
        return dict(sorted(movies.items(), key=lambda item: item[1]["year"], reverse=True))

    def sort_chronologically_earliest_first(self):
        movies = self._storage.list_movies()
        return dict(sorted(movies.items(), key=lambda item: item[1]["year"], reverse=False))

    def filter_movies(self, min_rating_input, start_year_input, end_year_input):
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
            (movie, int(details['year']), float(details['rating']))
            for movie, details in movies.items() if (min_rating is None or float(details['rating']) >= min_rating)
            and (start_year is None or int(details['year']) >= start_year)
            and (end_year is None or int(details['year']) <= end_year)
        ]

        return filtered_movies, None

