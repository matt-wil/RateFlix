from fuzzywuzzy import process
import Levenshtein


class MovieSearch:
    def __init__(self, storage, view):
        self._storage = storage
        self._view = view  # this will be the GUI class

    def search_movie(self):
        search_item = self._view.get_search_input()
        movies = self._storage.list_movies()

        # exact match
        exact_match = self.find_exact_match(search_item, movies)
        if exact_match:
            return self._view.show_results(exact_match)

        # fuzzy match
        fuzzy_results = self.find_fuzzy_matches(search_item, movies)
        if fuzzy_results:
            return self._view.show_results(fuzzy_results)

        # levenshtein distance match
        return self.find_levenshtein_matches(search_item, movies)

    def find_exact_match(self, search_item, movies):
        lower_movies = {title.lower(): title for title in movies.keys()}
        if search_item in lower_movies:
            exact_search = lower_movies[search_item]
            return [
                {'title': exact_search, 'year': movies[exact_search]['year'], 'rating': movies[exact_search]['rating']}]
        return None

    def find_fuzzy_matches(self, search_item, movies):
        movies_list = list(movies.keys())
        fuzzy_matches = process.extract(search_item, movies_list, limit=5)
        fuzzy_results = [(title, score) for title, score in fuzzy_matches if score > 50]

        if fuzzy_results:
            return [{'title': title, 'year': movies[title]['year'], 'rating': movies[title]['rating']} for title, score
                    in fuzzy_results]
        return None

    def find_levenshtein_matches(self, search_item, movies):
        distances = [
            (title, Levenshtein.distance(search_item, title.lower())) for title in movies.keys()
                     ]
        sorted_distances = sorted(distances, key=lambda x: x[1])
        top_matches = sorted_distances[:5]
        return [
            {'title': title, 'year': movies[title]['year'], 'rating': movies[title]['rating']}
            for title, distance in top_matches] if top_matches else None
