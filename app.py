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
        st.success(response.text) if
