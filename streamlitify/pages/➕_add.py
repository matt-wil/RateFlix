import streamlit as st
from model.storage_csv import StorageCSV
from presenter.movie_crud import MovieCrud
import os
os.getcwd()


# initialize database
storage = StorageCSV()
crud = MovieCrud(storage)

st.set_page_config(
    page_title="PopcornPicker",
    page_icon="🎥",
)
st.title("Add a new movie into the PopcornPicker Library. ➕")
st.text("Type the Movie you would like to add and I will fly through the OMDb database and get it for you!")
st.sidebar.success("Select a Page above")


if "movie_to_add" not in st.session_state:
    st.session_state["movie_to_add"] = ""

my_input = st.text_input("Enter movie name here", st.session_state["movie_to_add"])
add = st.button("Add ➕")
if add:
    st.session_state["movie_to_add"] = my_input
    result = crud.add_movie(my_input)
    if result.get("success"):
        st.write(result.get("message"))
    else:
        st.write(result.get("error"))
