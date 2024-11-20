import streamlit as st
import requests
import pandas as pd

web_app_url = "https://script.google.com/macros/s/YOUR_DEPLOYMENT_ID/exec"

if st.button("Delete Last Row"):
    response = requests.post(web_app_url)
    st.write("Status Code:", response.status_code)
    st.write("Response Text:", response.text)

csv_url = "https://docs.google.com/spreadsheets/d/YOUR_SHEET_ID/export?format=csv"
df = pd.read_csv(csv_url)
st.write(df)
