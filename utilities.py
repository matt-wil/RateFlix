import sys
import time
from colorama import Fore, Style, Back
import logging
import pycountry
from model.movie_api import api_extraction


def welcome_page():
    """
    my little welcome to my app message!
    :return: Print statement
    """

    def lazy_print(text, step=50):
        for char in text:
            print(char, end="", flush=True)
            time.sleep(step / 1000)

    ascii_title = r"""
____    __    ____  _______  __        ______   ______   .___  ___.  _______ 
\   \  /  \  /   / |   ____||  |      /      | /  __  \  |   \/   | |   ____|
 \   \/    \/   /  |  |__   |  |     |  ,----'|  |  |  | |  \  /  | |  |__   
  \            /   |   __|  |  |     |  |     |  |  |  | |  |\/|  | |   __|  
   \    /\    /    |  |____ |  `----.|  `----.|  `--'  | |  |  |  | |  |____ 
    \__/  \__/     |_______||_______| \______| \______/  |__|  |__| |_______|

.___________.  ______                                                        
|           | /  __  \                                                       
`---|  |----`|  |  |  |                                                      
    |  |     |  |  |  |                                                      
    |  |     |  `--'  |                                                      
    |__|      \______/                                                       

.______     ______   .______     ______   ______   .______      .__   __.    
|   _  \   /  __  \  |   _  \   /      | /  __  \  |   _  \     |  \ |  |    
|  |_)  | |  |  |  | |  |_)  | |  ,----'|  |  |  | |  |_)  |    |   \|  |    
|   ___/  |  |  |  | |   ___/  |  |     |  |  |  | |      /     |  . `  |    
|  |      |  `--'  | |  |      |  `----.|  `--'  | |  |\  \----.|  |\   |    
| _|       \______/  | _|       \______| \______/  | _| `._____||__| \__|    

.______    __    ______  __  ___  _______ .______                            
|   _  \  |  |  /      ||  |/  / |   ____||   _  \                           
|  |_)  | |  | |  ,----'|  '  /  |  |__   |  |_)  |                          
|   ___/  |  | |  |     |    <   |   __|  |      /                           
|  |      |  | |  `----.|  .  \  |  |____ |  |\  \----.                      
| _|      |__|  \______||__|\__\ |_______|| _| `._____|                      
     """
    lazy_print(ascii_title, step=3)
    time.sleep(2)


def main_menu():
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
        print(Fore.LIGHTWHITE_EX + "1. List Movies")
        print(Fore.LIGHTWHITE_EX + "2. Add Movie")
        print(Fore.LIGHTWHITE_EX + "3. Delete Movie")
        print(Fore.LIGHTWHITE_EX + "4. Update Movie Note")
        print(Fore.LIGHTWHITE_EX + "5. Stats")
        print(Fore.LIGHTWHITE_EX + "6. Random Movie")
        print(Fore.LIGHTWHITE_EX + "7. Search Movie")
        print(Fore.LIGHTWHITE_EX + "8. Movies Sorted by Rating")
        print(Fore.LIGHTWHITE_EX + "9. Create a Histogram")
        print(Fore.LIGHTWHITE_EX + "10. Movies Sorted by Chronological Order")
        print(Fore.LIGHTWHITE_EX + "11. Filter Movies")
        print(Fore.LIGHTWHITE_EX + "12. Generate Website")
        print()

        user_menu_input = input(Fore.LIGHTGREEN_EX + "Enter choice (0-12): \n >>> ")

        if user_menu_input.strip() == "":
            print(Fore.MAGENTA + "You forget to enter a menu number!")
            continue

        try:
            user_menu_input = int(user_menu_input)
            if 0 <= user_menu_input <= 12:
                return user_menu_input
            else:
                print(Fore.MAGENTA + "Please enter a number between 0-12")

        except ValueError:
            print(Fore.MAGENTA + "Enter only numbers please!")
        except Exception as e:
            logging.error(e)
            print(f"{Fore.RED + Back.BLACK}Something went wrong! \n Error message: {e}")


def returner_func():
    """
    This function will play after every finished menu option in order for the user to press enter and return to menu.
    :return: User input 'ENTER' key.
    """
    input(Fore.CYAN + Style.BRIGHT + "Please press enter to return to the main menu!")


def add(movies, storage):
    try:
        movie_to_add = input(
            Fore.LIGHTGREEN_EX + "What Movie would you like to add to the PopcornPicker library?\n>>> ")
        if not movie_to_add:
            raise ValueError("You didn't type a movie name")

        movie_details = api_extraction(movie_to_add)
        if movie_to_add in movies:
            print(Fore.CYAN + "Movie is already in the Library.\n"
                              "Taking you back to the main menu")
            returner_func()
            return
        movie_to_add, movie_rating, movie_year, movie_poster, imdb_full_link, country = api_extraction(
            movie_to_add)
        storage.add_movie(movie_to_add, movie_rating, movie_year, movie_poster, imdb_full_link, country)
        print(f"{movie_to_add} successfully added to the PopcornPicker Library. "
              f"Released in {movie_year} it has a imdb rating of {movie_rating}")
    except Exception as e:
        print(f"Error occurred: {e}")

    returner_func()


def get_country_code_from_name(country):
    """
    Receives a string containing 1 or more country names.
    Takes the names and returns the country codes for the names e.g. Australia = AU
    :param country: (str) country name/s
    :return: (str) country code
    """
    if country and "," in country:
        countries = [c.strip() for c in country.split(",")]
        country_codes = []
        for country in countries:
            try:
                country_objects = pycountry.countries.lookup(country)
                country_codes.append(country_objects.alpha_2)
            except LookupError:
                pass
        return country_codes[0]  # change later to show all flags
    elif country:
        try:
            country = pycountry.countries.lookup(country)
            return country.alpha_2
        except LookupError as e:
            print(f"LookupError: {e}")
            return None
    else:
        return None


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


def exit_program():
    sys.exit()
