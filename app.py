from landing_page import display_landing_page, display_create_account_page
import streamlit as st

display_landing_page()

if st.session_state.page == 'create_account_page':
    display_create_account_page()  
  

