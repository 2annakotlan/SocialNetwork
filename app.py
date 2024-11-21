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

# Specify the Spreadsheet ID and range
SPREADSHEET_ID = '1g_upGl2tligN2G7OjVDDIIjVXuhFCupkJME4vPDL7ro'  # Replace with your actual Spreadsheet ID
RANGE_NAME = 'Sheet1!A1:B5'  # Adjust range to match your data (expand if needed)

# Retrieve data from the specified range
sheet = service.spreadsheets()
result = sheet.values().get(spreadsheetId=SPREADSHEET_ID, range=RANGE_NAME).execute()
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
