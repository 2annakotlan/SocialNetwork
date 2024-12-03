import streamlit as st
import time

def display_button(label, target_page):
    if st.button(label):
        st.session_state.page = target_page

def display_admin_email_button(login_target_page, signup_target_page):
    email = st.text_input("Email:")
    existing_domain = "@gmail.com" 
    
    if st.button("Next"):
        if email == f"admin{existing_domain}":
            st.session_state.page = login_target_page
            st.success("Logging In")
            time.sleep(3)  
        elif email.startswith("admin") and not email.endswith(existing_domain):
            st.session_state.page = signup_target_page
            st.success("Signing Up")
            time.sleep(3)  
        elif not email.startswith("admin"):
            st.error("Please use an admin email")

def display_student_email_button(login_target_page, signup_target_page):
    email = st.text_input("Email:")
    existing_domain = "@gmail.com" 
    
    if st.button("Next"):
        if email.startswith("admin"):
            st.error("Please do not use an admin email")
        elif email.endswith(existing_domain):
            st.session_state.page = login_target_page
            st.success("Logging In")
            time.sleep(3)  
        elif not email.endswith(existing_domain):
            st.session_state.page = signup_target_page
            st.success("Signing Up")
            time.sleep(3)  



