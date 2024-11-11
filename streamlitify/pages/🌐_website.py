import os

import streamlit as st
from presenter.movie_website_generator import WebsiteGenerator


web_directory = os.path.join(os.getcwd(), "web", "index.html")

st.set_page_config(
    page_title="PopcornPicker",
    page_icon="🎥",
)

if "storage" not in st.session_state:
    st.session_state.storage = None
    st.warning("Please select a storage on the Homepage!")

st.title("Website Generator 🪄")
st.subheader("This button will create an Interactive Website with the current up to date data from you storage file. ")

if st.session_state.storage:
    website_generator = WebsiteGenerator(st.session_state.storage)
    gen_web = st.button("Generate Website 🌐", on_click=website_generator.generate_website)
else:
    st.warning("Storage is not selected. Please choose a storage type first!")
st.subheader("This button will open your browser")

#  must figure this out so that it will open the index.html properly.
if os.path.exists(web_directory):
    web_link = web_directory
    st.link_button("Open Website", web_link)
else:
    st.warning("index.html not found.")

