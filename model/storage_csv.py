from os.path import join
from model.istorage import IStorage
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

    def __init__(self, file_path=join("model", "movies.csv")):
        """Initialise the object with the CSV filepath"""
        self.file_path = file_path

    def list_movies(self):
        """
        reads the movies.csv file and returns a dictionary in the correct format to be worked with.
        :return: (dict)  {"title": {
                                    "rating": rating,
                                    "year": year,
                                    "poster": poster,
                                    "imdbID": imdbID,
                                    "country": country,
                                    "note": note
                                    }
                            }
        """
        movies = {}
        try:
            with open(self.file_path, mode="r", newline="") as csv_file:
                reader = csv.DictReader(csv_file)
                for row in reader:
                    movies[row["title"]] = {
                        # Default value for missing rating
                        "rating": row.get("rating", "N/A"),
                        # Default value for missing year
                        "year": row.get("year", "N/A"),
                        # Default value for missing poster
                        "poster": row.get("poster", "No Poster Available"),
                        # Default value for missing imdbID
                        "imdbID": row.get("imdbID", "Unknown"),
                        # Default value for missing country
                        "country": row.get("country", "Unknown"),
                        # Default value for missing note
                        "note": row.get("note", "No notes available"),
                    }
        except FileNotFoundError:
            pass
        return movies

    def update_movie(self, title: str, note: str):
        """Reads the CSV file and adds in the Note to the dictionary and resaves the file"""
        movies = self.list_movies()
        if title in movies:
            movies[title]["note"] = note
            self._save_movies(movies)

    def add_movie(self, title: str, rating: float, year: int, poster: str, imdbID: str, country: str):
        """
        Adds a new movie to the csv file! if the file doesn't exist it will create the file.
        """
        file_exists = os.path.isfile(self.file_path)

        with open(self.file_path, mode="a", newline="") as csv_file:
            fieldnames = ["title", "rating", "year",
                          "poster", "imdbID", "country", "note"]
            writer = csv.DictWriter(csv_file, fieldnames=fieldnames)

            if not file_exists:
                writer.writeheader()

            writer.writerow({
                "title": title,
                "rating": rating,
                "year": year,
                "poster": poster,
                "imdbID": imdbID,
                "country": country,
                "note": None
            })

    def delete_movie(self, title: str):
        """Reads the CSV file and deletes the given movie if in the file then resaves the file"""
        movies = self.list_movies()
        if title in movies:
            del movies[title]
            self._save_movies(movies)

    def _save_movies(self, movies: dict):
        """Saving method to save the CSV file back into the correct storage format"""
        with open(self.file_path, mode="w", newline="") as csv_file:
            fieldnames = ["title", "rating", "year",
                          "poster", "imdbID", "country", "note"]
            writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
            writer.writeheader()
            for title, info in movies.items():
                writer.writerow({
                    "title": title,
                    "rating": info["rating"],
                    "year": info["year"],
                    "poster": info["poster"],
                    "imdbID": info["imdbID"],
                    "country": info["country"],
                    "note": info["note"],
                })
