import requests
import os
from dotenv import load_dotenv
import streamlit as st


# load_dotenv("global.env")

API_KEY = os.getenv("API_KEY")

URL = f"https://api.nasa.gov/planetary/apod?api_key={API_KEY}"

response = requests.get(URL).json()


    
    
st.set_page_config(
    page_title="SPAAACE",
    page_icon="🪐"
)
    
st.title(response["title"])
     
st.image(response["url"])

st.write(response["explanation"])