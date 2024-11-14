import streamlit as st
from old_app.movie_stats import MovieStats

st.set_page_config(
    page_title="PopcornPicker",
    page_icon="🎥",
)

if "storage" not in st.session_state:
    st.session_state.storage = None
    st.warning("Please select a storage on the Homepage!")

if "stats" not in st.session_state:
    st.session_state.stats = MovieStats(st.session_state.storage)

movies = st.session_state.stats.movies()
highest_rating = st.session_state.stats.highest_rating()
lowest_rating = st.session_state.stats.lowest_rating()
highest_rated_movies = st.session_state.stats.highest_rated_movies()
lowest_rated_movies = st.session_state.stats.lowest_rated_movies()
st.title("Here are the current PopcornPicker statistics 📈")
col1, col2 = st.columns(2)
with col1:
    st.subheader(f"Average Rating: {st.session_state.stats.calc_avg():.2f}")
    st.subheader(f"Highest Rated Movies:")
    for title in highest_rated_movies:
        st.subheader(f"{title} with a rating of {highest_rating}")
        st.image(f"{movies.get(title)['poster']}")
    st.write("")
with col2:
    st.subheader(f"Mean Rating: {st.session_state.stats.calc_mean()}")
    st.subheader(f"Lowest Rated Movies:")
    for title in lowest_rated_movies:
        st.subheader(f"{title} with a rating of {lowest_rating}")
        st.image(f"{movies.get(title)['poster']}")
    st.write("")


st.sidebar.success("Select a Page above")
