import streamlit as st

def display_landing_page():
    st.write("Landing Page")
    if st.button('Student Sign In'):
        st.session_state.page = "create_account_page"

def display_student_portal_page():
    st.write("Create Account")
