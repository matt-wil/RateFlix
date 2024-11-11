import os.path
import time

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


st.title("Lets create a Histogram 📊")
filename = st.text_input("Enter a filename to save the histogram under")

histogram_folder = os.path.join(os.getcwd(), "histograms")


def create_histogram():
    if filename:
        if not os.path.exists(histogram_folder):
            os.makedirs(histogram_folder)

        st.session_state.manager.create_histogram(filename=os.path.join(histogram_folder, filename))
        st.success(f"Histogram saved as {filename}.png")
        time.sleep(1)


st.button("Create Histogram", on_click=create_histogram)
file_path = os.path.join(histogram_folder, f"{filename}.png")
if filename and os.path.isfile(file_path):
    st.image(file_path)
else:
    st.warning("The histogram image does not exist yet. Lets generate it first")

st.sidebar.success("Select a Page above")
