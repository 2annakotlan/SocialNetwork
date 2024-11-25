import streamlit as st

def landing_page():
    st.write("Landing Page")
    if st.button('Student Sign In'):
        st.session_state.page = "create_account_page"

def create_account_page():
    st.write("Create Account")
