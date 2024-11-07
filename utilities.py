import time
from colorama import Fore, Style, Back
import logging


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

