from movie_app import MovieApp
from storage_json import StorageJson


# initialize storage and app
storage = StorageJson()
app = MovieApp(storage)


def main():
    # Initialize a dispatcher dictionary
    menu_options = {
        0: app.exit_program,
        1: app.list_movies,
        2: app.add_movie,
        3: app.delete_movie,
        4: app.update_movie,
        5: app.stats,
        6: app.random_movie,
        7: app.search_movie,
        8: app.movies_sorted_by_rating,
        9: app.create_histogram_and_save,
        10: app.movies_sorted_by_chronological_order,
        11: app.filter_movies
    }
    app.welcome_page()
    while True:
        user_input = app.main_menu()
        # Call the corresponding function or return if not valid
        func = menu_options.get(user_input, app.returner_func)
        func()


if __name__ == '__main__':
    main()
