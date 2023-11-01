from datetime import timedelta
from pathlib import Path

import requests
import streamlit as st

import parse_downloads_page


@st.cache_resource(ttl=timedelta(hours=6), show_spinner="Gettin latest version info...")
def get_latest_release():
    return parse_downloads_page.get_latest_release()


latest_release_info = get_latest_release()

st.write("Latest release:", latest_release_info.name)

url = latest_release_info.classic_win_small_url
file_name = url.rpartition("/")[2]


def download(url, file_name):
    with st.spinner(f"Loading {file_name}..."):
        response = requests.get(url)
        response.raise_for_status()
        Path(file_name).open("wb").write(response.content)

    st.write(f"File {file_name} loaded")


if Path(file_name).is_file():
    st.write(f"File {file_name} already loaded")
else:
    download(url, file_name)

button = st.button("Download again")

if button:
    download(url, file_name)
