from fuzzywuzzy import process
import Levenshtein


class MovieSearch:
    """
    A class for searching movies based on exact match, fuzzy match, or Levenshtein distance.

    Methods:
        __init__(storage, view):
            Initializes the MovieSearch with a storage object.

        search_movie():
            Searches for a movie using exact match, fuzzy match, or Levenshtein distance, and displays results.

        find_exact_match(search_item, movies):
            Finds an exact match for the search item in the movie list.

        find_fuzzy_matches(search_item, movies):
            Finds fuzzy matches for the search item in the movie list using fuzzy string matching.

        find_levenshtein_matches(search_item, movies):
            Finds movies whose titles have a Levenshtein distance of less than 5 from the search item.
    """

    def __init__(self, storage):
        """
        Initializes the MovieSearch instance with a storage.
        :arg:
            storage: An instance of the storage class responsible for managing movie data.
        """
        self._storage = storage

    def search_movie(self, search_item):
        """
        Searches for a movie based on the search item entered by the user. It first tries exact matching,
        then fuzzy matching, and finally Levenshtein distance matching.
        :return: (dict): A dictionary with movie details (title, year, rating, etc.) for the matched movies,
                        or None if no matches are found.
        """
        movies = self._storage.list_movies()

        # exact match
        exact_match = self.find_exact_match(search_item, movies)
        if exact_match:
            return exact_match

        # fuzzy match
        fuzzy_results = self.find_fuzzy_matches(search_item, movies)
        if fuzzy_results:
            return fuzzy_results

        # levenshtein distance match
        return self.find_levenshtein_matches(search_item, movies)

    @staticmethod
    def find_exact_match(search_item, movies):
        """
        Finds an exact match for the search item in the movie list.
        :arg:
            search_item (str): The movie title to search for.
            movies (dict): A dictionary of movies where the key is the movie title.

        :return: (list): A list of movie details for the exact match or None if no match is found.
        """
        lower_movies = {title.lower(): title for title in movies.keys()}
        if search_item in lower_movies:
            exact_search = lower_movies[search_item]
            return [
                {
                    'title': exact_search,
                    'year': movies[exact_search].get('year'),
                    'rating': movies[exact_search].get('rating'),
                    'poster': movies[exact_search].get('poster'),
                    'country': movies[exact_search].get('country'),
                    'note': movies[exact_search].get('note')
                }
            ]
        return None

    @staticmethod
    def find_fuzzy_matches(search_item, movies):
        """
        Finds fuzzy matches for the search item in the movie list using fuzzy string matching.
        :arg:
            search_item (str): The movie title to search for.
            movies (dict): A dictionary of movies where the key is the movie title.
        :return: (list): A list of movie details for the fuzzy matches with scores greater than 50,
                  or None if no matches are found.
        """
        movies_list = list(movies.keys())
        fuzzy_matches = process.extract(search_item, movies_list, limit=5)
        fuzzy_results = [(title, score) for title, score in fuzzy_matches if score > 50]

        if fuzzy_results:
            return [
                {
                    'title': title,
                    'year': movies[title].get('year'),
                    'rating': movies[title].get('rating'),
                    'poster': movies[title].get('poster'),
                    'country': movies[title].get('country'),
                    'note': movies[title].get('note')
                }
                for title, score in fuzzy_results]
        return None

    @staticmethod
    def find_levenshtein_matches(search_item, movies):
        """
        Finds movies whose titles have a Levenshtein distance of less than 5 from the search item.
        :arg:
            search_item (str): The movie title to search for.
            movies (dict): A dictionary of movies where the key is the movie title.
        :return: (list): A list of movie details for the top matches based on Levenshtein distance,
                  or None if no matches are found.
        """
        distances = [
            (title, Levenshtein.distance(search_item, title.lower())) for title in movies.keys()
        ]
        sorted_distances = sorted(distances, key=lambda x: x[1])
        top_matches = [match for match in sorted_distances if match[1] < 5][:5]
        return [
            {
                'title': title,
                'year': movies[title].get('year'),
                'rating': movies[title].get('rating'),
                'poster': movies[title].get('poster'),
                'country': movies[title].get('country'),
                'note': movies[title].get('note')
            }
            for title, distance in top_matches] if top_matches else None
