import requests
import streamlit as st

import parse_downloads_page

st.write("Fetching latest release info...")

latest_release_info = parse_downloads_page.get_latest_release()

st.write("Latest release:", latest_release_info.name)

button = st.button("Download latest release package")

if button:
    url = latest_release_info.classic_win_small_url
    
    st.write("Loading...")
    
    response = requests.get(url)
    response.raise_for_status()
    
    st.write("Loaded.")
