import streamlit as st
import requests
import pandas as pd

# Google Apps Script Web App URL
web_app_url = "https://script.google.com/macros/s/AKfycbzpnW2AmxdMTr7qhE0b-Sx4pgqnUgpT4_T8lP1Nbk4jHryR_dGxi6j-ReEWLx6XNx_N6Q/exec"

# Button to trigger the deletion
if st.button("Delete Last Row"):
    response = requests.post(web_app_url)  # Send POST request without additional data
    st.write(response.text)  # Display the response message

# Fetch and display the updated sheet data
csv_url = "https://docs.google.com/spreadsheets/d/14ExBLiXSqPKFI6jBvwGH63b1LiItPp64To68d36K7GE/export?format=csv"
df = pd.read_csv(csv_url)
st.write(df)
