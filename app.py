import streamlit as st

def display_button(label, target_page):
    if st.button(label):
        st.session_state.page = target_page

def display_landing_page():
    st.write("Landing Page")
    display_button("Student Login", "student_login_page")
    display_button("Admin Login", "admin_login_page")

def display_student_login_page():
    st.write("Student Login Page")
    email = st.text_input("Enter your email:")
    if email:
        display_button("Login", "student_profile_page")
    display_button("Back", "landing_page")

def display_admin_login_page():
    st.write("Admin Login Page")
    email = st.text_input("Enter your email:")
    if email:
        display_button("Login", "admin_landing_page")
    display_button("Back", "landing_page")

def display_student_profile_page():
    st.write("Student Profile Page")
    display_button("Save Changes", "student_landing_page")
    display_button("Log out", "landing_page")

def display_admin_landing_page():
    st.write("Admin Landing Page")
    display_button("Log out", "landing_page")

def display_student_landing_page():
    st.write("Student Landing Page")
    display_button("Edit Profile", "student_profile_page")
    display_button("Log out", "landing_page")

if 'page' not in st.session_state:
    st.session_state.page = 'landing_page'

page_functions = {name[8:]: func for name, func in globals().items() if name.startswith('display_')}

if st.session_state.page in page_functions:
    page_functions[st.session_state.page]()
