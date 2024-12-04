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

def dddddddddddddisplay_admin_email_button(login_target_page, signup_target_page):
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

#######################################################################################
import streamlit as st
import pandas as pd
import time
from googleapiclient.discovery import build
from googlesheets import *

# Function to fetch email domains from the Google Sheet
def get_sheet_data_2(service):
    result = service.spreadsheets().values().get(
        spreadsheetId='1g_upGl2tligN2G7OjVDDIIjVXuhFCupkJME4vPDL7ro',
        range="Institutions"
    ).execute()
    data = result.get('values', [])
    return pd.DataFrame(data[1:], columns=data[0])

def display_admin_email_button(service, login_target_page, signup_target_page):
    # Fetch the institutions data
    institutions_df = get_sheet_data_2(service)
    # Extract unique domains from the Institutions column
    institution_domains = institutions_df["Institutions"].unique()

    email = st.text_input("Email:")

    if st.button("Enter"):
        # Validate the email against institution domains
        if email.startswith("admin") and any(email.endswith(f"@{domain}") for domain in institution_domains):
            st.session_state.page = login_target_page
            st.success("Logging In")
            time.sleep(3)
        elif email.startswith("admin") and not any(email.endswith(f"@{domain}") for domain in institution_domains):
            st.session_state.page = signup_target_page
            st.success("Signing Up")
            time.sleep(3)
        elif not email.startswith("admin"):
            st.error("Please use an admin email")


