import streamlit as st

from presenter.movie_manager import MovieManager

st.set_page_config(
    page_title="PopcornPicker",
    page_icon="🎥",
)


if "storage" not in st.session_state:
    st.session_state.storage = None
    st.warning("Please select a storage on the Homepage!")

if "manager" not in st.session_state:
    st.session_state.manager = MovieManager(st.session_state.storage)


movies = st.session_state.manager.list_movies()
st.title("Add a note to a certain movie")
movie_title = st.text_input("Movie title")
if movie_title:
    if movie_title in movies.keys():
        note = st.text_input("Note")
        if note:
            result_dict = st.session_state.manager.update_movie(
                movie_title, note)
            if result_dict.get("success"):
                st.write(f"{result_dict.get('message')}")
            else:
                st.write(f"{result_dict.get('error')}")
    else:
        st.warning("This movie is not in the library")

st.sidebar.success("Select a Page above")
