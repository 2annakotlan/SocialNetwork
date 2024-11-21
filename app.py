import pandas as pd
import streamlit as st
from googleapiclient.discovery import build
from google.oauth2.service_account import Credentials

# Google Sheets API setup
service = build('sheets', 'v4', credentials=Credentials.from_service_account_info(st.secrets["google_service_account"], scopes=['https://www.googleapis.com/auth/spreadsheets']))  # Authenticate and build client
SPREADSHEET_ID = '1g_upGl2tligN2G7OjVDDIIjVXuhFCupkJME4vPDL7ro'

# Function to fetch the data from Google Sheets
def fetch_data_from_sheets():
    # Fetch data from Google Sheets
    sheet = service.spreadsheets().get(spreadsheetId=SPREADSHEET_ID).execute()['sheets'][0]
    last_row, last_column = sheet['properties']['gridProperties'].values()
    RANGE_NAME = f"Sheet1!A1:{chr(64 + last_column)}{last_row}"
    rows = service.spreadsheets().values().get(spreadsheetId=SPREADSHEET_ID, range=RANGE_NAME).execute().get('values', [])

    # Create DataFrame
    return pd.DataFrame(rows[1:], columns=rows[0])  # Use first row as headers

# Initially load data
df = fetch_data_from_sheets()

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
    service.spreadsheets().values().update(spreadsheetId=SPREADSHEET_ID, range=f"Sheet1!A1", valueInputOption="RAW", body={"values": [df.columns.tolist()] + new_data}).execute()

    # Reload the data from Google Sheets to reflect the update
    df = fetch_data_from_sheets()
    
    # Display updated data in Streamlit
    st.write(f"Name '{new_name}' has been added to the dataframe and updated in the sheet.")
    st.write("Here is the updated data:")
    st.dataframe(df)
else:
    if new_name:
        st.write(f"Name '{new_name}' already exists in the dataframe.")
