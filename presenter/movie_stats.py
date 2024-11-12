class MovieStats:
    """
        A class to calculate and return various statistical information about movies stored in the database.

        Methods:
            __init__(storage):
                Initializes the MovieStats instance with a storage object for fetching movie data.

            movies():
                Returns a dictionary of all movies stored in the storage.

            collect_ratings_float():
                Collects all movie ratings as float values from the storage and returns them in a list.

            calc_avg():
                Calculates the average rating of all movies and returns the result.

            calc_mean():
                Calculates the median rating of all movies and returns the result.

            highest_rating():
                Returns the highest rating from all movies.

            lowest_rating():
                Returns the lowest rating from all movies.

            highest_rated_movies():
                Returns a list of movie titles that have the highest rating.

            lowest_rated_movies():
                Returns a list of movie titles that have the lowest rating.
        """
    def __init__(self, storage):
        """Initialise with the storage object"""
        self._storage = storage

    def movies(self):
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

    def collect_ratings_float(self):
        """Collects the ratings of all movies and returns them as a list of floats
        :return: (list): a list of floats representing all the ratings."""
        movies = self.movies()
        return [float(movie["rating"]) for movie in movies.values()]

    def calc_avg(self):
        """
        calculates the average rating of all movies
        :return: (float) or None: The average rating if there are ratings.
        """
        ratings = self.collect_ratings_float()
        return sum(ratings) / len(ratings) if ratings else None

    def calc_mean(self):
        """
        Calculates the Median rating of all movies
        :return: (float) or None: The mean rating if there are ratings
        """
        ratings = self.collect_ratings_float()
        if not ratings:
            return None

        # sort ratings and calculate median
        sorted_ratings = sorted(ratings)
        num_of_movies = len(ratings)

        if num_of_movies % 2 == 1:
            return sorted_ratings[num_of_movies // 2]
        else:
            mid = num_of_movies // 2
            return (sorted_ratings[mid - 1] + sorted_ratings[mid]) / 2

    def highest_rating(self):
        """
        Finds and returns the highest rating
        :return: (float) or None: highest rating if available
        """
        ratings = self.collect_ratings_float()
        return max(ratings) if ratings else None

    def lowest_rating(self):
        """
        Finds and returns the lowest rating
        :return: (float) or None: lowest rating if available
        """
        ratings = self.collect_ratings_float()
        return min(ratings) if ratings else None

    def highest_rated_movies(self):
        """
        Retrieves a list of movie titles that have the highest rating
        :return: (list): list of movies with the highest rating
        """
        movies = self.movies()
        highest = self.highest_rating()
        return [title for title, details in movies.items() if float(movies[title]["rating"]) == highest]

    def lowest_rated_movies(self):
        """
        Retrieves a list of movie titles that have the lowest rating
        :return: (list): list of movies with the lowest rating
        """
        movies = self.movies()
        lowest = self.lowest_rating()
        return [title for title, details in movies.items() if float(movies[title]["rating"]) == lowest]

