import streamlit as st
import requests
import pandas as pd

# Google Apps Script web app URL
web_app_url = "https://script.google.com/macros/s/AKfycbzpnW2AmxdMTr7qhE0b-Sx4pgqnUgpT4_T8lP1Nbk4jHryR_dGxi6j-ReEWLx6XNx_N6Q/exec"

# Input for the name of the row to delete
name = st.text_input("Enter the name of the row to delete:")

if st.button("Delete"):
    if name.strip():  # Ensure the input is not empty
        try:
            response = requests.post(web_app_url, data={'name': name})
            if response.status_code == 200:
                st.success(f"Response: {response.text}")
            else:
                st.error(f"Error: {response.status_code}. Response: {response.text}")
        except Exception as e:
            st.error(f"An exception occurred: {e}")
    else:
        st.error("Please enter a valid name.")
