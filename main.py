from movie_app import MovieApp
from storage_json import StorageJson
from storage_csv import StorageCSV


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
            11: self.app.filter_movies
        }

    def run(self):
        self.app.welcome_page()
        while True:
            user_input = self.app.main_menu()
            # Call the corresponding function or return if not valid
            func = self.menu_options.get(user_input, self.app.returner_func)
            func()


if __name__ == '__main__':
    app = MovieApplicationRun()
    app.run()
