import streamlit as st

def display_button(label, target_page):
    if st.button(label):
        st.session_state.page = target_page

def display_email_buttons(target_page):
    email = st.text_input("Email:")
    
    if st.button("Login"):
        if email.endswith("@gmail.com"): 
            st.session_state.page = target_page
        else:
            st.error("Invalid email. Please use a Gmail address.")
    
    if st.button("Sign Up"):
        if email:
            st.success("Sign-up successful! Please log in.")
        else:
            st.error("Please enter a valid email to sign up.")

def display_landing_page():
    st.write("Landing Page")
    display_button("Student", "student_start_page")
    display_button("Admin", "admin_start_page")

def display_student_start_page():
    st.write("Student Start Page")
    display_email_buttons("student_profile_page")
    display_button("Back", "landing_page")

def display_admin_start_page():
    st.write("Admin Start Page")
    display_email_buttons("admin_landing_page")
    display_button("Back", "landing_page")

def display_student_profile_page():
    st.write("Student Profile Page")
    display_button("Save Changes", "student_landing_page")
    display_button("Log out", "landing_page")

def display_admin_profile_page():
    st.write("Admin Profile Page")
    display_button("Save Changes", "admin_landing_page")
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
