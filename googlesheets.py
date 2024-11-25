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

def append_row_to_sheet(service, name, friends, interests, activities):
    df = get_sheet_data(service)
    new_row = [name, friends, interests, activities]
    service.spreadsheets().values().append(spreadsheetId='1g_upGl2tligN2G7OjVDDIIjVXuhFCupkJME4vPDL7ro', range="Sheet1", valueInputOption="RAW", body={'values': [new_row]}).execute()
    return df

def delete_row_by_name(service, name):
    df = get_sheet_data(service)
    row_to_delete = df[df['name'] == name].index
    if not row_to_delete.empty:
        row_index = row_to_delete[0] + 2  
        service.spreadsheets().values().clear(spreadsheetId='1g_upGl2tligN2G7OjVDDIIjVXuhFCupkJME4vPDL7ro', range=f"Sheet1!A{row_index}:D{row_index}").execute()
    return df



