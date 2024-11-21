import pandas as pd
import streamlit as st
from googlesheets.py import df

# Display data in Streamlit
st.write("Here is the data:")
st.dataframe(df)

# Input: Get name to be added (e.g., from user input in Streamlit)
new_name = st.text_input("Enter a name to add:")

# Check if the new name already exists in the 'name' column
if new_name and new_name not in df['name'].values:
    # If name doesn't exist, append it using pd.concat()
    new_row = pd.DataFrame([{'name': new_name}])  # Create new row as a DataFrame
    df = pd.concat([df, new_row], ignore_index=True)  # Concatenate new row to the DataFrame
    
    # Optionally update the Google Sheet with the new row (ensure data is correct)
    new_data = df.values.tolist()
    service.spreadsheets().values().update(spreadsheetId=SPREADSHEET_ID, range=RANGE_NAME, valueInputOption="RAW", body={"values": [df.columns.tolist()] + new_data}).execute()

    st.write(f"Name '{new_name}' has been added to the dataframe and updated in the sheet.")
else:
    if new_name:
        st.write(f"Name '{new_name}' already exists in the dataframe.")
