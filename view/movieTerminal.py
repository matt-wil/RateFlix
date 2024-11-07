import utilities
from colorama import Fore, Style, Back
from userinterfaces.Base_UI import BaseUI
import time


class MovieAppTerminalUI(BaseUI):
    def __init__(self, app_functionality):
        self.app_functionality = app_functionality
        self.movies = self.app_functionality.list_movies()

    def display_all(self):
        """
        receive a dictionary of movies in the storage
        displays the name, imdb rating, the year of release and notes if a movie has some.
        :return:
        """
        print(f"\nThere are {len(self.movies.keys())} movies currently in the PopcornPicker library.")
        for movie, details in self.movies.items():
            print(Fore.CYAN + movie)
            print(f"\thas a rating of {Fore.YELLOW}{details['rating']}")
            print(f"\twas released in {Fore.YELLOW}{details['year']}\n")
        utilities.returner_func()

    def add(self):
        try:
            movie_to_add = input(
                Fore.LIGHTGREEN_EX + "What Movie would you like to add to the PopcornPicker library?\n>>> ")
            if not movie_to_add:
                raise ValueError("You didn't type a movie name")

            if movie_to_add in movies:
                print(Fore.CYAN + "Movie is already in the Library.\n"
                                  "Taking you back to the main menu")
                utilities.returner_func()
                return
            movie_to_add, movie_rating, movie_year, movie_poster, imdb_full_link, country = self.api_extraction(
                movie_to_add, api_key, OMDb_url)
            self._storage.add_movie(movie_to_add, movie_rating, movie_year, movie_poster, imdb_full_link, country)
            print(f"{movie_to_add} successfully added to the PopcornPicker Library. "
                  f"Released in {movie_year} it has a imdb rating of {movie_rating}")
        except Exception as e:
            print(f"Error occurred: {e}")

        utilities.returner_func()

    def delete(self):
        pass

    def update(self):
        update_movie_name = input(
            Fore.LIGHTGREEN_EX + "Which movie would you like to add a note to?\n>>> "
        )
        if self.app_functionality.update_movie(update_movie_name, "") is not None:
            notes = input("What note would you like to add?\n>>> ")
            if notes.strip():
                success = self.app_functionality.update_movie(update_movie_name, notes)
                if success:
                    print("Note successfully added!")
                    utilities.returner_func()
            else:
                print("Please enter a Valid note")
                time.sleep(2)
        else:
            print("Movie not in the Library")
        utilities.returner_func()

    def display_stats(self):
        pass

    def display_random(self):
        pass

    def search(self):
        pass

    def display_sorted(self):
        pass

    def create_histogram(self):
        pass

    def display_chronologically(self):
        pass

    def filter(self):
        pass

    def generate_website(self):
        pass
