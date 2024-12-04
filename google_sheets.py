import streamlit as st
import pandas as pd
from googleapiclient.discovery import build
from google.oauth2.service_account import Credentials

def get_sheets_service():
    credentials = Credentials.from_service_account_info(st.secrets["google_service_account"], scopes=['https://www.googleapis.com/auth/spreadsheets'])
    return build('sheets', 'v4', credentials=credentials)

def get_sheet_data(service):
    result = service.spreadsheets().values().get(spreadsheetId='1g_upGl2tligN2G7OjVDDIIjVXuhFCupkJME4vPDL7ro', range="Sheet1").execute()
    data = result.get('values', []) 
    return pd.DataFrame(data[1:], columns=data[0]) 

def create_account(service, name, friends, interests, activities):
    row = [name, friends, interests, activities]
    service.spreadsheets().values().append(spreadsheetId='1g_upGl2tligN2G7OjVDDIIjVXuhFCupkJME4vPDL7ro', range="Sheet1", valueInputOption="RAW", body={'values': [row]}).execute()
    st.success("Account Created")
    return get_sheet_data(service)

def delete_account(service, name):
    df = get_sheet_data(service)
    row_index = df[df['name'] == name].index[0] + 2
    service.spreadsheets().values().clear(spreadsheetId='1g_upGl2tligN2G7OjVDDIIjVXuhFCupkJME4vPDL7ro', range=f"Sheet1!A{row_index}:D{row_index}").execute()   
    st.success("Account Deleted")
    return df

def edit_account(service, name, friends, interests, activities):
    df = get_sheet_data(service)
    row_index = df[df['name'] == name].index[0] + 2
    row = [name, friends, interests, activities]
    service.spreadsheets().values().update(spreadsheetId='1g_upGl2tligN2G7OjVDDIIjVXuhFCupkJME4vPDL7ro', range=f"Sheet1!A{row_index}:D{row_index}", valueInputOption="RAW", body={'values': [row]}).execute()
    st.success("Information Edited")
    return df

##############################################################################################################################################
def get_sheet_data_2(service):
    result = service.spreadsheets().values().get(spreadsheetId='1g_upGl2tligN2G7OjVDDIIjVXuhFCupkJME4vPDL7ro', range="Institutions").execute()
    data = result.get('values', []) 
    return pd.DataFrame(data[1:], columns=data[0]) 

def create_account_2(service, institution):
    row = [name, friends, interests, activities]
    service.spreadsheets().values().append(spreadsheetId='1g_upGl2tligN2G7OjVDDIIjVXuhFCupkJME4vPDL7ro', range="Institutions", valueInputOption="RAW", body={'values': [row]}).execute()
    st.success("Admin Account Created")
    return get_sheet_data_2(service)











