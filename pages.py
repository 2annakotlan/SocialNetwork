import streamlit as st

def display_button(label, target_page):
    if st.button(label):
        st.session_state.page = target_page

def display_email_button():
    if st.button("Enter Email"):
        st.session_state.show_email_input = True

def display_landing_page():
    st.write("Landing Page")
    display_button("Student Login", "student_login_page")
    display_button("Admin Login", "admin_login_page")
 
def display_student_login_page():
    st.write("Student Login Page")
    email = st.text_input("Enter your email:")
    display_button("Next", "student_profile_page")
    display_button("Back", "landing_page")
    
def display_admin_login_page():
    st.write("Admin Login Page")
    display_button("Back", "landing_page")

def display_student_profile_page():
    st.write("Student Profile Page")
