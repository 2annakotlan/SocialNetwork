import pandas as pd
import streamlit as st
from googleapiclient.discovery import build
from google.oauth2.service_account import Credentials

def get_sheets_service():
    credentials = Credentials.from_service_account_info(st.secrets["google_service_account"], scopes=['https://www.googleapis.com/auth/spreadsheets'])
    return build('sheets', 'v4', credentials=credentials)

def get_sheet_data(service):
    result = service.spreadsheets().values().get(spreadsheetId='1g_upGl2tligN2G7OjVDDIIjVXuhFCupkJME4vPDL7ro', range="Sheet1").execute()
    data = result.get('values', [])
    return pd.DataFrame(data[1:], columns=data[0]) if data else pd.DataFrame()

def append_row_to_sheet(service, columnA=None, columnB=None, columnC=None, columnD=None):
    df = get_sheet_data(service)  
    new_row = [''] * len(df.columns)  
    
    if columnA is not None:
        new_row[df.columns.get_loc('columnA')] = columnA
    if columnB is not None:
        new_row[df.columns.get_loc('columnB')] = columnB
    if columnC is not None:
        new_row[df.columns.get_loc('columnC')] = columnC
    if columnD is not None:
        new_row[df.columns.get_loc('columnD')] = columnD
    
    service.spreadsheets().values().append(spreadsheetId='1g_upGl2tligN2G7OjVDDIIjVXuhFCupkJME4vPDL7ro', range="Sheet1", valueInputOption="RAW", body={'values': [new_row]}).execute()
    return df  



