import streamlit as st
from googlesheets import append_row_to_sheet, get_sheets_service

# Initialize Google Sheets service
service = get_sheets_service()

# Streamlit input for the user to enter a name
name = st.text_input("Enter name to append:")

# Specify the column where the name should be added
column = "0_degree"  # Change this to the correct column name if needed

if st.button("Append Name"):
    if name:
        # Call append_row_to_sheet to add the name to the correct column
        updated_df = append_row_to_sheet(service, column, name)
        st.success(f"Name '{name}' has been added to the sheet!")
        st.write(updated_df)  # Display the updated DataFrame
