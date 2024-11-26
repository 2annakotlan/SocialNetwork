import streamlit as st
from pages import display_landing_page

# Check if 'page' is in session_state, otherwise set default value
if 'page' not in st.session_state:
    st.session_state.page = 'landing_page'

# Assuming you want to display the landing page:
if st.session_state.page == 'landing_page':
    display_landing_page()
