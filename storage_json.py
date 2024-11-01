from istorage import IStorage
import json


class StorageJson(IStorage):
    def __init__(self, file_path="movies.json"):
        self.file_path = file_path

    def list_movies(self):
        try:
            with open(self.file_path, "r") as json_file:
                return json.load(json_file)
        except FileNotFoundError:
            return {}

    def add_movie(self, title, rating, year):
        """Reads the json file adds a movie into the correct format and then saves the json file"""
        movies = self.list_movies()
        movies[title] = {"rating": rating,
                         "year": year
                         }
        # save back to file
        self.save_movies(movies)

    def delete_movie(self, title):
        movies = self.list_movies()
        # delete the movie
        if title in movies:
            del movies[title]
            self.save_movies(movies)

    def update_movie(self, title, rating):
        movies = self.list_movies()
        # update the movie rating
        if title in movies:
            movies[title]["rating"] = rating
            self.save_movies(movies)

    def save_movies(self, movies):
        with open(self.file_path, "w") as json_file:
            json.dump(movies, json_file, indent=4)


