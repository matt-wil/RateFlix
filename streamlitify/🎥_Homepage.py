import streamlit as st
import sys
from pathlib import Path
sys.path.append(str(Path(__file__).resolve().parent.parent))
from presenter.movie_manager import MovieManager
from model.storage_csv import StorageCSV
from model.storage_json import StorageJson


# Page config
st.set_page_config(
    page_title="PopcornPicker",
    page_icon="🎥",
)


class SearchView:
    def get_search_input(self):
        return st.session_state.get("search_item", "")

    def show_results(self, results):
        if results:
            st.header("Here are your search results")
            for result in results:
                col1, col2 = st.columns(2)
                with col1:
                    st.header(result['title'])
                    poster_url = result.get('poster', None)
                    if poster_url:
                        st.image(poster_url)
                    else:
                        st.write("Poster not available")
                with col2:
                    st.subheader(f"Released in {result['year']}")
                    st.subheader(f"Made in {result['country']}")
                    st.subheader(f"Imbd rating of {result['rating']}")
            else:
                st.write("No matching movies found")


st.title("Welcome to the PopcornPicker Movie Application.")
st.text("Please choose your storage type.")

if "storage" not in st.session_state:
    st.session_state.storage = None
col1, col2 = st.columns(2)
with col1:
    JSON = st.button("JSON")
with col2:
    CSV = st.button("CSV")

if "view" not in st.session_state:
    st.session_state.view = SearchView()
# initialize storage and functionality as session_state variables
if JSON:
    st.session_state.selected_storage = "json"
    st.session_state.storage = StorageJson()
    st.session_state.manager = MovieManager(st.session_state.storage)
    st.success("JSON storage selected")


if CSV:
    st.session_state.selected_storage = "csv"
    st.session_state.storage = StorageCSV()
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

