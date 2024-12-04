import streamlit as st
import time

def display_button(label, target_page):
    if st.button(label):
        st.session_state.page = target_page 

def display_student_email_button(login_target_page, signup_target_page):
    email = st.text_input("Email:")
    existing_domain = "@gmail.com"
    existing_username = "akotlan"
    
    if st.button("Enter"):
        if email.startswith(existing_username) and email.endswith(existing_domain): 
            st.session_state.page = login_target_page
            st.success("Logging In")
            time.sleep(3)  
        elif not email.startswith(existing_username) and email.endswith(existing_domain):
            st.session_state.page = signup_target_page  
            st.success("Signing Up")
            time.sleep(3)  
        elif not email.endswith(existing_domain): 
            st.error("Your organization has not created an account with us.")

'''
def display_admin_email_button(login_target_page, signup_target_page):
    email = st.text_input("Email:")
    existing_domain = "@gmail.com" 
    
    if st.button("Enter"):
        if email.startswith("admin") and email.endswith(existing_domain):
            st.session_state.page = login_target_page
            st.success("Logging In")
            time.sleep(3)  
        elif email.startswith("admin") and not email.endswith(existing_domain):
            st.session_state.page = signup_target_page
            st.success("Signing Up")
            time.sleep(3)  
        elif not email.startswith("admin"):
            st.error("Please use an admin email")
'''

from google_sheets import *

def display_admin_email_button(login_target_page, signup_target_page):
    email = st.text_input("Email:")

    # Fetch the institution data from the Google Sheet
    service = get_sheets_service()
    institutions_df = get_sheet_data(service, "Institutions")  # Get the entire DataFrame
    existing_domains = institutions_df['institution'].tolist()  # Extract 'institution' column as a list of domains

    if st.button("Enter"):
        # Check if the email ends with any of the valid domains
        if email.startswith("admin") and any(email.endswith(domain) for domain in existing_domains):
            st.session_state.page = login_target_page
            st.success("Logging In")
            time.sleep(3)  
        else:
            st.session_state.page = signup_target_page
            st.success("Signing Up")
            time.sleep(3)
