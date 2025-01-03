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
    existing_emails = get_data("admin", None, "email")
    existing_institutions = get_data("admin", None, "institution")
    st.write(existing_emails)
    email = st.text_input("Email:")
    domain = email.split('@')[1] if email and '@' in email and '.' in email.split('@')[1] else None
    institution_guess = email.split('@')[1].split('.')[-2].capitalize() if email and '@' in email and '.' in email.split('@')[1] else None
    institution = st.text_input("Institution:", value=institution_guess) if email and email not in existing_emails.values else None
    
    if st.button("Enter"):   
        st.session_state.admin_email = email    
        if email in existing_emails.values: # existing email --> logging in
            st.session_state.page = login_target_page
            st.success("Logging In")
        elif institution in existing_institutions.values: # wrong institution
            st.error("this institution is already associated with a different email")
        else: # not existing email --> signing up
            edit_cell("admin", "email", "append", email)
            edit_cell("admin", "domain", email, domain)
            edit_cell("admin", "institution", email, institution)
            create_new_sheet(institution)
            edit_header(institution, "name")
            edit_header(institution, "friends")
            edit_header(institution, "activities") 
            edit_header(institution, "interests") 
            st.session_state.page = signup_target_page  
            st.success("Signing Up")
            
def display_admin_profile_button():
    email = st.session_state.admin_email
    institution = str((get_data("admin", email, "institution")).iloc[0, 0])
    st.write(institution)
    existing_headers = get_header(institution)
    st.write("Data Collected:")

    if "deleted_headers" not in st.session_state:
        st.session_state.deleted_headers = []
    if "added_headers" not in st.session_state:
        st.session_state.added_headers = []

    for i, header in enumerate(existing_headers):
        col1, col2 = st.columns([0.2, 1])
        with col1:
            if header in st.session_state.deleted_headers:
                header_text = f"- ~~{header}~~"
            else:
                header_text = f"- {header}"
            st.write(header_text)
        with col2:
            if header in st.session_state.deleted_headers:
                restore = st.button("➕", key=f"restore_{i}")
                if restore:
                    st.session_state.deleted_headers.remove(header)
            else:
                delete = st.button("❌", key=f"edit_{i}")
                if delete:
                    st.session_state.deleted_headers.append(header)

    for i, new_header in enumerate(st.session_state.added_headers):
        col1, col2 = st.columns([0.2, 1])
        with col1:
            st.write(f"- {new_header}")
        with col2:
            delete_added = st.button("❌", key=f"delete_added_{i}")
            if delete_added:
                st.session_state.added_headers.remove(new_header)

    col3, col4 = st.columns([3, 1])
    with col3:
        new_column = st.text_input("New Column:", key="new_column_input")
    with col4:
        add = st.button("➕")
        if add and new_column.strip():
            st.session_state.added_headers.append(new_column.strip())

    st.write(st.session_state.deleted_headers)
    st.write(st.session_state.added_headers)

