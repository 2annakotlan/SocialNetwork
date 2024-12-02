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
    display_button("Back", "landing_page")
    
def display_admin_login_page():
    st.write("Admin Login Page")
    display_button("Back", "landing_page")
