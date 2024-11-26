import streamlit as st
from pages import *

if 'page' not in st.session_state:
    st.session_state.page = 'landing_page'

if st.session_state.page == 'landing_page':
    display_landing_page()
    
if st.session_state.page == 'profile_info':
    display_profile_info_page()
