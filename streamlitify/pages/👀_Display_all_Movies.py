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

movies_dict = st.session_state.manager.list_movies()
st.title("Here is a List of all the Movies currently in the PopcornPicker library 👀")

for title, details in movies_dict.items():
    col1, col2 = st.columns(2)
    with col1:
        st.image(f"{details.get('poster')}")
    with col2:
        st.header(f"{title}")
        st.subheader(f"Released in {details.get('year')}")
        st.subheader(f"Imdb Rating: {details.get('rating')}")
        st.subheader(f"Filmed in: {details.get('country')}")
        if details.get('note'):
            st.subheader(f"Movie Note: {details.get('note')}")


st.sidebar.success("Select a Page above")
