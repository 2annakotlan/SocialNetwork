import streamlit as st

def display_landing_page():
    if st.button("Student Login"):
        st.session_state.page = 'student_login_page' 
    if st.button("Admin Login"):
        st.session_state.page = 'admin_login_page' 
 
def display_student_login_page():
    st.write("Student Info")
    
def display_admin_login_page():
    st.write("Admin Info") 
