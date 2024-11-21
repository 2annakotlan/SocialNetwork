import pandas as pd
import streamlit as st
from googleapiclient.discovery import build
from google.oauth2.service_account import Credentials

# Initialize Google Sheets API
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

# Append a new row with the given name
def append_row(service, name):
    df = get_sheet_data(service)
    new_row = [name] + [''] * (len(df.columns) - 1)  
    df.loc[len(df)] = new_row
    service.spreadsheets().values().update(
        spreadsheetId='1g_upGl2tligN2G7OjVDDIIjVXuhFCupkJME4vPDL7ro',
        range="Sheet1!A1",
        valueInputOption="RAW",
        body={'values': df.values.tolist()}).execute()
    return df

