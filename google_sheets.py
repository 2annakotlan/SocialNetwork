import streamlit as st
import pandas as pd
from googleapiclient.discovery import build
from google.oauth2.service_account import Credentials

def get_sheets_service():
    credentials = Credentials.from_service_account_info(st.secrets["google_service_account"], scopes=['https://www.googleapis.com/auth/spreadsheets'])
    return build('sheets', 'v4', credentials=credentials)

service = get_sheets_service()

def get_sheet_column_data(sheet_name, column_name):
    result = service.spreadsheets().values().get(spreadsheetId='1g_upGl2tligN2G7OjVDDIIjVXuhFCupkJME4vPDL7ro', range=sheet_name).execute()
    data = result.get('values', []) 
    df = pd.DataFrame(data[1:], columns=data[0])
    return df[[column_name]]

def create_new_sheet(new_sheet_name):
    service.spreadsheets().batchUpdate(
        spreadsheetId='1g_upGl2tligN2G7OjVDDIIjVXuhFCupkJME4vPDL7ro',
        body={'requests': [{"addSheet": {"properties": {"title": new_sheet_name}}}]}).execute()

def append_values(input_data, sheet_name, column_name):
    service.spreadsheets().values().append(spreadsheetId='1g_upGl2tligN2G7OjVDDIIjVXuhFCupkJME4vPDL7ro', range=f'{sheet_name}!{column_name}1', valueInputOption='RAW', body={'values': [[input_data]]}).execute()

'''

def get_sheet_data(service, sheet_name):
    result = service.spreadsheets().values().get(spreadsheetId='1g_upGl2tligN2G7OjVDDIIjVXuhFCupkJME4vPDL7ro', range=sheet_name).execute()
    data = result.get('values', []) 
    return pd.DataFrame(data[1:], columns=data[0]) 
    
def create_admin_account(service, email):
    row = [name, friends, interests, activities]
    service.spreadsheets().values().append(spreadsheetId='1g_upGl2tligN2G7OjVDDIIjVXuhFCupkJME4vPDL7ro', range="Institution", valueInputOption="RAW", body={'values': [row]}).execute()
    st.success("Admin Account Created")
    return get_sheet_data(service, "Institution")

def create_student_account(service, name, friends, interests, activities):
    row = [name, friends, interests, activities]
    service.spreadsheets().values().append(spreadsheetId='1g_upGl2tligN2G7OjVDDIIjVXuhFCupkJME4vPDL7ro', range="Sheet1", valueInputOption="RAW", body={'values': [row]}).execute()
    st.success("Account Created")
    return get_sheet_data(service, "Sheet1")

def delete_student_account(service, name):
    df = get_sheet_data(service)
    row_index = df[df['name'] == name].index[0] + 2
    service.spreadsheets().values().clear(spreadsheetId='1g_upGl2tligN2G7OjVDDIIjVXuhFCupkJME4vPDL7ro', range=f"Sheet1!A{row_index}:D{row_index}").execute()   
    st.success("Account Deleted")
    return df

def edit_student_account(service, name, friends, interests, activities):
    df = get_sheet_data(service)
    row_index = df[df['name'] == name].index[0] + 2
    row = [name, friends, interests, activities]
    service.spreadsheets().values().update(spreadsheetId='1g_upGl2tligN2G7OjVDDIIjVXuhFCupkJME4vPDL7ro', range=f"Sheet1!A{row_index}:D{row_index}", valueInputOption="RAW", body={'values': [row]}).execute()
    st.success("Information Edited")
    return df


'''










