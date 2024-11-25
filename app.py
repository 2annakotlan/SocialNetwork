import streamlit as st
from googlesheets import get_sheets_service, append_row_to_sheet, delete_row_by_name, edit_row_by_name

st.set_page_config(page_title="Add Info", layout="centered")
st.title("Add Your Information")

with st.form(key="input_form"):
    name = st.text_input("Name:")
    friends = st.text_area("Friends (comma separated):", value="")
    interests = st.text_area("Interests (comma separated):")
    activities = st.text_area("Activities (comma separated):", value="")
    add = st.form_submit_button("Add Entry")
    delete = st.form_submit_button("Delete Entry")
    edit = st.form_submit_button("Edit Entry")

if add:
    df = append_row_to_sheet(get_sheets_service(), name, friends, interests, activities)

