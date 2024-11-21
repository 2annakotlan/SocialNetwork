import pandas as pd
from googleapiclient.discovery import build
from google.oauth2.service_account import Credentials

def get_api():
  # Google Sheets API setup
  service = build('sheets', 'v4', credentials=Credentials.from_service_account_info(st.secrets["google_service_account"], scopes=['https://www.googleapis.com/auth/spreadsheets']))  # Authenticate and build client
  SPREADSHEET_ID = '1g_upGl2tligN2G7OjVDDIIjVXuhFCupkJME4vPDL7ro'
  
  # Fetch data from Google Sheets
  sheet = service.spreadsheets().get(spreadsheetId=SPREADSHEET_ID).execute()['sheets'][0]
  last_row, last_column = sheet['properties']['gridProperties'].values()
  RANGE_NAME = f"Sheet1!A1:{chr(64 + last_column)}{last_row}"
  rows = service.spreadsheets().values().get(spreadsheetId=SPREADSHEET_ID, range=RANGE_NAME).execute().get('values', [])
  df = pd.DataFrame(rows[1:], columns=rows[0])  # Use first row as headers
