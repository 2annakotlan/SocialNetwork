from googleapiclient.discovery import build
from google.oauth2.service_account import Credentials

def get_google_sheets_service():
    service = build('sheets', 'v4', credentials=Credentials.from_service_account_info(
        st.secrets["google_service_account"], 
        scopes=['https://www.googleapis.com/auth/spreadsheets']))
    return service

def fetch_data_from_sheets(service, spreadsheet_id, range_name):
    rows = service.spreadsheets().values().get(spreadsheetId=spreadsheet_id, range=range_name).execute().get('values', [])
    return rows
