import streamlit as st
from buttons import *

def display_landing_page():
    st.write("Landing Page")
    display_button(label="Student", target_page="student_credentials_page") 
    display_button(label="Admin", target_page="admin_credentials_page")

def display_student_credentials_page():
    st.write("Student Credentials Page")
    display_student_email_button(label="Enter", signin_target_page="student_landing_page", signup_target_page="student_profile_page")
    display_button(label="Back", target_page="landing_page")

def display_student_profile_page():
    st.write("Student Profile Page")
    display_student_profile_button(label="Enter", target_page=None, delete_account_target_page=None)
    display_button(label="Save Changes", target_page="student_landing_page")

def display_student_landing_page():
    st.write("Student Landing Page")
    display_button(label="Edit Profile", target_page="student_profile_page")
    display_button(label="Sign Out", target_page="landing_page")

def display_admin_credentials_page():
    st.write("Admin Credentials Page")
    display_admin_email_button(label="Enter", signin_target_page="admin_landing_page", signup_target_page="admin_profile_page")
    display_button(label="Back", target_page="landing_page")

def display_admin_profile_page():
    st.write("Admin Profile Page")
    display_admin_profile_button(label="Admin Page", target_page="admin_landing_page", delete_account_target_page="landing_page")

def display_admin_landing_page():
    st.write("Admin Landing Page")
    display_button(label="Edit Profile", target_page="admin_profile_page")
    display_button(label="Sign Out", target_page="landing_page")

if 'page' not in st.session_state: st.session_state.page = 'landing_page'
page_functions = {name[8:]: func for name, func in globals().items() if name.startswith('display_')}
if st.session_state.page in page_functions: page_functions[st.session_state.page]()
