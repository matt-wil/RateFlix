import argparse
import os
from movie_app import MovieApp
from data.storage_json import StorageJson
from data.storage_csv import StorageCSV


class MovieApplicationRun:
    def __init__(self, storage_type="json"):
        if storage_type == "csv":
            self.storage = StorageCSV()
        else:
            self.storage = StorageJson()
        self.app = MovieApp(self.storage)
        # Initialize a dispatcher dictionary
        self.menu_options = {
            0: self.app.exit_program,
            1: self.app.list_movies,
            2: self.app.add_movie,
            3: self.app.delete_movie,
            4: self.app.update_movie,
            5: self.app.stats,
            6: self.app.random_movie,
            7: self.app.search_movie,
            8: self.app.movies_sorted_by_rating,
            9: self.app.create_histogram_and_save,
            10: self.app.movies_sorted_by_chronological_order,
            11: self.app.filter_movies,
            12: self.app.generate_website,
        }

    def run(self):
        self.app.welcome_page()
        while True:
            user_input = self.app.main_menu()
            # Call the corresponding function or return if not valid
            func = self.menu_options.get(user_input, self.app.returner_func)
            func()


def determine_storage_type(file_path: str) -> str:
    """determine the storage type based on the file extension"""
    _, extension = os.path.splitext(file_path)
    extension = extension.lower()

    if extension == ".json":
        return "json"
    elif extension == ".csv":
        return "csv"
    else:
        raise ValueError("Unsupported file type. At this time we only support .json and .csv files.")


def main():
    # set up argument parsing
    parser = argparse.ArgumentParser(description="Run the movie application with a specified storage file.")
    parser.add_argument("storage_file", type=str, help="Path to the storage file (JSON or CSV).")

    # Parse arguments
    args = parser.parse_args()

    # determine storage type via file extension
    try:
        storage_type = determine_storage_type(args.storage_file)
    except ValueError as e:
        print(f"Error: {e}")
        return

    # run the app
    app = MovieApplicationRun(storage_type=storage_type)
    app.run()


if __name__ == '__main__':
    main()
