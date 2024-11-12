import argparse
from model.storage_json import StorageJson
from model.storage_csv import StorageCSV
import command_line_args
from presenter.movie_crud import MovieCrud
from presenter.movie_manager import MovieManager
from presenter.movie_search import MovieSearch
from presenter.movie_stats import MovieStats
from presenter.movie_website_generator import WebsiteGenerator
from view.movieTerminal import MovieAppTerminalUI
import utilities


class MovieApplicationRun:
    """
    Main class to manage the movie application. This class initializes storage, view,
    and other components, and provides a menu-based interface for interacting with the
    movie database.
    Attributes:
        storage (object): The storage system (JSON or CSV) for managing movie data.
        app (MovieAppTerminalUI): The terminal-based user interface.
        menu_options (dict): A dictionary that maps menu choices to functions.
    """
    def __init__(self, storage_type="json"):
        """
        Initializes the MovieApplicationRun with the chosen storage type (JSON or CSV).
        :arg:
            storage_type (str): The type of storage to use ("json" or "csv").
        """
        if storage_type == "csv":
            self.storage = StorageCSV()
        else:
            self.storage = StorageJson()
        crud = MovieCrud(self.storage)
        manager = MovieManager(self.storage)
        stats = MovieStats(self.storage)
        search = MovieSearch(self.storage)
        website_gen = WebsiteGenerator(self.storage)
        self.app = MovieAppTerminalUI(crud, manager, stats, search, website_gen)
        # Initialize a dispatcher dictionary
        self.menu_options = {
            0: lambda: self._execute_and_returner(self.app.exit),
            1: lambda: self._execute_and_returner(self.app.display_all),
            2: lambda: self._execute_and_returner(self.app.add),
            3: lambda: self._execute_and_returner(self.app.delete),
            4: lambda: self._execute_and_returner(self.app.update),
            5: lambda: self._execute_and_returner(self.app.display_stats),
            6: lambda: self._execute_and_returner(self.app.display_random),
            7: lambda: self._execute_and_returner(self.app.search),
            8: lambda: self._execute_and_returner(self.app.display_sorted),
            9: lambda: self._execute_and_returner(self.app.create_histogram),
            10: lambda: self._execute_and_returner(self.app.display_chronologically),
            11: lambda: self._execute_and_returner(self.app.filter),
            12: lambda: self._execute_and_returner(self.app.generate_website),
        }

    def _execute_and_returner(self, func):
        """Executes a function than calls the returner function after"""
        func()
        utilities.returner_func()

    def run(self):
        """Runs the main loop of the app. displaying the menu and responding to user input until exited"""
        # utilities.welcome_page()
        while True:
            user_input = utilities.main_menu()
            # Call the corresponding function or return if not valid
            func = self.menu_options.get(user_input, utilities.returner_func)
            func()


def main():
    """
    Entry point of the application. Parses command-line arguments to determine
    the storage file and type (JSON or CSV) and starts the application.
    """
    # set up argument parsing
    parser = argparse.ArgumentParser(description="Run the movie application with a specified storage file.")
    parser.add_argument("storage_file", type=str, help="Path to the storage file (JSON or CSV).")

    # Parse arguments
    args = parser.parse_args()

    # determine storage type via file extension
    try:
        storage_type = command_line_args.determine_storage_type(args.storage_file)
    except ValueError as e:
        print(f"Error: {e}")
        return

    # create View
    app = MovieApplicationRun(storage_type=storage_type)
    app.run()


if __name__ == '__main__':
    main()
