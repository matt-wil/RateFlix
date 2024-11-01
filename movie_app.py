# Welcome to Matt's Epic Movie Dictionary!
import time
from fuzzywuzzy import process
import Levenshtein
import matplotlib.pyplot as plt
import random
from old_app import movie_data
import sys
from colorama import Fore, Style, Back, init
import datetime
import textwrap
init(autoreset=True)

# Error Logs
import logging
logging.basicConfig(
    level=logging.ERROR, format='%(asctime)s - %(levelname)s - %(message)s', handlers=[
        logging.FileHandler('app_errors.log'),
        logging.StreamHandler()
    ]
)


class MovieApp:
    """
    A class representing a movie management application.

    Allows the user to interact with a collection of movies providing
    functionalities such as listing, adding, deleting
    updating movies, generating statistics and much more.

    Methods:
    __init__(storage):
        initializes the movie app with a provided storage
    welcome_page():
        Display an animated Ascii welcome message
    main_menu():
        Displays the main menu options, handles user input, and returns the selected option.
    returner_func():
        Waits for the user to press Enter to return to the main menu.
    list_movies():
        Lists all movies stored in the app and prompts the user to return to the main menu.
    add_movie():
        Prompts the user for movie details, adds a new movie to the collection, and confirms the addition.
    delete_movie():
        Prompts the user to select a movie to delete, removes it from the collection, and confirms the deletion.
    update_movie():
        Prompts the user to select a movie and update its details, and confirms the update.
    movie_stats():
        Calculates and displays statistics for the movie collection, such as average rating and total movies.
    random_movie():
        Selects and displays a random movie from the collection.
    search_movie():
        Prompts the user for a search term and displays matching movies from the collection.
    movie_sort():
        Sorts movies by a chosen attribute (e.g., title, rating) and displays the sorted list.
    generate_histogram():
        Generates a histogram based on movie ratings to visualize rating distribution.
    save_and_exit():
        Saves the current movie data to storage and exits the application.
    download_poster():
        Prompts the user for a movie title and attempts to download its poster image from an external source.

    """
    def __init__(self, storage):
        """
        initializing the RateFlix Movie App with the storage instance to manage data.
        :param storage: (Storage(class)) instance of the storage class to retrieve and save data.
        """
        self._storage = storage

    def welcome_page(self):
        """
        my little welcome to my app message!
        :return: Print statement
        """

        def lazy_print(text, step=50):
            for char in text:
                print(char, end="", flush=True)
                time.sleep(step / 1000)

        ascii_title = r"""
     ▄         ▄  ▄▄▄▄▄▄▄▄▄▄▄  ▄            ▄▄▄▄▄▄▄▄▄▄▄  ▄▄▄▄▄▄▄▄▄▄▄  ▄▄       ▄▄  ▄▄▄▄▄▄▄▄▄▄▄
    ▐░▌       ▐░▌▐░░░░░░░░░░░▌▐░▌          ▐░░░░░░░░░░░▌▐░░░░░░░░░░░▌▐░░▌     ▐░░▌▐░░░░░░░░░░░▌
    ▐░▌       ▐░▌▐░█▀▀▀▀▀▀▀▀▀ ▐░▌          ▐░█▀▀▀▀▀▀▀▀▀ ▐░█▀▀▀▀▀▀▀█░▌▐░▌░▌   ▐░▐░▌▐░█▀▀▀▀▀▀▀▀▀
    ▐░▌       ▐░▌▐░▌          ▐░▌          ▐░▌          ▐░▌       ▐░▌▐░▌▐░▌ ▐░▌▐░▌▐░▌
    ▐░▌   ▄   ▐░▌▐░█▄▄▄▄▄▄▄▄▄ ▐░▌          ▐░▌          ▐░▌       ▐░▌▐░▌ ▐░▐░▌ ▐░▌▐░█▄▄▄▄▄▄▄▄▄
    ▐░▌  ▐░▌  ▐░▌▐░░░░░░░░░░░▌▐░▌          ▐░▌          ▐░▌       ▐░▌▐░▌  ▐░▌  ▐░▌▐░░░░░░░░░░░▌
    ▐░▌ ▐░▌░▌ ▐░▌▐░█▀▀▀▀▀▀▀▀▀ ▐░▌          ▐░▌          ▐░▌       ▐░▌▐░▌   ▀   ▐░▌▐░█▀▀▀▀▀▀▀▀▀
    ▐░▌▐░▌ ▐░▌▐░▌▐░▌          ▐░▌          ▐░▌          ▐░▌       ▐░▌▐░▌       ▐░▌▐░▌
    ▐░▌░▌   ▐░▐░▌▐░█▄▄▄▄▄▄▄▄▄ ▐░█▄▄▄▄▄▄▄▄▄ ▐░█▄▄▄▄▄▄▄▄▄ ▐░█▄▄▄▄▄▄▄█░▌▐░▌       ▐░▌▐░█▄▄▄▄▄▄▄▄▄
    ▐░░▌     ▐░░▌▐░░░░░░░░░░░▌▐░░░░░░░░░░░▌▐░░░░░░░░░░░▌▐░░░░░░░░░░░▌▐░▌       ▐░▌▐░░░░░░░░░░░▌
     ▀▀       ▀▀  ▀▀▀▀▀▀▀▀▀▀▀  ▀▀▀▀▀▀▀▀▀▀▀  ▀▀▀▀▀▀▀▀▀▀▀  ▀▀▀▀▀▀▀▀▀▀▀  ▀         ▀  ▀▀▀▀▀▀▀▀▀▀▀

               ▄▄▄▄▄▄▄▄▄▄▄  ▄▄▄▄▄▄▄▄▄▄▄
              ▐░░░░░░░░░░░▌▐░░░░░░░░░░░▌
               ▀▀▀▀█░█▀▀▀▀ ▐░█▀▀▀▀▀▀▀█░▌
                   ▐░▌     ▐░▌       ▐░▌
                   ▐░▌     ▐░▌       ▐░▌
                   ▐░▌     ▐░▌       ▐░▌
                   ▐░▌     ▐░▌       ▐░▌
                   ▐░▌     ▐░▌       ▐░▌
                   ▐░▌     ▐░█▄▄▄▄▄▄▄█░▌
                   ▐░▌     ▐░░░░░░░░░░░▌
                    ▀       ▀▀▀▀▀▀▀▀▀▀▀

     ▄▄▄▄▄▄▄▄▄▄▄  ▄▄▄▄▄▄▄▄▄▄▄  ▄▄▄▄▄▄▄▄▄▄▄  ▄▄▄▄▄▄▄▄▄▄▄  ▄▄▄▄▄▄▄▄▄▄▄  ▄            ▄▄▄▄▄▄▄▄▄▄▄  ▄       ▄
    ▐░░░░░░░░░░░▌▐░░░░░░░░░░░▌▐░░░░░░░░░░░▌▐░░░░░░░░░░░▌▐░░░░░░░░░░░▌▐░▌          ▐░░░░░░░░░░░▌▐░▌     ▐░▌
    ▐░█▀▀▀▀▀▀▀█░▌▐░█▀▀▀▀▀▀▀█░▌ ▀▀▀▀█░█▀▀▀▀ ▐░█▀▀▀▀▀▀▀▀▀ ▐░█▀▀▀▀▀▀▀▀▀ ▐░▌           ▀▀▀▀█░█▀▀▀▀  ▐░▌   ▐░▌
    ▐░▌       ▐░▌▐░▌       ▐░▌     ▐░▌     ▐░▌          ▐░▌          ▐░▌               ▐░▌       ▐░▌ ▐░▌
    ▐░█▄▄▄▄▄▄▄█░▌▐░█▄▄▄▄▄▄▄█░▌     ▐░▌     ▐░█▄▄▄▄▄▄▄▄▄ ▐░█▄▄▄▄▄▄▄▄▄ ▐░▌               ▐░▌        ▐░▐░▌
    ▐░░░░░░░░░░░▌▐░░░░░░░░░░░▌     ▐░▌     ▐░░░░░░░░░░░▌▐░░░░░░░░░░░▌▐░▌               ▐░▌         ▐░▌
    ▐░█▀▀▀▀█░█▀▀ ▐░█▀▀▀▀▀▀▀█░▌     ▐░▌     ▐░█▀▀▀▀▀▀▀▀▀ ▐░█▀▀▀▀▀▀▀▀▀ ▐░▌               ▐░▌        ▐░▌░▌
    ▐░▌     ▐░▌  ▐░▌       ▐░▌     ▐░▌     ▐░▌          ▐░▌          ▐░▌               ▐░▌       ▐░▌ ▐░▌
    ▐░▌      ▐░▌ ▐░▌       ▐░▌     ▐░▌     ▐░█▄▄▄▄▄▄▄▄▄ ▐░▌          ▐░█▄▄▄▄▄▄▄▄▄  ▄▄▄▄█░█▄▄▄▄  ▐░▌   ▐░▌
    ▐░▌       ▐░▌▐░▌       ▐░▌     ▐░▌     ▐░░░░░░░░░░░▌▐░▌          ▐░░░░░░░░░░░▌▐░░░░░░░░░░░▌▐░▌     ▐░▌
     ▀         ▀  ▀         ▀       ▀       ▀▀▀▀▀▀▀▀▀▀▀  ▀            ▀▀▀▀▀▀▀▀▀▀▀  ▀▀▀▀▀▀▀▀▀▀▀  ▀       ▀
     """
        lazy_print(ascii_title, step=3)
        time.sleep(2)

    def main_menu(self):
        """
        Printing the menu options and running the user input for the menu with a While, try, except and if statement.
        Asking for the user input and making sure its only digits between 1-9.
        :return: Integer -- user_menu_input
        """
        while True:
            print()
            print(Fore.CYAN + Style.BRIGHT + "Lets check out the menu!")
            print()
            print(Fore.LIGHTWHITE_EX + "Menu:")
            print(Fore.RED + "0. Exit")
            print(Fore.LIGHTWHITE_EX + "1. List movies")
            print(Fore.LIGHTWHITE_EX + "2. Add movie")
            print(Fore.LIGHTWHITE_EX + "3. Delete movie")
            print(Fore.LIGHTWHITE_EX + "4. Update movie")
            print(Fore.LIGHTWHITE_EX + "5. Stats")
            print(Fore.LIGHTWHITE_EX + "6. Random movie")
            print(Fore.LIGHTWHITE_EX + "7. Search movie")
            print(Fore.LIGHTWHITE_EX + "8. Movies sorted by rating")
            print(Fore.LIGHTWHITE_EX + "9. Create a histogram")
            print(Fore.LIGHTWHITE_EX + "10. Movies sorted by Chronological order")
            print(Fore.LIGHTWHITE_EX + "11. Filter movies")
            print()

            user_menu_input = input(Fore.LIGHTGREEN_EX + "Enter choice (0-11): \n >>> ")

            if user_menu_input.strip() == "":
                print(Fore.MAGENTA + "You forget to enter a menu number!")
                continue

            try:
                user_menu_input = int(user_menu_input)
                if 0 <= user_menu_input <= 11:
                    return user_menu_input
                else:
                    print(Fore.MAGENTA + "Please enter a number between 0-11")

            except ValueError:
                print(Fore.MAGENTA + "Enter only numbers please!")
            except Exception as e:
                logging.error(e)
                print(f"{Fore.RED + Back.BLACK}Something went wrong! \n Error message: {e}")

    def returner_func(self):
        """
        This function will play after every finished menu option in order for the user to press enter and return to menu.
        :return: User input 'ENTER' key.
        """
        input(Fore.CYAN + Style.BRIGHT + "Please press enter to return to the main menu!")

    def list_movies(self):
        """
        this function will print a list of every movie in the Dictionary of movies.
        then run the 'returner' function.
        :return:
        """
        movies = self._storage.list_movies()
        print(f"\nThere are {len(movies.keys())} movies currently in the RateFlix library.")
        for movie, details in movies.items():
            print(Fore.CYAN + movie)
            print(f"\thas a rating of {Fore.YELLOW}{details['rating']}")
            print(f"\twas released in {Fore.YELLOW}{details['year']}\n")
        self.returner_func()

    def add_movie(self):
        """
        Asking the user to input to add a movie and its rating to the dictionary.
        using try, except, if and else statements to get as much error handling as possible.
        :return: returning to our dictionary. Key - String and Value - Integer
        """
        movies = self._storage.list_movies()
        try:
            movie_to_add = input(Fore.LIGHTGREEN_EX + "What Movie would you like to add to the RateFlix library?\n>>> ")
            if not movie_to_add:
                raise ValueError("You didn't type a movie name")

            movie_rating = float(input(Fore.LIGHTGREEN_EX + "Enter a rating: \n>>> "))
            movie_year = (int(input(Fore.LIGHTGREEN_EX + "Enter the year of release \n>>> ")))

            # get current year
            current_year = datetime.datetime.now().year
            if 1988 <= movie_year <= current_year:
                if movie_to_add in movies:
                    print(Fore.CYAN + "Movie is already in the Library."
                                      "Taking you back to the main menu")
                    self.returner_func()
                    return

                elif 0 <= movie_rating <= 10:
                    self._storage.add_movie(movie_to_add, movie_rating, movie_year)
                    print(
                        f"You successfully added {Fore.YELLOW}{movie_to_add}{Fore.RESET}.\nReleased in {Fore.YELLOW}{movie_year}{Fore.RESET} and has a rating of {Fore.YELLOW}{movie_rating}{Fore.RESET}!")
                else:
                    print("Rating must be between 0-10")
            else:
                print(f"{Fore.RED}That cant be right!")
                fun_fact1 = f"{Fore.MAGENTA}Fun fact: {Fore.LIGHTWHITE_EX}did you know In Leeds, England Louis Le Prince films Roundhay Garden Scene is believed to be the first motion picture recorded created in 1888.\nBut it is possible to argue (as many film historians do) that the first ever “movie” was Eadweard Muybridge's The Horse In Motion in 1878, a sequence of a dozen photographs of a horse which, when viewed together, conveyed the sense of the horse literally being in motion."
                print(self.long_text_wrapper(fun_fact1))

        except ValueError:
            print(Fore.RED + "Please enter something Valid!")
        except Exception as e:
            logging.error(e)
            print(f"{Fore.RED + Back.BLACK}Something went wrong... \nError message {e} \nPlease try again!")
        self.returner_func()

    def delete_movie(self):
        """
        Asking user input to delete an item from our Dictionary.
        Firstly checking if the item is there and error handling if it's not there or if the input is incorrect.
        Otherwise the function follows through with the task and deletes the chosen item from the dictionary.
        :return: Formatted Print statement.
        """
        movies = self._storage.list_movies()
        movie_to_delete = input(Fore.LIGHTGREEN_EX + "Enter the movie you would like to delete: \n >>> ")
        try:
            if movie_to_delete in movies:
                self._storage.delete_movie(movie_to_delete)
                print(f"{Fore.YELLOW}{movie_to_delete}{Fore.RESET} was deleted from the RateFlix library.")
            else:
                print(f"{Fore.YELLOW}{movie_to_delete}{Fore.RESET} is not in the RateFlix library.")
        except Exception as e:
            logging.error(e)
            print(f"{Fore.RED + Back.BLACK}Oh oh! Something went wrong.\nError message: {e}")
        self.returner_func()

    def update_movie(self):
        """
        Updates an existing movie's rating in the RateFlix library.
        The user is prompted to provide the movie title and a new rating.
        :return: F-Strings
        """
        movies = self._storage.list_movies()

        update_movie_name = input(
            Fore.LIGHTGREEN_EX + "Which movie would you like to update in the RateFlix library? \n >>> ")
        if update_movie_name in movies:
            try:
                rating_to_give = float(
                    input(Fore.LIGHTGREEN_EX + "What's the new rating you would like to give the movie? \n >>> "))
                if 0 <= rating_to_give <= 10:
                    self._storage.update_movie(update_movie_name, rating_to_give)
                    print(
                        f"{Fore.YELLOW}{update_movie_name}{Fore.RESET} updated in RateFlix library with a rating of: {Fore.YELLOW}{rating_to_give}")
                else:
                    print(Fore.RED + "Movie ratings are between 0 and 10...")
            except ValueError:
                print(Fore.RED + "Incorrect input")
            except Exception as e:
                print(Fore.RED + Back.BLACK + f"Oh ohh!!\nError code: {e}")
        else:
            print(f"Well {Fore.YELLOW}{update_movie_name}{Fore.RESET} is not there! Maybe you should add it!")
        self.returner_func()

    def stats(self):
        """
        Access the movies.json file to make the required calculations to provide the statistics needed for our print statements
        :return: (F-string) print statistics = Average and Mean plus the Best and Worst movies
        """
        movies = self._storage.list_movies()

        # calculate average
        ratings = [movie["rating"] for movie in movies.values()]
        if ratings:
            average = sum(ratings) / len(ratings)
            print(f"The Average rating is: {Fore.YELLOW}{average:.2f}")
        else:
            print(Fore.RED + "No movies to calculate average.")
            return

        # calculate mean
        sorted_ratings = sorted(ratings)
        num_movies = len(sorted_ratings)

        if num_movies % 2 == 1:
            median = sorted_ratings[num_movies // 2]
        else:
            median = (sorted_ratings[num_movies // 2 - 1] + sorted_ratings[num_movies // 2]) / 2
        print(f"The Median rating is: {Fore.YELLOW}{median:.2f}")

        # find highest and lowest rating
        ratings = [movies[title]["rating"] for title in movies]
        highest_rating = max(ratings)
        lowest_rating = min(ratings)
        highest_rated_movies = [title for title in movies if movies[title]["rating"] == highest_rating]
        lowest_rated_movies = [title for title in movies if movies[title]["rating"] == lowest_rating]

        print("Highest Rated Movies:")
        for movie in highest_rated_movies:
            print(f"\t{Fore.YELLOW}{movie}{Fore.RESET} - Rating: {Fore.YELLOW}{highest_rating}")

        print("\nLowest Rated Movies:")
        for movie in lowest_rated_movies:
            print(f"\t{Fore.YELLOW}{movie}{Fore.RESET} - Rating: {Fore.YELLOW}{lowest_rating}")

        self.returner_func()

    def random_movie(self):
        """
        print a random movie from the dictionary and then call returner function
        :return: print statement
        """
        movies = self._storage.list_movies()
        the_random_movie, val = random.choice(list(movies.items()))
        print(
            f"Random movie is: {Fore.YELLOW}{the_random_movie}{Fore.RESET}, released in {Fore.YELLOW}{val["year"]}{Fore.RESET} with a rating of {Fore.YELLOW}{val["rating"]}")
        self.returner_func()

    def search_movie(self):
        """
        asking for user input to search the dictionary. stripping and lowercasing to remove case sensitivity and space amounts.
         firstly we search for an exact match, then we move to fuzzy method to check for partial matches.
         lastly move to the Levenshtein distance to pick up any other possible matches.
        :return: a Formatted string with the title and rating taken from the movies' dictionary.
        """
        movies = self._storage.list_movies()
        search_item = input(Fore.LIGHTGREEN_EX + "Please type what movie your searching for? \n >>> ").strip().lower()
        lower_movies = {title.lower(): title for title in movies.keys()}

        # Exact user input
        if search_item in lower_movies:
            exact_search = lower_movies[search_item]
            print(
                f"{Fore.YELLOW}{exact_search.capitalize()}{Fore.RESET}, released in {Fore.YELLOW}{movies[exact_search]["year"]}{Fore.RESET} has a rating of {Fore.YELLOW}{movies[exact_search]["rating"]}")
            self.returner_func()

        # Fuzzy matching
        movies_list = list(movies.keys())
        fuzzy_matches = process.extract(search_item, movies_list, limit=5)
        fuzzy_results = [(title, score) for title, score in fuzzy_matches if score > 50]

        if fuzzy_results:
            print(Fore.CYAN + "Found the following fuzzy movies: ")
            for title, score in fuzzy_results:
                print(
                    f"{Fore.YELLOW}{title}{Fore.RESET} released in {Fore.YELLOW}{movies[title]["year"]}{Fore.RESET} has a rating of {Fore.YELLOW}{movies[title]["rating"]}")

        # If Fuzzy cant match it goes to the levenshtein distance.
        else:
            distances = [
                (title, Levenshtein.distance(search_item, title.lower()))
                for title in movies.keys()
            ]
            sorted_distances = sorted(distances, key=lambda x: x[1])

            top_matches = sorted_distances[:5]

            if top_matches:
                print(Fore.CYAN + "Found the following movies: ")
                for title, distance in top_matches:
                    print(
                        f"{Fore.YELLOW}{title}{Fore.RESET} released in {Fore.YELLOW}{movies[title]["year"]}{Fore.RESET} has a rating of {Fore.YELLOW}{movies[title]}")
            else:
                print(Fore.RED + "No movies found matching your search.")
        self.returner_func()

    def movies_sorted_by_rating(self):
        """
        Here we just sort the dictionary of movies by its values from highest to lowest using the key=lambda function and
        reverse to make sure it starts with the highest rated movie to the lowest
        :return: Formatted print statement
        """
        movies = self._storage.list_movies()
        sorted_movies = dict(sorted(movies.items(), key=lambda item: item[1]["rating"], reverse=True))

        print(Fore.CYAN + "Movies sorted by rating:")
        for movie, details in sorted_movies.items():
            print(
                f"{Fore.YELLOW}{movie}{Fore.RESET}: Rating: {Fore.YELLOW}{details["rating"]}{Fore.RESET}, Year: {Fore.YELLOW}{details["year"]}")
        self.returner_func()

    def create_histogram_and_save(self):
        """
        Here we turn all dictionary values into a list and using matplotlib library and the hist() function we create a histogram.
        Then ask the user under what name they would like the histogram to be saved under.
        :return: saved Histogram .png file
        """
        movies = self._storage.list_movies()
        movie_ratings = [val["rating"] for val in movies.values()]

        plt.hist(movie_ratings, bins=5, color='blue', edgecolor='black')
        plt.title("Movie Ratings Histogram")
        plt.xlabel("Rating")
        plt.ylabel("Number of Movies")

        filename = input("Please enter a file name to save the histogram.\n>>> ")
        if not filename.endswith(".png"):
            filename += ".png"
        plt.savefig(filename)

        plt.show()

    def exit_program(self):
        print("Thanks for using the RateFlix app!")
        print("Have a wonderful day")
        print(r""" 
            ____             _ 
            | __ ) _   _  ___| |
            |  _ \| | | |/ _ \ |
            | |_) | |_| |  __/_|
            |____/ \__, |\___(_)
                   |___/        
                   """)
        sys.exit()

    def movies_sorted_by_chronological_order(self):
        """
        This function sorts the movies into chronological order and prints them out according to how the user chooses.
        if "Y" latest to earliest.
        if "N" earliest to latest.
        :return: F-String of the movies
        """
        movies = self._storage.list_movies()
        while True:
            user_input = input(
                Fore.LIGHTGREEN_EX + "Would you like not to see the movies from latest movies first? Y/N\n>>> ").upper()
            if user_input == "Y":
                # sort latest to earliest
                sorted_movies = dict(sorted(movies.items(), key=lambda item: item[1]["year"], reverse=True))
                break
            elif user_input == "N":
                # sort earliest to latest
                sorted_movies = dict(sorted(movies.items(), key=lambda item: item[1]["year"], reverse=False))
                break
            else:
                print("Invalid Input, please enter 'Y' or 'N'.")

        print(Fore.CYAN + "Movies sorted by rating:")
        for movie, details in sorted_movies.items():
            print(
                f"{Fore.YELLOW}{movie}{Fore.RESET}: Rating: {Fore.YELLOW}{details["rating"]}{Fore.RESET}, Year: {Fore.YELLOW}{details["year"]}")
        self.returner_func()

    def filter_movies(self):
        """
        This function filters movies based on minimum rating, start year, and end year.
        If any input is left blank, it is considered as no filter for that criterion.
        It also handles invalid input types.
        """
        movies = self._storage.list_movies()

        def validate_input(prompt, cast_type):
            """
            Helper function to get a valid number input.
            Prompts the user for input and attempts to cast it to the specified type (int or float).
            If the input is invalid it will prompt the user again.
            """
            while True:
                user_input = input(Fore.LIGHTGREEN_EX + prompt).strip()
                if not user_input:
                    return None  # return None for blank inputs
                try:
                    return cast_type(user_input)  # try cast to desired type
                except ValueError:
                    print(Fore.RED + "Invalid Input! Please enter a valid number or nothing.")

        min_rating = validate_input("Enter minimum rating (leave blank for no minimum rating)\n>>> ", float)
        start_year = validate_input("Enter start year (leave blank for no start year)\n>>> ", int)
        end_year = validate_input("Enter end year (leave blank for no start year)\n>>> ", int)

        # access movies
        filtered_movies = []
        for movie, details in movies.items():
            rating = details["rating"]
            year = details["year"]

            # Apply filters, respecting empty inputs
            if (min_rating is None or rating >= min_rating) and \
                    (start_year is None or year >= start_year) and \
                    (end_year is None or year <= end_year):
                filtered_movies.append(f"{movie} ({year}): {rating}")

        # output
        if filtered_movies:
            print(Fore.CYAN + "Filtered Movies:")
            for movie in filtered_movies:
                print(Fore.YELLOW + movie)
        else:
            print(Fore.RED + "No movies found matching the criteria")
        self.returner_func()

    def long_text_wrapper(self, text, wrap=80):
        wrapped_text = textwrap.fill(text, width=wrap)
        return wrapped_text






