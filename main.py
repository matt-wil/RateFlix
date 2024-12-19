import argparse
from model.storage_json import StorageJson
from model.storage_csv import StorageCSV
import command_line_args
from presenter.movie_manager import MovieManager
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
        manager = MovieManager(self.storage)
        self.app = MovieAppTerminalUI(manager)
        # Initialize a dispatcher dictionary
        self.menu_options = {
            0: self.app.exit,
            1: self.app.display_all,
            2: self.app.add,
            3: self.app.delete,
            4: self.app.update,
            5: self.app.display_stats,
            6: self.app.display_random,
            7: self.app.search,
            8: self.app.display_sorted,
            9: self.app.create_histogram,
            10: self.app.display_chronologically,
            11: self.app.filter,
            12: self.app.generate_website,
        }

    def run(self):
        """Runs the main loop of the app. displaying the menu and responding to user input until exited"""
        # utilities.welcome_page()
        while True:
            user_input = utilities.main_menu()
            utilities.logging_users_choice(user_input)
            # Call the corresponding function or return if not valid
            func = self.menu_options.get(user_input, utilities.menu_option)
            func()


def main():
    """
    Entry point of the application. Parses command-line arguments to determine
    the storage file and type (JSON or CSV) and starts the application.
    """
    # set up argument parsing
    parser = argparse.ArgumentParser(
        description="Run the movie application with a specified storage file.")
    parser.add_argument("storage_file", type=str,
                        help="Path to the storage file (JSON or CSV).")

    # Parse arguments
    args = parser.parse_args()

    # determine storage type via file extension
    try:
        storage_type = command_line_args.determine_storage_type(
            args.storage_file)
    except ValueError as e:
        print(f"Error: {e}")
        return

    # create View
    app = MovieApplicationRun(storage_type=storage_type)
    app.run()


if __name__ == '__main__':
    main()
