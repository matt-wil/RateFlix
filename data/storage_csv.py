from os.path import join
from data.istorage import IStorage
import csv
import os


class StorageCSV(IStorage):
    """
        Child of the Abstract(IStorage) class in order to work with accessing and saving files under csv format.
        Methods:
            __init__(file_path):
                initialise the StorageCsv object with the file_path for the file.
            list_movies:
                read the csv file and return a dictionary to be accesses within the program.
            add_movie(title, rating, year):
                if the file is not there the file will then be created.
                reads the csv file, receive the title, rating and
                year from the user and adds the movie into the dictionary
                then saves the dictionary back into the json file
            delete_movie(title):
                reads the csv file and checks if the given title is in the file. if so the movie is deleted and the file resaved.
            update_movie(title, rating):
                reads the csv file if the given title is there it will update the rating and resave the file.
            _save_movies(movies):
                writes/saves the movies dictionary back to the movies.csv file.

        """
    def __init__(self, file_path=join("storage", "movies.csv")):
        self.file_path = file_path

    def list_movies(self):
        """
        reads the movies.csv file and returns a dictionary in the correct format to be worked with.
        :return: (dict) "title": title, "rating": rating, "year", year
        """
        movies = {}
        try:
            with open(self.file_path, mode="r", newline="") as csv_file:
                reader = csv.DictReader(csv_file)
                for row in reader:
                    movies[row["title"]] = {
                        "rating": row["rating"],
                        "year": row["year"],
                        "poster": row["poster"],
                        "note": row["note"]
                    }
        except FileNotFoundError:
            pass
        return movies

    def update_movie(self, title: str, note: str):
        movies = self.list_movies()
        # update the movie rating
        if title in movies:
            movies[title]["note"] = note
            self._save_movies(movies)

    def add_movie(self, title: str, rating: float, year: int, poster: str):
        """
        Adds a new movie to the csv file! if the file doesn't exist it will create the file.
        :param title:
        :param rating:
        :param year:
        :param poster:
        :return:
        """
        file_exists = os.path.isfile(self.file_path)

        with open(self.file_path, mode="a", newline="") as csv_file:
            fieldnames = ["title", "rating", "year", "poster"]
            writer = csv.DictWriter(csv_file, fieldnames=fieldnames)

            if not file_exists:
                writer.writeheader()

            writer.writerow({"title": title, "rating": rating, "year": year, "poster": poster})

    def delete_movie(self, title: str):
        movies = self.list_movies()
        # delete the movie
        if title in movies:
            del movies[title]
            self._save_movies(movies)

    def _save_movies(self, movies: dict):
        with open(self.file_path, mode="w", newline="") as csv_file:
            fieldnames = ["title", "rating", "year", "poster"]
            writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
            writer.writeheader()
            for title, info in movies.items():
                writer.writerow({
                    "title": title,
                    "rating": info["rating"],
                    "year": info["year"],
                    "poster": info["poster"],
                    "note": info["note"]
                })


