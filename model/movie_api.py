import requests
from requests.exceptions import HTTPError, ConnectionError, Timeout, RequestException
import os


# access environment variable for api_key
from dotenv import load_dotenv
load_dotenv()
api_key = os.getenv("API_KEY")
OMDb_url = "http://www.omdbapi.com/?apikey="


def api_extraction(title, api=api_key, url=OMDb_url, search_type="&t="):
    """
    searches the OMDb database for given Title movie
    returns the movie title, rating, year, poster URL, imdb_full_link, country
    :param title: (str)
    :param api: (str) Api key for OMDb
    :param url: (str) Url for OMDb
    :param search_type: (str) search type keyword set for Movie title search
    :return: movie name, movie rating, movie year of release, the Poster URL, imdb full website link and the country
    """
    try:
        response = requests.get(url + api + search_type + title)
        response.raise_for_status()
        movie_info = response.json()
        movie = movie_info["Title"]
        rating = movie_info["imdbRating"]
        year = movie_info["Year"]
        poster_url = movie_info["Poster"]
        imdb_id = movie_info["imdbID"]
        imdb_full_link = f"https://www.imdb.com/title/{imdb_id}/"
        country = movie_info["Country"]
        return movie, rating, year, poster_url, imdb_full_link, country
    except HTTPError as e:
        print(
            f"HTTP error occurred: {e} - Status Code: {response.status_code}")
    except ConnectionError as e:
        print(f"Connection Error: unable to connect to API {e}")
    except Timeout:
        print(f"Error request has timed out")
    except RequestException as e:
        print(f"Ann error occurred: {e}")
