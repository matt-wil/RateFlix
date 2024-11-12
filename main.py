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
    def __init__(self, storage_type="json"):
        if storage_type == "csv":
            self.storage = StorageCSV()
        else:
            self.storage = StorageJson()
        crud = MovieCrud(self.storage)
        manager = MovieManager(self.storage)
        stats = MovieStats(self.storage)
        search = MovieSearch(self.storage)
        website_gen = WebsiteGenerator(self.storage)
        view = MovieAppTerminalUI(crud, manager, stats, search, website_gen)
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
        func()
        utilities.returner_func()

    def run(self):
        # utilities.welcome_page()
        while True:
            user_input = utilities.main_menu()
            # Call the corresponding function or return if not valid
            func = self.menu_options.get(user_input, utilities.returner_func)
            func()


def main():
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
