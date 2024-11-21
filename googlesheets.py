import pandas as pd
import streamlit as st
from googleapiclient.discovery import build
from google.oauth2.service_account import Credentials

def get_googlesheets_api():
    service_account_credentials = st.secrets["google_service_account"] 
    api_scopes = ['https://www.googleapis.com/auth/spreadsheets']  
    google_credentials = Credentials.from_service_account_info(service_account_credentials, scopes=api_scopes)
    sheets_service = build('sheets', 'v4', credentials=google_credentials)
    return sheets_service
    
def get_googlesheets_data(sheets_service):
    spreadsheet_id = '1g_upGl2tligN2G7OjVDDIIjVXuhFCupkJME4vPDL7ro'  
    sheet_info = sheets_service.spreadsheets().get(spreadsheetId=spreadsheet_id).execute()
    sheet_properties = sheet_info['sheets'][0]['properties']['gridProperties']
    num_rows = sheet_properties['rowCount'] 
    num_columns = sheet_properties['columnCount'] 
    data_range = f"Sheet1!A1:{chr(64 + num_columns)}{num_rows}" 
    sheet_data = sheets_service.spreadsheets().values().get(spreadsheetId=spreadsheet_id, range=data_range).execute()
    sheet_rows = sheet_data.get('values', [])  
    return pd.DataFrame(sheet_rows[1:], columns=sheet_rows[0])  

sheets_service = get_googlesheets_api()
df = get_googlesheets_data(sheets_service)

