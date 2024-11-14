import os.path
import random
from os.path import join
from matplotlib import pyplot as plt
from datetime import datetime
import model.movie_api
from fuzzywuzzy import process
import Levenshtein
import time
from utilities import get_country_code_from_name


class MovieManager:
    """
    A class for managing movies, including operations like sorting, filtering, searching, and creating visualizations.
    Methods:
        __init__(storage):
            Initializes the MovieManager with a storage object for movie data.

        list_movies():
            Retrieves and returns the dictionary of movies from the storage.

        update_movie(movie_name, notes):
            Adds a note to a specified movie and returns a dictionary indicating success or failure.

        add_movie(movie_name):
            Adds a new movie to the storage by fetching its data from the OMDB API and returns a success or error message.

        delete_movie(movie_name):
            Deletes a specified movie from the storage and returns a dictionary indicating success or failure.

        random_movie():
            Returns a randomly selected movie from the stored movies.

        sort_by_rating():
            Sorts the movies by rating in descending order and returns the sorted dictionary.

        create_histogram(filename="movies_histogram.png"):
            Creates and saves a histogram of movie ratings as a PNG file in the 'histograms' directory.

        sort_chronologically(latest_first=True):
            Sorts the movies by their release year in descending or ascending order and returns the sorted dictionary.

        sort_chronologically_earliest_first():
            Sorts the movies by their release year in ascending order and returns the sorted dictionary.

        filter_movies(min_rating_input, start_year_input, end_year_input):
            Filters movies based on the provided rating and release year range and returns the filtered movies with an optional error message.

        search_movie(search_item):
            Searches for a movie by title using exact, fuzzy, and Levenshtein distance matching.

        find_exact_match(search_item, movies):
            Performs an exact match search for a movie title and returns matching movie details or None.

        find_fuzzy_matches(search_item, movies):
            Uses fuzzy string matching to find movie titles similar to the search item and returns movie details for matches.

        find_levenshtein_matches(search_item, movies):
            Finds movie titles with a Levenshtein distance of less than 5 from the search item and returns movie details.

        get_movies_by_country(country):
            Retrieves movies from a specified country by matching against country data.

        get_movies_by_genre(genre):
            Filters movies by genre and returns details for movies matching the specified genre.

        get_average_rating():
            Calculates and returns the average rating of all movies in the storage.

        get_highest_rated_movie():
            Identifies and returns the highest-rated movie and its details.

        get_lowest_rated_movie():
            Identifies and returns the lowest-rated movie and its details.

        save_to_file(filename="movies.json"):
            Saves the movie data to a specified file in JSON format.

        load_from_file(filename="movies.json"):
            Loads movie data from a specified JSON file into the storage.
    """

    def __init__(self, storage):
        """
        Initializes the MovieManager instance with a storage object for managing movie data.
        :arg:
            storage: An instance of a storage class responsible for movie data persistence.
        """
        self._storage = storage

    def list_movies(self) -> dict:
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

    def update_movie(self, movie_name: str, notes: str) -> dict:
        """
        Adds a note to the dictionary and returns a dictionary to be used inside the View class
        :param movie_name: Title of the movie
        :param notes: Notes to be added to the give movie_name
        :return: (dict)
                    Success: {"success": True, "message": f" {notes} added to {movie_name}"}
                    Error: {"success": False, "error": f"{movie_name} not found in the library"}
        """
        movies = self._storage.list_movies()
        if movie_name in movies:
            self._storage.update_movie(movie_name, notes)
            return {"success": True, "message": f"{notes} added to {movie_name}"}
        else:
            return {"success": False, "error": f"{movie_name} not found in the library"}

    def add_movie(self, movie_name: str) -> dict:
        """
        Adds a new movie to the storage by fetching the data from the OMDB API
        :param movie_name: title of the movie
        :return: (dict)
                    Success: {"success": True, "message": f"{movie_name} added successfully to the library"}
                    Error: {"success": False, "error": (The relevant error message)}
        """
        if not movie_name:
            return {"success": False, "error": "Movie name cannot be empty"}

        movies = self._storage.list_movies()
        if movie_name in movies:
            return {"success": False, "error": "Movie is already in the library"}

        try:
            movie, rating, year, poster_url, imdb_full_link, country = model.movie_api.api_extraction(movie_name)
        except Exception as e:
            return {"success": False, "error": f"API Error: {str(e)}"}

        if not movie:
            return {"success": False, "error": "Movie not found in the database"}

        self._storage.add_movie(movie_name, rating, year, poster_url, imdb_full_link, country)
        return {"success": True, "message": f"{movie_name} added successfully to the library"}

    def delete_movie(self, movie_name: str) -> dict:
        """
        Delete a movie from the storage
        :param movie_name: title of the movie
        :return: (dict)
                    Success: {"success": True, "message": f"{movie_name} deleted from the library"}
                    Error: {"success": False, "error": f"{movie_name} was not found in the library"}
        """
        movies = self._storage.list_movies()
        if movie_name in movies:
            self._storage.delete_movie(movie_name)
            return {"success": True, "message": f"{movie_name} deleted from the library"}
        else:
            return {"success": False, "error": f"{movie_name} was not found in the library"}

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

    def sort_chronologically(self, latest_first=True):
        """
        Sorts the movies by their release year in descending or descending order and returns the sorted dictionary.
        :param: latest_first: (bool) True to sort the movies from latest first or False for earliest first
        :return: (dict): A dictionary of movies sorted by release year from latest to earliest.
        """
        movies = self._storage.list_movies()
        return dict(sorted(movies.items(), key=lambda item: item[1]["year"], reverse=latest_first))

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

    def collect_ratings_float(self):
        """Collects the ratings of all movies and returns them as a list of floats
        :return: (list): a list of floats representing all the ratings."""
        movies = self.list_movies()
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
        movies = self.list_movies()
        highest = self.highest_rating()
        return [title for title, details in movies.items() if float(movies[title]["rating"]) == highest]

    def lowest_rated_movies(self):
        """
        Retrieves a list of movie titles that have the lowest rating
        :return: (list): list of movies with the lowest rating
        """
        movies = self.list_movies()
        lowest = self.lowest_rating()
        return [title for title, details in movies.items() if float(movies[title]["rating"]) == lowest]

    def generate_website(self):
        """
        Generates an HTML website displaying a list of movies. For each movie, it includes details such as
        the title, year, rating, poster, country flag, and a link to the IMDb page. The generated website
        is saved as 'index.html' in the 'web' directory.
        The method also adds country flags by fetching the corresponding country code and uses the `get_country_code_from_name` function
        to generate the flag image URL.
        """
        movies = self._storage.list_movies()
        html_content = """
         <!DOCTYPE html>
         <html lang="en">
         <head>
             <meta charset="UTF-8">
             <meta name="viewport" content="width=device-width, initial-scale=1.0">
             <link rel="stylesheet" href="style.css"/>
             <title>PopcornPicker</title>
         </head>
         <body>
         <main>
             <div class="list-movies-title">
                 <h1>PopcornPicker Movie Library</h1>
             </div>
             <div class="list">
         """
        # add all movies to html list
        for title, details in movies.items():
            country_code = get_country_code_from_name(details.get('country'))
            html_content += f"""
                 <div class="movie">
                     <a href="{details.get("imdbID")}" target="_blank">
                         <div class="flag-container">
                             <img class="country-flag" src="https://flagsapi.com/{country_code}/flat/64.png" alt="{details.get('country')} Flag">
                         </div>
                             <img class="movie-poster" src="{details.get("poster")}">
                     </a>
                     <div class="text">
                         <div class="movie-title">{title}</div>
                         <div class="movie-year">{details.get("year")}</div>
                         <div class="movie-rating">iMDb Rating: {details.get("rating")}</div>
                         <div class="movie-note">{details.get("note", "")}</div>
                     </div>
                 </div>
         """

        # closing tags
        html_content += """
             </div>
         </main>
         </body>
         </html>
         """

        # write the HTML content to a file
        with open(join("web", "index.html"), "w") as file:
            file.write(html_content)

        time.sleep(2)
