import streamlit as st
import requests
import pandas as pd

# Google Apps Script web app URL
web_app_url = "https://script.google.com/macros/s/AKfycbzpnW2AmxdMTr7qhE0b-Sx4pgqnUgpT4_T8lP1Nbk4jHryR_dGxi6j-ReEWLx6XNx_N6Q/exec"

# Input for the name of the row to delete
name = st.text_input("Enter the name of the row to delete:")

# Delete button
if st.button("Delete"):
    if name.strip():  # Ensure the input is not empty
        response = requests.post(web_app_url, data={'name': name})
        st.success(response.text) if response.status_code == 200 else st.error("Failed to delete the row.")
    else:
        st.error("Please enter a valid name.")

# Fetch and display the updated spreadsheet
csv_url = "https://docs.google.com/spreadsheets/d/14ExBLiXSqPKFI6jBvwGH63b1LiItPp64To68d36K7GE/export?format=csv"
try:
    df = pd.read_csv(csv_url)
    st.write("Updated Spreadsheet:")
    st.write(df)
except Exception as e:
    st.error("Failed to fetch the spreadsheet.")
