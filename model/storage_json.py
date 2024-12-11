from os.path import join
from model.istorage import IStorage
import json


class StorageJson(IStorage):
    """
    Child of the Abstract(IStorage) class in order to work with accessing and saving files under json format.
    Methods:
        __init__(file_path):
            initialise the StorageJson object with the file_path for the file.
        list_movies:
            read the json file and return a dictionary to be accesses within the program.
        add_movie(title, rating, year):
            reads the json file, receive the title, rating and
            year from the user and adds the movie into the dictionary
            then saves the dictionary back into the json file
        delete_movie(title):
            reads the json file and checks if the given title is in the file.
            If so the movie is deleted and the file resaved.
        update_movie(title, rating):
            reads the json file if the given title is there it will update the rating and resave the file.
        _save_movies(movies):
            writes/saves the movies dictionary back to the movies.json file.

    """

    def __init__(self, file_path=join("model", "movies.json")):
        """Initialise the JSON file with the correct filepath"""
        self.file_path = file_path

    def list_movies(self):
        """read the JSON file and return the file contents in dictionary format
        :return: (dict)  {"title": {
                                    "rating": rating,
                                    "year": year,
                                    "poster": poster,
                                    "imdbID": imdbID,
                                    "country": country,
                                    "note": note
                                    }
                            }"""
        try:
            with open(self.file_path, "r") as json_file:
                return json.load(json_file)
        except FileNotFoundError:
            return {}

    def update_movie(self, title: str, note: str):
        """Read the JSON file update a note into the selected movie and resave the file"""
        movies = self.list_movies()
        if title in movies:
            movies[title]["note"] = note
            self._save_movies(movies)

    def add_movie(self, title: str, rating: float, year: int, poster: str, imdbID: str, country: str):
        """Reads the json file adds a movie into the correct format and then saves the json file"""
        movies = self.list_movies()
        movies[title] = {"rating": rating,
                         "year": year,
                         "poster": poster,
                         "imdbID": imdbID,
                         "country": country,
                         }
        # save back to file
        self._save_movies(movies)

    def delete_movie(self, title: str):
        movies = self.list_movies()
        # delete the movie
        if title in movies:
            del movies[title]
            self._save_movies(movies)

    def _save_movies(self, movies: dict):
        """Saves the JSON file in correct format"""
        with open(self.file_path, "w") as json_file:
            json.dump(movies, json_file, indent=4)
