from model.storage_json import StorageJson
from model.storage_csv import StorageCSV
from presenter.movie_manager import MovieManager
import streamlit as st
import sys
from pathlib import Path
sys.path.append(str(Path(__file__).resolve().parent.parent))


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
