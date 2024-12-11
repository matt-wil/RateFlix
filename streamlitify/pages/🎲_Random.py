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


def run_randomizer():
    movie, details = st.session_state.manager.random_movie()
    st.session_state.random_movie_title = movie
    st.session_state.random_movie_details = details


st.title("Click the button to see what random movie you get!")
if st.button("🎲"):
    run_randomizer()
col1, col2 = st.columns(2)
if "random_movie_title" in st.session_state:
    with col1:
        st.image(f"{st.session_state.random_movie_details.get('poster')}")
    with col2:
        st.subheader(f"Movie: {st.session_state.random_movie_title}")
        st.subheader(
            f"Rating: {st.session_state.random_movie_details.get('rating')}")
        st.subheader(
            f"Released in {st.session_state.random_movie_details.get('year')}")
        st.subheader(
            f"Made in: {st.session_state.random_movie_details.get('country')}")
        if st.session_state.random_movie_details.get('note'):
            st.subheader(
                f"Note: {st.session_state.random_movie_details.get('note')}")

st.sidebar.success("Select a Page above")
