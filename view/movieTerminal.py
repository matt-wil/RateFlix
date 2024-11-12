import utilities
from colorama import Fore
from view.Base_UI import BaseUI


class MovieAppTerminalUI(BaseUI):
    """
    Terminal-based user interface for the PopcornPicker Movie Application.
    Provides methods for managing movies, displaying statistics, filtering,
    sorting, generating a website, and interacting with the user.

    Methods:
        welcome_page():
            Displays the welcome page.

        main_menu():
            Displays the main menu.

        display_all():
            Lists all movies in the storage with details such as name, IMDb rating, year of release, and notes.

        add():
            Prompts the user to add a new movie to the library.

        delete():
            Prompts the user to delete a specified movie from the library.

        update():
            Allows the user to add or update notes for a specified movie.

        display_stats():
            Displays movie statistics including highest and lowest ratings and the mean and average ratings.

        display_random():
            Displays a random movie from the library with its details.

        search():
            Allows the user to search for movies by title.

        display_sorted():
            Displays movies sorted by rating from highest to lowest.

        create_histogram():
            Saves a histogram of movie ratings to a file.

        display_chronologically():
            Displays movies in chronological order, allowing the user to choose ascending or descending order.

        filter():
            Allows the user to filter movies by rating and release year range.

        generate_website():
            Generates an HTML website displaying the movie library.

        exit():
            Exits the application.
    """
    def __init__(self, presenter_crud, presenter_manager, presenter_stats, presenter_search, presenter_web_gen):
        """
        Initialising the UI with presenters for different functionality
        :param presenter_crud: Presenter for CRUD operations on movies.
        :param presenter_manager: Presenter for managing and filtering movies
        :param presenter_stats: Presenter for calculating a displaying statistics
        :param presenter_search: Presenter for searching movies
        :param presenter_web_gen: Presenter for generating the HTML Website
        """
        self.presenter_crud = presenter_crud
        self.presenter_manager = presenter_manager
        self.presenter_stats = presenter_stats
        self.presenter_search = presenter_search
        self.presenter_web_gen = presenter_web_gen

    def welcome_page(self):
        """Displays the welcome page with a greeting and basic instructions """
        utilities.welcome_page()

    def main_menu(self):
        """Displays the main menu options"""
        utilities.main_menu()

    def display_all(self):
        """
        Lists all movies in the storage
        displays the name, imdb rating, the year of release and notes if a movie has some.
        :return:
        """
        movies = self.presenter_crud.list_movies()
        print(f"\nThere are {len(movies.keys())} movies currently in the PopcornPicker library.")
        for movie, details in movies.items():
            print(Fore.CYAN + movie)
            print(f"\thas a rating of {Fore.YELLOW}{details['rating']}")
            print(f"\twas released in {Fore.YELLOW}{details['year']}\n")
            if details.get('note'):
                print(f"\tNote: {Fore.YELLOW}{details['note']}\n")

    def add(self):
        """Prompts the user to add a new movie to the library by entering movie title"""
        title = input(
            Fore.LIGHTGREEN_EX + "What Movie would you like to add to the PopcornPicker library?\n>>> ")

        result = self.presenter_crud.add_movie(title)
        if result.get("success"):
            print(result.get("message"))
        else:
            print(f"{result.get('error')}")

    def delete(self):
        """Prompts the user to delete a movie by entering movie name"""
        movie_to_delete = input(Fore.LIGHTGREEN_EX + "Enter the movie you would like to delete: \n >>> ")
        result = self.presenter_crud.delete_movie(movie_to_delete)
        if result.get("success"):
            print(result.get("message"))
        else:
            print(result.get("error"))

    def update(self):
        """Prompts the user to add or update a notation to a certain movie """
        movie_name = input(
            Fore.LIGHTGREEN_EX + "Which movie would you like to add a note to?\n>>> "
        )
        notes = input(Fore.LIGHTGREEN_EX + "What note would you like to add?\n>>> ")
        result = self.presenter_crud.update_movie(movie_name, notes)
        if result.get("success"):
            print(result.get("message"))
        else:
            print(result.get("error"))

    def display_stats(self):
        """Displays statistics on the movie collection, shows mean, average, highest and lowest rated movies"""
        highest_rating = self.presenter_stats.highest_rating()
        lowest_rating = self.presenter_stats.lowest_rating()
        highest_rated_movies = self.presenter_stats.highest_rated_movies()
        lowest_rated_movies = self.presenter_stats.lowest_rated_movies()
        print(f"The Average rating is: {self.presenter_stats.calc_avg():.2f}")
        print(f"The Mean rating is: {self.presenter_stats.calc_mean()}")
        print("\nHighest Rated Movies:")
        for movies in highest_rated_movies:
            print(f"\t{movies} Rating: {highest_rating}")
        print("\nLowest Rated Movies:")
        for movies in lowest_rated_movies:
            print(f"\t{movies} Rating: {lowest_rating}")

    def display_random(self):
        """Displays a random movie and its details"""
        random_movie, details = self.presenter_manager.random_movie()
        print(
            f"Random movie is: {Fore.YELLOW}{random_movie}{Fore.RESET}, "
            f"released in {Fore.YELLOW}{details['year']}{Fore.RESET} "
            f"with a rating of {Fore.YELLOW}{details['rating']}")

    def search(self):
        """Prompts the user to search for a movie title and displays the results"""
        movie_to_search = input(Fore.LIGHTGREEN_EX + "Please type what movie your searching for? \n >>> ").strip().lower()

        search_results = self.presenter_search.search_movie(movie_to_search)

        if search_results:
            print(Fore.CYAN + "\nSearch Results:")
            for result in search_results:
                title = result['title']
                year = result['year']
                rating = result['rating']
                print(
                    f"{Fore.YELLOW}{title}{Fore.RESET} - Released in {Fore.LIGHTGREEN_EX}{year}{Fore.RESET} with a rating of {Fore.LIGHTGREEN_EX}{rating}{Fore.RESET}")
        else:
            print(Fore.RED + "No matches found for your search. Please try again with a different title.")

    def display_sorted(self):
        """Displays all movies sorted by rating from highest to lowest"""
        sorted_movies = self.presenter_manager.sort_by_rating()
        print(Fore.CYAN + "Movies sorted by rating:")
        for movie, details in sorted_movies.items():
            print(
                f"{Fore.YELLOW}{movie}{Fore.RESET}: Rating: {Fore.YELLOW}{details['rating']}{Fore.RESET}, Year: {Fore.YELLOW}{details['year']}")

    def create_histogram(self):
        """Prompts the user for a filename and saves a histogram of movie ratings."""
        filename = input("Please enter a file name to save the histogram.\n>>> ").strip()
        if not filename:
            filename = "movies_histogram.png"
        elif not filename.endswith(".png"):
            filename += ".png"
        self.presenter_manager.create_histogram(filename)
        print(f"Histogram saved as {filename}")

    def display_chronologically(self):
        """Displays movies sorted chronologically. Prompts the user for the choice of earliest or latest first"""
        latest_first = self.presenter_manager.sort_chronologically_latest_first()
        earliest_first = self.presenter_manager.sort_chronologically_earliest_first()
        user_input = input(
            Fore.LIGHTGREEN_EX + "Would you like not to see the movies from latest movies first? Y/N\n>>> ").upper()
        if user_input == "Y":
            # sort latest to earliest
            print(Fore.CYAN + "Movies sorted by rating:")
            for movie, details in latest_first.items():
                print(
                    f"{Fore.YELLOW}{movie}{Fore.RESET}: Rating: {Fore.YELLOW}{details['rating']}{Fore.RESET}, Year: {Fore.YELLOW}{details['year']}")
        elif user_input == "N":
            # sort earliest to latest
            print(Fore.CYAN + "Movies sorted by rating:")
            for movie, details in earliest_first.items():
                print(
                    f"{Fore.YELLOW}{movie}{Fore.RESET}: Rating: {Fore.YELLOW}{details['rating']}{Fore.RESET}, Year: {Fore.YELLOW}{details['year']}")
        else:
            print("Invalid Input, please enter 'Y' or 'N'.")

    def filter(self):
        """Prompts the user for a minimum rating, start year and end year.
        Displays filtered movies based on these inputs"""
        min_rating = input("Enter minimum rating (leave blank for no minimum rating)\n>>> ").strip()
        start_year = input("Enter start year (leave blank for no start year)\n>>> ").strip()
        end_year = input("Enter end year (leave blank for no start year)\n>>> ").strip()

        filtered_movies, error_message = self.presenter_manager.filter_movies(min_rating, start_year, end_year)
        if error_message:
            print(error_message)
        else:
            for movie, year, rating, poster, note in filtered_movies:
                print(f"{movie} was released in {year} and has an imdb rating of {rating}")
                if note:
                    print(f"Note: {note}")

    def generate_website(self):
        """Generates the HTML website"""
        self.presenter_web_gen.generate_website()
        print(f"Website successfully generated")

    @staticmethod
    def exit():
        """Gives a thankyou message and exits the program"""
        print("Thanks for using the PopcornPicker Movie Application!")
        utilities.exit_program()

    def get_search_input(self):
        """Gets the movie search input from the user."""
        return input(
            Fore.LIGHTGREEN_EX + "Please type the title of the movie you're searching for:\n>>> ").strip().lower()