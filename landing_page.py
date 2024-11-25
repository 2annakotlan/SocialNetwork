import streamlit as st

def display_landing_page():
    if st.button('Student Sign In'):
        st.session_state.page = "create_account_page"

def display_create_account_page():
    st.write("Create Account")
