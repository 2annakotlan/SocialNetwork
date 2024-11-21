import pandas as pd
import streamlit as st
from googlesheets import append_row_to_sheet, get_sheets_service

# Initialize Google Sheets service
service = get_sheets_service()

# Streamlit input for the user to enter a name
name = st.text_input("Enter name to append:")

# Ensure the name is not empty
if name:
    if st.button("Append Name"):
        try:
            # Call append_row_to_sheet to add the name to the correct column
            updated_df = append_row_to_sheet(service, "0_degree", name)
            st.success(f"Name '{name}' has been added to the sheet!")

            # Refresh the data and display the updated DataFrame
            updated_df = get_sheet_data(service)  # Fetch updated data after append
            st.write(updated_df)  # Display the updated DataFrame.
        except Exception as e:
            st.error(f"An error occurred: {e}")
else:
    st.warning("Please enter a name to append.")
