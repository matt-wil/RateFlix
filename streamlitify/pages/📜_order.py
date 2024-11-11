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

st.title("Here we have sorted the movies by rating for you!")
sorted_movies = st.session_state.manager.sort_by_rating()
st.title("Movies sorted by rating:")
rows = len(sorted_movies.keys())
for movie, details in sorted_movies.items():
    col1, col2 = st.columns(2)
    with col1:
        st.image(f"{details['poster']}")
    with col2:
        st.title(f"{movie}")
        st.subheader(f"Imdb Rating: {details['rating']}")
        st.subheader(f"Released: {details['year']}")
        st.subheader(f"Filmed in: {details['country']}")
        if details.get("note"):
            st.subheader(f"Note: {details['note']}")

st.sidebar.success("Select a Page above")
