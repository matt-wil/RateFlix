import streamlit as st
from old_app.movie_search import MovieSearch
import importlib
homepage_module = importlib.import_module("streamlitify.🎥_Homepage")
SearchView = getattr(homepage_module, "SearchView")

if "view" not in st.session_state:
    st.session_state.view = SearchView()

if "search" not in st.session_state:
    st.session_state.search = MovieSearch(st.session_state.storage, st.session_state.view)

st.title("Lets search for a certain movie!")

search_item = st.text_input("Enter a movie name to search")
st.session_state["search_item"] = search_item

if st.button("Search"):
    results = st.session_state.search.search_movie()


st.sidebar.success("Select a Page above")

