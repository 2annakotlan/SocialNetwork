import streamlit as st
from googlesheets import get_sheets_service, append_row_to_sheet

st.set_page_config(page_title="Add Info", layout="centered")
st.title("Add Your Information")

with st.form(key="input_form"):
    name = st.text_input("Name:")
    friends = st.text_area("Friends (comma separated):", value="")
    interests = st.text_area("Interests (comma separated):")
    activities = st.text_area("Activities (comma separated):", value="")
    submit = st.form_submit_button("Submit")

if submit:
        friends = friends if friends else ""
        activities = activities if activities else ""
        df = append_row_to_sheet(get_sheets_service(), name, friends, interests, activities)
        st.success("Info added!")
        st.write(df)
else:
        st.warning("Please fill in 'Name' and 'Interests'.")

