import streamlit as st
from google_sheets import *

# GENERAL PAGE BUTTONS
def display_button(label, target_page):
    button_key = f"{label}_{target_page}"
    if st.button(label, key=button_key):
        st.session_state.page = target_page
        
# STUDENT CREDENTIALS BUTTON 
def display_student_email_button(label, signin_target_page, signup_target_page):
    email = st.text_input("Email:")
    existing_admin_emails = read_sheet()
    if st.button(label):
        admin_email = f"admin@{email.split('@')[1]}"
        if admin_email in existing_admin_emails: 
            existing_student_emails = read_values(sheet_name=admin_email, column_name="email", row_name=None)
            if email in existing_student_emails.values: # <-- SIGNING IN
                st.success("Signing In")
                st.session_state.email = email
                st.session_state.admin_email = admin_email
                st.session_state.page = signin_target_page
            if email not in existing_student_emails.values: # <-- SIGNING UP
                st.success("Signing Up")
                st.session_state.email = email
                st.session_state.admin_email = admin_email
                st.session_state.page = signup_target_page
                edit_values(sheet_name=admin_email, column_name="email", row_name="append", value=email)
                edit_values(sheet_name=admin_email, column_name="friends", row_name=email, value=None)
                edit_values(sheet_name=admin_email, column_name="activities", row_name=email, value=None)
                edit_values(sheet_name=admin_email, column_name="interests", row_name=email, value=None)
        if not admin_email in existing_admin_emails: # <-- INSTITUTION HAS NOT MADE AN ACCOUNT
            st.error("Your Institution Has Not Made an Account with Us")

# STUDENT PROFILE BUTTON
def display_student_profile_button(label, target_page, delete_account_target_page): 
    email = st.session_state.email
    admin_email = st.session_state.admin_email 
    student_profile_info = read_values(sheet_name=admin_email, column_name=None, row_name=email)
    st.write(student_profile_info)
    for i in student_profile_info.values()
        print(i)
    add_value = st.text_input("Add Friends:") # <-- ADDING INFO
    if st.button("Edit Friends"):
        edit_values(sheet_name=admin_email, column_name='friends', row_name='email', value=add_value)
    '''
    delete_column = st.text_input("Delete Data Field:") # <-- DELETING DATA FIELDS
    if st.button("Delete Data Field"):
        delete_column(sheet_name=email, column_name=delete_column)
    if st.button("Delete Account"): # <-- DELETE ACCOUNT
        st.success("Deleting Account")
        delete_sheet(sheet_name=email)
        st.session_state.page = delete_account_target_page
        st.session_state.email = None
    if st.button(label): # <-- HOME PAGE
        st.session_state.page = target_page
    '''

# ADMIN CREDENTIALS BUTTON
def display_admin_email_button(label, signin_target_page, signup_target_page):
    email = st.text_input("Email:")
    existing_emails = read_sheet()

    if st.button(label):
        if email in existing_emails: # <-- SIGNING IN
            st.success("Signing In")
            st.session_state.email = email
            st.session_state.page = signin_target_page
        if email not in existing_emails: # <-- SIGNING UP
            st.success("Signing Up")
            st.session_state.email = email
            st.session_state.page = signup_target_page
            create_sheet(sheet_name=email)
            add_column(sheet_name=email, value="email")
            add_column(sheet_name=email, value="friends")
            add_column(sheet_name=email, value="activities") 
            add_column(sheet_name=email, value="interests") 

# ADMIN PROFILE BUTTON
def display_admin_profile_button(label, target_page, delete_account_target_page):
    email = st.session_state.email
    existing_headers = read_column(sheet_name=email)
    st.write(existing_headers)
    add_column = st.text_input("Add Data Field:") # <-- ADDING DATA FIELDS
    if st.button("Add Data Field"):
        add_column(sheet_name=email, value=add_column) 
    delete_column = st.text_input("Delete Data Field:") # <-- DELETING DATA FIELDS
    if st.button("Delete Data Field"):
        delete_column(sheet_name=email, column_name=delete_column)
    if st.button("Delete Account"): # <-- DELETE ACCOUNT
        st.success("Deleting Account")
        delete_sheet(sheet_name=email)
        st.session_state.page = delete_account_target_page
        st.session_state.email = None
    if st.button(label): # <-- HOME PAGE
        st.session_state.page = target_page
