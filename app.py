import streamlit as st
from pages import display_landing_page

if 'page' not in st.session_state:
    st.session_state.page = 'landing_page'

if st.session_state.page == 'landing_page':
    display_landing_page()
