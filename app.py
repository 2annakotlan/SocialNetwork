import streamlit as st
import requests
import pandas as pd

web_app_url = "https://script.google.com/macros/s/AKfycbzpnW2AmxdMTr7qhE0b-Sx4pgqnUgpT4_T8lP1Nbk4jHryR_dGxi6j-ReEWLx6XNx_N6Q/exec"
name = st.text_input("Enter your name to remove:")

if st.button("Delete Name"):
    # Send a POST request to the Google Apps Script to remove the name
    response = requests.post(web_app_url, data={'name': name})
    
    if response.status_code == 200:
        st.success(f"Name '{name}' has been successfully removed.")
    else:
        st.error(f"Failed to remove the name '{name}'. Please try again.")

# Display the current data in the sheet (optional)
csv_url = "https://docs.google.com/spreadsheets/d/14ExBLiXSqPKFI6jBvwGH63b1LiItPp64To68d36K7GE/export?format=csv"
df = pd.read_csv(csv_url)
st.write(df)
