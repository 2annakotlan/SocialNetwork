import pandas as pd
import streamlit as st
from googleapiclient.discovery import build
from google.oauth2.service_account import Credentials

# Function to initialize Google Sheets API
def get_sheets_service():
    credentials = Credentials.from_service_account_info(
        st.secrets["google_service_account"],
        scopes=['https://www.googleapis.com/auth/spreadsheets']
    )
    return build('sheets', 'v4', credentials=credentials)

# Retrieve data from the Google Sheet
def get_sheet_data(service):
    spreadsheet_id = '1g_upGl2tligN2G7OjVDDIIjVXuhFCupkJME4vPDL7ro'
    result = service.spreadsheets().values().get(spreadsheetId=spreadsheet_id, range="Sheet1").execute()
    data = result.get('values', [])
    return pd.DataFrame(data[1:], columns=data[0]) if data else pd.DataFrame()

# Function to append a row to the Google Sheet
def append_row_to_sheet(service, name):
    # Fetch the current data from Google Sheets
    df = get_sheet_data(service)
    
    # Create a new row with the 'name' and empty columns for the rest
    new_row = [name] + [''] * (len(df.columns) - 1)  # Adjust based on the number of columns in the sheet
    
    # Append the new row to the DataFrame
    df.loc[len(df)] = new_row

    # Update Google Sheets with the new data
    service.spreadsheets().values().update(
        spreadsheetId='1g_upGl2tligN2G7OjVDDIIjVXuhFCupkJME4vPDL7ro',
        range="Sheet1!A1",  # Adjust if needed
        valueInputOption="RAW",
        body={'values': df.values.tolist()}
    ).execute()

    return df
