from view.Base_UI import BaseUI


class MovieAppStreamlitUI(BaseUI):
    def __init__(self, presenter_crud, presenter_manager, presenter_stats, presenter_search, presenter_web_gen):
        self.presenter_crud = presenter_crud
        self.presenter_manager = presenter_manager
        self.presenter_stats = presenter_stats
        self.presenter_search = presenter_search
        self.presenter_web_gen = presenter_web_gen

    def welcome_page(self):
        pass

    def main_menu(self):
        pass

    def display_all(self):
        pass

    def add(self):
        pass

    def delete(self):
        pass

    def update(self):
        pass

    def display_stats(self):
        pass

    def display_random(self):
        pass

    def search(self):
        pass

    def display_sorted(self):
        pass

    def create_histogram(self):
        pass

    def display_chronologically(self):
        pass

    def filter(self):
        pass

    def generate_website(self):
        pass

    def exit(self):
        pass