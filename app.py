import streamlit as st
import requests
import pandas as pd

# Google Apps Script Web App URL
web_app_url = "https://script.google.com/macros/s/AKfycbzpnW2AmxdMTr7qhE0b-Sx4pgqnUgpT4_T8lP1Nbk4jHryR_dGxi6j-ReEWLx6XNx_N6Q/exec"

# Button to trigger the deletion
if st.button("Delete Last Row"):
    try:
        response = requests.post(web_app_url)  # Send POST request
        st.write("Response status code:", response.status_code)  # Display status code
        st.write("Response text:", response.text)  # Display response text
    except requests.exceptions.RequestException as e:
        st.write(f"Request failed: {e}")

# Fetch and display the updated sheet data
csv_url = "https://docs.google.com/spreadsheets/d/14ExBLiXSqPKFI6jBvwGH63b1LiItPp64To68d36K7GE/export?format=csv"
try:
    df = pd.read_csv(csv_url)
    st.write(df)
except Exception as e:
    st.write(f"Failed to load spreadsheet data: {e}")
