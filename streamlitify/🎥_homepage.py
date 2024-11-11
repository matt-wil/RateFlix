import streamlit as st
import sys
from pathlib import Path
sys.path.append(str(Path(__file__).resolve().parent.parent))
from presenter.movie_crud import MovieCrud
from presenter.movie_website_generator import WebsiteGenerator
from presenter.movie_manager import MovieManager
from presenter.movie_search import MovieSearch
from presenter.movie_stats import MovieStats
from model.storage_csv import StorageCSV
from model.storage_json import StorageJson


class SearchView:
    def get_search_input(self, search_text: str):
        search_input = st.text_input(search_text)
        return search_input

    def show_results(self, results):
        if results:
            for movie in results:
                st.write(f"**Title**: {movie['title']}, **Year**: {movie['year']}, **Rating**: {movie['rating']}")
            else:
                st.write("No movies found.")


# Page config
st.set_page_config(
    page_title="PopcornPicker",
    page_icon="🎥",
)
st.title("Welcome to the PopcornPicker Movie Application.")
st.text("Please choose your storage type.")

if "storage" not in st.session_state:
    st.session_state.storage = None
col1, col2 = st.columns(2)
with col1:
    JSON = st.button("JSON")
with col2:
    CSV = st.button("CSV")

view = SearchView()
# initialize storage and functionality as session_state variables
if JSON:
    st.session_state.selected_storage = "json"
    st.session_state.storage = StorageJson()
    st.session_state.crud = MovieCrud(st.session_state.storage)
    st.session_state.web_gen = WebsiteGenerator(st.session_state.storage)
    st.session_state.stats = MovieStats(st.session_state.storage)
    st.session_state.search = MovieSearch(st.session_state.storage, view)
    st.session_state.manager = MovieManager(st.session_state.storage)
    st.success("JSON storage selected")


if CSV:
    st.session_state.selected_storage = "csv"
    st.session_state.storage = StorageCSV()
    st.session_state.crud = MovieCrud(st.session_state.storage)
    st.session_state.web_gen = WebsiteGenerator(st.session_state.storage)
    st.session_state.stats = MovieStats(st.session_state.storage)
    st.session_state.search = MovieSearch(st.session_state.storage, view)
    st.session_state.manager = MovieManager(st.session_state.storage)
    st.success("CSV storage selected")

if st.session_state.storage is None:
    st.warning("Please select a storage option!")


st.text("All of your options are as shown in the side bar to the left!")
st.text("Click through and have a look at your options 😊")
st.text("This Application was built using only 🐍 ")
st.text("Created by Matthew Williams")
st.link_button("My Github", "https://github.com/matt-wil")
st.sidebar.success("Select a Page above")

