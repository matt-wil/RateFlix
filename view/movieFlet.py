from view.Base_UI import BaseUI
import flet as ft
from fletify.components import MyButton
from fletify.router import Router


class MovieAppFletUI(BaseUI):
    def __init__(self, page, presenter_crud, presenter_manager, presenter_stats, presenter_search, presenter_web_gen):
        self.page = page
        # app settings
        self.page.title = "PopcornPicker"
        self.page.window_width = 800
        self.page.window_height = 1000
        self.page.bgcolor = ft.colors.DEEP_PURPLE_400

        self.presenter_crud = presenter_crud
        self.presenter_manager = presenter_manager
        self.presenter_stats = presenter_stats
        self.presenter_search = presenter_search
        self.presenter_web_gen = presenter_web_gen
        self.page.on_route_change = Router.route_change
        self.page.on_view_pop = Router.view_pop
        self.page.update()

    def welcome_page(self):
        pass

    def main_menu(self):
        self.page.add(ft.Text("Menu"))
        button0 = MyButton("Exit", lambda: Router.route_change(self.page, ft.RouteChangeEvent(route="/exit")))
        button1 = MyButton("List Movies", lambda: Router.route_change(self.page, ft.RouteChangeEvent(route="/display_all")))
        button2 = MyButton("Add Movie", lambda: Router.route_change(self.page, ft.RouteChangeEvent(route="/add")))
        button3 = MyButton("Delete Movie", lambda: Router.route_change(self.page, ft.RouteChangeEvent(route="/delete")))
        button4 = MyButton("Update Movie Note", lambda: Router.route_change(self.page, ft.RouteChangeEvent(route="/update")))
        button5 = MyButton("Stats", lambda: Router.route_change(self.page, ft.RouteChangeEvent(route="/display_stats")))
        button6 = MyButton("Random Movie", lambda: Router.route_change(self.page, ft.RouteChangeEvent(route="/display_random")))
        button7 = MyButton("Search Movie", lambda: Router.route_change(self.page, ft.RouteChangeEvent(route="/search")))
        button8 = MyButton("Movies Sorted by Rating", lambda: Router.route_change(self.page, ft.RouteChangeEvent(route="/display_sorted")))
        button9 = MyButton("Create a Histogram", lambda: Router.route_change(self.page, ft.RouteChangeEvent(route="/create_histogram")))
        button10 = MyButton("Movies Sorted by Chronological Order", lambda: Router.route_change(self.page, ft.RouteChangeEvent(route="/display_chronologically")))
        button11 = MyButton("Filter Movies",lambda: Router.route_change(self.page, ft.RouteChangeEvent(route="/filter")))
        button12 = MyButton("Generate Website",lambda: Router.route_change(self.page, ft.RouteChangeEvent(route="/generate_website")))

        self.page.add(button0, button1, button2, button3, button4, button5, button6, button7, button8, button9,
                      button10, button11, button12)
        self.page.update()

    def handle_route_change(self, route, event):
        event.route = route
        Router.route_change(self.page, event)

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
