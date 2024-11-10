class MovieStats:
    def __init__(self, storage):
        self._storage = storage

    def movies(self):
        return self._storage.list_movies()

    def collect_ratings_float(self):
        movies = self.movies()
        return [float(movie["rating"]) for movie in movies.values()]

    def calc_avg(self):
        ratings = self.collect_ratings_float()
        return sum(ratings) / len(ratings) if ratings else None

    def calc_mean(self):
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
        ratings = self.collect_ratings_float()
        return max(ratings) if ratings else None

    def lowest_rating(self):
        ratings = self.collect_ratings_float()
        return min(ratings) if ratings else None

    def highest_rated_movies(self):
        movies = self.movies()
        highest = self.highest_rating()
        return [title for title, details in movies.items() if float(movies[title]["rating"]) == highest]

    def lowest_rated_movies(self):
        movies = self.movies()
        lowest = self.lowest_rating()
        return [title for title, details in movies.items() if float(movies[title]["rating"]) == lowest]

