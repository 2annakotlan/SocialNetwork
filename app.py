import streamlit as st
from buttons import *

def display_landing_page():
    st.write("Landing Page")
    display_button("Student", "student_start_page")
    display_button("Admin", "admin_start_page")

def display_student_start_page():
    st.write("Student Start Page")
    display_student_email_button("student_landing_page", "student_profile_page")
    display_button("Back", "landing_page")

def display_student_profile_page():
    st.write("Student Profile Page")
    display_button("Save Changes", "student_landing_page")
    display_button("Log out", "landing_page")

def display_student_landing_page():
    st.write("Student Landing Page")
    display_button("Edit Profile", "student_profile_page")
    display_button("Log out", "landing_page")

def display_admin_start_page():
    st.write("Admin Start Page")
    display_button("Sign In", "admin_signin_page")
    display_button("Sign Up", "admin_signup_page")
    display_button("Back", "landing_page")

def display_admin_signin_page():
    st.write("Admin Sign In Page")
    display_button("Sign In", "admin_landing_page")
    #display_button("Back", "admin_start_page")

def display_admin_signup_page():
    st.write("Admin Sign Up Page")
    display_button("Sign Up", "admin_profile_page")
    display_button("Back", "admin_start_page")

def display_admin_profile_page():
    st.write("Admin Profile Page")
    display_button("Save Changes", "admin_landing_page")

def display_admin_landing_page():
    st.write("Admin Landing Page")
    display_button("Edit Profile", "admin_profile_page")
    display_button("Sign Out", "landing_page")

if 'page' not in st.session_state:
    st.session_state.page = 'landing_page'

page_functions = {name[8:]: func for name, func in globals().items() if name.startswith('display_')}

if st.session_state.page in page_functions:
    page_functions[st.session_state.page]()
