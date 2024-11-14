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
st.title("Would you like to delete a movie from the library?")
movie_to_delete = st.text_input("Movie name")
if movie_to_delete:
    if movie_to_delete in movies.keys():
        result = st.session_state.manager.delete_movie(movie_to_delete)
        if result:
            st.write(f"{result.get('success')}")
        else:
            st.write(f"{result.get('error')}")
    else:
        st.warning("Movie not in the Library")
st.sidebar.success("Select a Page above")
