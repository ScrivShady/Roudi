import streamlit as st
from bs4 import BeautifulSoup

# Load the HTML file
with open('equine_equity.html') as f:
    soup = BeautifulSoup(f, 'html.parser')

# Set up the Streamlit app
st.title('Equine Equity App')

# Convert the HTML content to a Streamlit-friendly format
st.markdown(soup.prettify(), unsafe_allow_html=True)