import pandas as pd
import streamlit as st
from googlesheets import append_row_to_sheet, get_sheets_service

# Initialize Google Sheets service
service = get_sheets_service()

# Streamlit inputs for the user to enter values for each column
columnA_value = st.text_input("Enter value for Column A:")
columnB_value = st.text_input("Enter value for Column B:")
columnC_value = st.text_input("Enter value for Column C:")
columnD_value = st.text_input("Enter value for Column D:")

# Ensure that at least one field is filled out
if st.button("Append Row"):
    try:
        # Check if each value is None, and if so, set it to an empty string
        row_data = [
            columnA_value if columnA_value else '',  # Use empty string if not provided
            columnB_value if columnB_value else '',
            columnC_value if columnC_value else '',
            columnD_value if columnD_value else ''
        ]
        
        # Call append_row_to_sheet with the user inputs for each column
        updated_df = append_row_to_sheet(
            service,
            columnA=row_data[0], 
            columnB=row_data[1], 
            columnC=row_data[2], 
            columnD=row_data[3]
        )
        st.success("Row has been added to the sheet!")

        # Refresh the data and display the updated DataFrame
        updated_df = get_sheet_data(service)  # Fetch updated data after append
        st.write(updated_df)  # Display the updated DataFrame

    except Exception as e:
        st.error(f"An error occurred: {e}")
else:
    st.warning("Please enter values for the columns before appending.")
