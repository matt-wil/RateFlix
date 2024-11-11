import streamlit as st
from presenter.movie_crud import MovieCrud

st.set_page_config(
    page_title="PopcornPicker",
    page_icon="🎥",
)

if "storage" not in st.session_state:
    st.session_state.storage = None
    st.warning("Please select a storage on the Homepage!")

if "crud" not in st.session_state:
    st.session_state.crud = MovieCrud(st.session_state.storage)

movies_dict = st.session_state.crud.list_movies()
st.title("Here is a List of all the Movies currently in the PopcornPicker library 👀")

for title, details in movies_dict.items():
    col1, col2 = st.columns(2)
    with col1:
        st.image(f"{details.get('poster')}")
    with col2:
        st.subheader(f"{title}")
        st.write(f"Released in {details.get('year')}")
        st.write(f"Imdb Rating:{details.get('rating')}")
        st.write(f"Movie Note: {details.get('note') if details.get('note') else None}")
        st.write(f"Filmed in: {details.get('country')}")


st.sidebar.success("Select a Page above")
