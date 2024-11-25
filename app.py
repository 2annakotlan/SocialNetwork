import streamlit as st
from googlesheets import get_sheets_service, create_account, delete_account, edit_account

st.set_page_config(page_title="Add Info", layout="centered")
st.title("Add Your Information")

with st.form(key="input_form"):
    name = st.text_input("Name:")
    friends = st.text_area("Friends (comma separated):", value="")
    interests = st.text_area("Interests (comma separated):", value="")
    activities = st.text_area("Activities (comma separated):", value="")
    add = st.form_submit_button("Create Account")
    delete = st.form_submit_button("Delete Account")
    edit = st.form_submit_button("Edit Account Information")

if add:
    df = create_account(get_sheets_service(), name, friends, interests, activities)

if delete:
    df = delete_account(get_sheets_service(), name)

if edit: 
    df = edit_account(get_sheets_service(), name, new_friends, new_interests, new_activities)

