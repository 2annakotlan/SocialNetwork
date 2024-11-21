import pandas as pd
import streamlit as st
from googleapiclient.discovery import build
from google.oauth2.service_account import Credentials

# Load service account credentials from Streamlit secrets
service_account_info = st.secrets["google_service_account"]

# Define the scope for the API
SCOPES = ['https://www.googleapis.com/auth/spreadsheets']

# Authenticate the service account using the information from Streamlit secrets
credentials = Credentials.from_service_account_info(service_account_info, scopes=SCOPES)

# Build the Sheets API client
service = build('sheets', 'v4', credentials=credentials)

# Specify the Spreadsheet ID
SPREADSHEET_ID = '1g_upGl2tligN2G7OjVDDIIjVXuhFCupkJME4vPDL7ro'  # Replace with your actual Spreadsheet ID

# First, retrieve the sheet's metadata to determine the number of rows and columns
sheet_metadata = service.spreadsheets().get(spreadsheetId=SPREADSHEET_ID).execute()
sheet = sheet_metadata['sheets'][0]  # Assumes only one sheet or you can change the index if necessary

# Determine the last row with data in the sheet
last_row = sheet['properties']['gridProperties']['rowCount']
last_column = sheet['properties']['gridProperties']['columnCount']

# Retrieve data from the entire sheet range from A1 to the last row and column
RANGE_NAME = f"Sheet1!A1:{chr(64 + last_column)}{last_row}"  # Build dynamic range (e.g., A1:B5)

# Retrieve data from the specified range
result = service.spreadsheets().values().get(spreadsheetId=SPREADSHEET_ID, range=RANGE_NAME).execute()
rows = result.get('values', [])

# If data exists, create a pandas DataFrame using the first row as headers
if rows:
    headers = rows[0]  # First row as headers
    data = rows[1:]    # All subsequent rows as data

    # Create a DataFrame with the first row as columns
    df = pd.DataFrame(data, columns=headers)

    # Display the DataFrame in Streamlit
    st.write("Here is the data:")
    st.dataframe(df)
