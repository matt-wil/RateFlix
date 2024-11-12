import time
from os.path import join
from utilities import get_country_code_from_name


class WebsiteGenerator:
    """
    A class for generating a simple HTML website displaying a movie library with details such as title,
    year, rating, poster, and country flag.

    Methods:
        __init__(storage):
            Initializes the WebsiteGenerator with a storage object that holds movie data.

        generate_website():
            Generates an HTML file with a list of movies, their details, and country flags,
            then saves it to the 'web' folder as index.html.
    """

    def __init__(self, storage):
        """
        Initializes the WebsiteGenerator instance with a storage object for managing movie data.
        :arg:
            storage: An instance of the storage class responsible for providing movie data.
        """
        self._storage = storage

    def generate_website(self):
        """
        Generates an HTML website displaying a list of movies. For each movie, it includes details such as
        the title, year, rating, poster, country flag, and a link to the IMDb page. The generated website
        is saved as 'index.html' in the 'web' directory.
        The method also adds country flags by fetching the corresponding country code and uses the `get_country_code_from_name` function
        to generate the flag image URL.
        """
        movies = self._storage.list_movies()
        html_content = """
         <!DOCTYPE html>
         <html lang="en">
         <head>
             <meta charset="UTF-8">
             <meta name="viewport" content="width=device-width, initial-scale=1.0">
             <link rel="stylesheet" href="style.css"/>
             <title>PopcornPicker</title>
         </head>
         <body>
         <main>
             <div class="list-movies-title">
                 <h1>PopcornPicker Movie Library</h1>
             </div>
             <div class="list">
         """
        # add all movies to html list
        for title, details in movies.items():
            country_code = get_country_code_from_name(details.get('country'))
            html_content += f"""
                 <div class="movie">
                     <a href="{details.get("imdbID")}" target="_blank">
                         <div class="flag-container">
                             <img class="country-flag" src="https://flagsapi.com/{country_code}/flat/64.png" alt="{details.get('country')} Flag">
                         </div>
                             <img class="movie-poster" src="{details.get("poster")}">
                     </a>
                     <div class="text">
                         <div class="movie-title">{title}</div>
                         <div class="movie-year">{details.get("year")}</div>
                         <div class="movie-rating">iMDb Rating: {details.get("rating")}</div>
                         <div class="movie-note">{details.get("note", "")}</div>
                     </div>
                 </div>
         """

        # closing tags
        html_content += """
             </div>
         </main>
         </body>
         </html>
         """

        # write the HTML content to a file
        with open(join("web", "index.html"), "w") as file:
            file.write(html_content)

        print("Website was generated successfully")
        time.sleep(2)
