from datetime import timedelta
from pathlib import Path

import streamlit as st

import download_source


@st.cache_resource(ttl=timedelta(hours=6), show_spinner="Gettin latest version info...")
def get_latest_release():
    return download_source.get_latest_release()


def download(url, file_name):
    with st.spinner(f"Loading {file_name}..."):
        download_source.download_file(url, file_name)

    st.write(f"File {file_name} loaded")


latest_release_info = get_latest_release()

st.write("Latest release:", latest_release_info.name)

url = latest_release_info.classic_win_small_url
file_name = url.rpartition("/")[2]

if Path(file_name).is_file():
    st.write(f"File {file_name} already loaded")
else:
    download(url, file_name)

button = st.button("Download again")

if button:
    download(url, file_name)
