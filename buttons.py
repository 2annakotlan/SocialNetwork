import streamlit as st
from google_sheets import *
import time

def display_button(label, target_page):
    if st.button(label):
        st.session_state.page = target_page 

def display_student_email_button(login_target_page, signup_target_page):
    email = st.text_input("Email:")
    existing_domain = "@gmail.com"
    existing_username = "akotlan"
    
    if st.button("Enter"):
        if email.startswith(existing_username) and email.endswith(existing_domain): # existing email --> logging in
            st.session_state.page = login_target_page
            st.success("Logging In")
            time.sleep(3)  
        elif not email.startswith(existing_username) and email.endswith(existing_domain): # not existing email, but existing domain --> signing up
            st.session_state.page = signup_target_page  
            st.success("Signing Up")
            time.sleep(3)  
        elif not email.endswith(existing_domain): # not existing domain --> error message
            st.error("Your organization has not created an account with us.")

def display_admin_email_button(login_target_page, signup_target_page):
    existing_emails = get_sheet_column_data("Admin", "domain")
    st.write(existing_emails)
    email = st.text_input("Email:")
    
    if st.button("Enter"):
        if email in existing_emails.values: # existing email --> logging in
            st.session_state.page = login_target_page
            st.success("Logging In")
            time.sleep(3)  
        else: # not existing email --> signing up
            update_cell_value("Admin", "B4", email)

            #create_new_sheet(email)
            st.session_state.page = signup_target_page  
            st.success("Signing Up")
            time.sleep(3)  

    
                          
