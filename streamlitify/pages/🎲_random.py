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

if "random_movie_title" in st.session_state:
    st.image(f"{st.session_state.random_movie_details.get("poster")}")
    st.subheader(f"Movie: {st.session_state.random_movie_title}")
    st.subheader(f"Rating: {st.session_state.random_movie_details.get("rating")}")
    st.subheader(f"Note: {st.session_state.random_movie_details.get("note") if st.session_state.random_movie_details.get("note") else None}")
    st.subheader(f"Made in: {st.session_state.random_movie_details.get("country")}")

st.sidebar.success("Select a Page above")

