import streamlit as st
from landing_page import display_landing_page, display_create_account_page

if 'page' not in st.session_state:
    st.session_state.page = 'landing_page'

if st.session_state.page == 'landing_page':
    display_landing_page()

if st.session_state.page == 'create_account_page':
    display_create_account_page()
