import streamlit as st
from googleapiclient.discovery import build
from google.oauth2.service_account import Credentials

# Load the credentials from Streamlit secrets
service_account_info = st.secrets["google_service_account"]

# Define the scope for the API
SCOPES = ['https://www.googleapis.com/auth/spreadsheets']

# Authenticate the service account using the information from Streamlit secrets
credentials = Credentials.from_service_account_info(service_account_info, scopes=SCOPES)

# Build the Sheets API client
service = build('sheets', 'v4', credentials=credentials)

# Specify the Spreadsheet ID and range
SPREADSHEET_ID = '1g_upGl2tligN2G7OjVDDIIjVXuhFCupkJME4vPDL7ro'  # Replace with your actual Spreadsheet ID
RANGE_NAME = 'Sheet1!A1:A5'  # Replace with your desired range

# Retrieve data from the specified range
sheet = service.spreadsheets()
result = sheet.values().get(spreadsheetId=SPREADSHEET_ID, range=RANGE_NAME).execute()
rows = result.get('values', [])

# Display the data
if not rows:
    st.warning("No data found.")
else:
    st.success("Data retrieved successfully!")
    st.write("Here is the data:")
    st.table(rows)
