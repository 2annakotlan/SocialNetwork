import time
import pandas as pd
import streamlit as st
from googlesheets import get_googlesheets_api, get_googlesheets_data

while True:
    sheets_service = get_googlesheets_api()
    df = get_googlesheets_data(sheets_service)
    st.write(df)
    time.sleep(10)
