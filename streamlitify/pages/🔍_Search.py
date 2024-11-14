import streamlit as st
import importlib

from presenter.movie_manager import MovieManager

homepage_module = importlib.import_module("streamlitify.🎥_Homepage")

if "manager" not in st.session_state:
    st.session_state.manager = MovieManager(st.session_state.storage)

st.title("Lets search for a certain movie!")

search_item = st.text_input("Enter a movie name to search")
st.session_state["search_item"] = search_item

if st.button("Search"):
    results = st.session_state.manager.search_movie(search_item)
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


st.sidebar.success("Select a Page above")

