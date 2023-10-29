import requests
import streamlit as st
from pathlib import Path

import parse_downloads_page

st.write("Fetching latest release info...")

latest_release_info = parse_downloads_page.get_latest_release()

st.write("Latest release:", latest_release_info.name)

url = latest_release_info.classic_win_small_url
file_name = url.rpartition("/")[2]

if Path(file_name).is_file():
    st.write("File already loaded")
    download_button_text = "Download again"
else:
    download_button_text = "Download"

button = st.button(download_button_text)

if button:
    st.write("Loading...")
    
    response = requests.get(url)
    response.raise_for_status()
    
    Path(file_name).open("wb").write(response.content)
    
    st.write("Loaded.")
