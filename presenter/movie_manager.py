import random
from os.path import join

from matplotlib import pyplot as plt


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

        plt.hist(movie_ratings, bins=5, color='blue', edgecolor='black')
        plt.title("Movie Ratings Histogram")
        plt.xlabel("Rating")
        plt.ylabel("Number of Movies")

        plt.savefig(join("../histograms", filename))

        plt.show()

    def sort_chronologically_latest_first(self):
        movies = self._storage.list_movies()
        return dict(sorted(movies.items(), key=lambda item: item[1]["year"], reverse=True))

    def sort_chronologically_earliest_first(self):
        movies = self._storage.list_movies()
        return dict(sorted(movies.items(), key=lambda item: item[1]["year"], reverse=False))

    def filter_movies(self, min_rating, start_year, end_year):
        movies = self._storage.list_movies()
        filtered_movies = []
        for movie, details in movies.items():
            rating = float(details["rating"])
            year = int(details["year"])

            # apply filters
            if (min_rating is None or rating >= min_rating) and (start_year is None or year >= start_year) and (end_year is None or year <= end_year):
                filtered_movies.append((movie, year, rating))

