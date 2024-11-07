from abc import ABC, abstractmethod

# 0: self.app.exit_program,
# 1: self.app.list_movies,
# 2: self.app.add_movie,
# 3: self.app.delete_movie,
# 4: self.app.update_movie,
# 5: self.app.stats,
# 6: self.app.random_movie,
# 7: self.app.search_movie,
# 8: self.app.movies_sorted_by_rating,
# 9: self.app.create_histogram_and_save,  -- has no UI
# 10: self.app.movies_sorted_by_chronological_order,
# 11: self.app.filter_movies,
# 12: self.app.generate_website,  -- has no UI


class BaseUI(ABC):
    """
    An Abstract class to enforce modularity and the ability to easily create different UI classes
    for the Movie App to run in.
    """
    @abstractmethod
    def display_all(self):
        pass

    @abstractmethod
    def add(self):
        pass

    @abstractmethod
    def delete(self):
        pass

    @abstractmethod
    def update(self):
        pass

    @abstractmethod
    def display_stats(self):
        pass

    @abstractmethod
    def display_random(self):
        pass

    @abstractmethod
    def search(self):
        pass

    @abstractmethod
    def display_sorted(self):
        pass

    @abstractmethod
    def create_histogram(self):
        pass

    @abstractmethod
    def display_chronologically(self):
        pass

    @abstractmethod
    def filter(self):
        pass

    @abstractmethod
    def generate_website(self):
        pass
