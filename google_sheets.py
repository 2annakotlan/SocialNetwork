import streamlit as st
import pandas as pd
from googleapiclient.discovery import build 
from google.oauth2.service_account import Credentials

spreadsheetId = '1g_upGl2tligN2G7OjVDDIIjVXuhFCupkJME4vPDL7ro'

def get_sheets_service():
    credentials = Credentials.from_service_account_info(st.secrets["google_service_account"], scopes=['https://www.googleapis.com/auth/spreadsheets'])
    return build('sheets', 'v4', credentials=credentials)

service = get_sheets_service()

def get_data(sheet_name, row_name, column_name):
    result = service.spreadsheets().values().get(spreadsheetId=spreadsheetId, range=sheet_name).execute()
    data = result.get('values', [])
    df = pd.DataFrame(data[1:], columns=data[0])
    if row_name is None and column_name is not None:
        data = df[[column_name]]  
    elif column_name is None and row_name is not None:
        data = df[df.iloc[:, 0] == row_name] 
    elif row_name is not None and column_name is not None:
        data = df[df.iloc[:, 0] == row_name][[column_name]]  # Filter by row and column
    return data 

def get_header(sheet_name):
    result = service.spreadsheets().values().get(spreadsheetId=spreadsheetId, range=sheet_name).execute()
    data = result.get('values', [])
    df = pd.DataFrame(data[1:], columns=data[0])  # First row is used as column names
    header = df.columns  
    return header

def create_new_sheet(new_sheet_name):
    service.spreadsheets().batchUpdate(spreadsheetId=spreadsheetId, body={'requests': [{"addSheet": {"properties": {"title": new_sheet_name}}}]}).execute()

def edit_cell(sheet_name, column_name, row_name, value):
    column_names = service.spreadsheets().values().get(spreadsheetId=spreadsheetId, range=f"{sheet_name}!1:1").execute().get("values", [[]])[0]
    column_index = chr(65 + column_names.index(column_name))
    row_names = service.spreadsheets().values().get(spreadsheetId=spreadsheetId, range=f"{sheet_name}!A:A").execute().get("values", [[]])
    row_index = len(row_names) + 1 if row_name == "append" else [row[0] for row in row_names].index(row_name) + 1
    service.spreadsheets().values().update(spreadsheetId=spreadsheetId, range=f"{sheet_name}!{column_index}{row_index}", valueInputOption="RAW", body={"values": [[value]]}).execute()

def edit_header(sheet_name, value):
    column_names = service.spreadsheets().values().get(spreadsheetId=spreadsheetId, range=f"{sheet_name}!1:1").execute().get('values', [[]])[0]  
    column_index = chr(64 + len(column_names) + 1 )  
    service.spreadsheets().values().update(spreadsheetId=spreadsheetId, range=f"{sheet_name}!{column_index}1", valueInputOption="RAW", body={"values": [[value]]}).execute()




