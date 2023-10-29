import requests
import streamlit as st

button = st.button("Download Dwarf Fortress")

if button:
    url = "https://bay12games.com/dwarves/df_50_11_win.zip"
    
    st.write("Loading...")
    
    response = requests.get(url)
    response.raise_for_status()
    
    st.write("Loaded.")
