import utilities
from colorama import Fore, Style, Back
from view.Base_UI import BaseUI
import time
import logs.logging_handler


class MovieAppTerminalUI(BaseUI):
    def __init__(self, presenter):
        self.presenter = presenter
        self.movies = self.presenter.list_movies()

    def welcome_page(self):
        utilities.welcome_page()

    def main_menu(self):
        utilities.main_menu()

    def display_all(self):
        utilities.display_all(self.movies)

    def add(self):
        utilities.add(self.movies, self._storage)

    def delete(self):
        movies = self._storage.list_movies()
        movie_to_delete = input(Fore.LIGHTGREEN_EX + "Enter the movie you would like to delete: \n >>> ")
        try:
            if movie_to_delete in movies:
                self._storage.delete_movie(movie_to_delete)
                print(f"{Fore.YELLOW}{movie_to_delete}{Fore.RESET} was deleted from the PopcornPicker library.")
            else:
                print(f"{Fore.YELLOW}{movie_to_delete}{Fore.RESET} is not in the PopcornPicker library.")
        except Exception as e:
            logs.logging_handler.logging.error(e)
            print(f"{Fore.RED + Back.BLACK}Oh oh! Something went wrong.\nError message: {e}")
        utilities.returner_func()

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
