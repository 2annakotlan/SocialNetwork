import streamlit as st

def display_landing_page():
    st.write("Landing Page")
    if st.button("Student Login"):
        st.session_state.page = 'student_login_page' 
    if st.button("Admin Login"):
        st.session_state.page = 'admin_login_page' 
 
def display_student_login_page():
    st.write("Student Login Page")
    if st.button("Back"):
        st.session_state.page = 'landing_page' 
    
def display_admin_login_page():
    st.write("Admin Login Page")
    if st.button("Back"):
        st.session_state.page = 'landing_page' 
