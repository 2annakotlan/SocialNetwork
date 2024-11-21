import pandas as pd
import streamlit as st
from google.oauth2.service_account import Credentials
from googleapiclient.discovery import build

def get_google_sheets_data():
    service_account_credentials = st.secrets["google_service_account"] # Load service account credentials
    api_scopes = ['https://www.googleapis.com/auth/spreadsheets'] # Define required API scope
    google_credentials = Credentials.from_service_account_info(service_account_credentials, scopes=api_scopes) # Get credentials
    sheets_service = build('sheets', 'v4', credentials=google_credentials) # Build the Google Sheets service
    
    spreadsheet_id = '1g_upGl2tligN2G7OjVDDIIjVXuhFCupkJME4vPDL7ro'  # Fetch spreadsheet data
    sheet_info = sheets_service.spreadsheets().get(spreadsheetId=spreadsheet_id).execute()
    
    sheet_properties = sheet_info['sheets'][0]['properties']['gridProperties'] # Get sheet properties
    num_rows, num_columns = sheet_properties['values']  # Get last row and column
    data_range = f"Sheet1!A1:{chr(64 + num_columns)}{num_rows}" # Define the range to fetch data
    sheet_data = sheets_service.spreadsheets().values().get(spreadsheetId=spreadsheet_id, range=data_range).execute() # Get data from the sheet
    
    sheet_rows = sheet_data.get('values', []) # Extract rows and return as DataFrame
    return pd.DataFrame(sheet_rows[1:], columns=sheet_rows[0])  # First row as column headers

df = get_google_sheets_data()
