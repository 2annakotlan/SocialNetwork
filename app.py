import streamlit as st
from landing_page import display_landing_page, display_create_account_page

# Initialize session state if it's not already set
if 'page' not in st.session_state:
    st.session_state.page = 'landing_page'

# Display the appropriate page based on session state
if st.session_state.page == 'landing_page':
    display_landing_page()

if st.session_state.page == 'create_account_page':
    display_create_account_page()
