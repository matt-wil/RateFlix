import streamlit as st
from presenter.movie_manager import MovieManager
import datetime

st.set_page_config(
    page_title="PopcornPicker",
    page_icon="🎥",
)

if "storage" not in st.session_state:
    st.session_state.storage = None
    st.warning("Please select a storage on the Homepage!")

if "manager" not in st.session_state:
    st.session_state.manager = MovieManager(st.session_state.storage)

current_year = datetime.datetime.now().year

st.title("Let Filter the Movies")

min_rating = st.text_input("Minimum Rating (0 - 10)")
start_year = st.text_input("Start year (1888 to current year)")
end_year = st.text_input("End year (1888 to current year)")

if st.button("Filter Movies"):
    filtered_movies, error_message = st.session_state.manager.filter_movies(min_rating, start_year, end_year)

    if error_message:
        st.error(error_message)
    else:
        if filtered_movies:
            for movie, year, rating, poster, note in filtered_movies:
                col1, col2 = st.columns(2)
                with col1:
                    if poster:
                        st.image(poster)
                    else:
                        st.write("No image available")
                with col2:
                    st.header(f"{movie}")
                    st.subheader(f"Year: {year}")
                    st.subheader(f"Rating: {rating}")
                    if note:
                        st.subheader(f"Note: {note}")
        else:
            st.write("No movies found with the specified criteria")


st.sidebar.success("Select a Page above")
