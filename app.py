import streamlit as st
from googlesheets import append_row_to_sheet, get_sheets_service

# Function to handle user input and append the row
# Initialize Google Sheets service
service = get_sheets_service()
    
    # Streamlit input for the user to enter a name
name = st.text_input("Enter name to append:")

if st.button("Append Name"):
  if name:
    updated_df = append_row_to_sheet(service, name)
    st.success(f"Name '{name}' has been added to the sheet!")
    st.write(updated_df)  # Display the updated DataFrame



