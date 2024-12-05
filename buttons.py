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



def display_admin_email_button(login_target_page, signup_target_page):
    email = st.text_input("Email:")

    import streamlit as st
    import pandas as pd
    from googleapiclient.discovery import build
    from google.oauth2.service_account import Credentials
    
    def get_sheets_service():
        credentials = Credentials.from_service_account_info(st.secrets["google_service_account"], scopes=['https://www.googleapis.com/auth/spreadsheets'])
        return build('sheets', 'v4', credentials=credentials)
    
    service = get_sheets_service()
    
    def get_sheet_column_data(sheet_name, column_name):
        result = service.spreadsheets().values().get(spreadsheetId='1g_upGl2tligN2G7OjVDDIIjVXuhFCupkJME4vPDL7ro', range=sheet_name).execute()
        data = result.get('values', []) 
        df = pd.DataFrame(data[1:], columns=data[0])
        return df[[column_name]]
