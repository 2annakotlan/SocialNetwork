import streamlit as st
import requests
import pandas as pd

web_app_url = "https://script.google.com/macros/s/AKfycbzpnW2AmxdMTr7qhE0b-Sx4pgqnUgpT4_T8lP1Nbk4jHryR_dGxi6j-ReEWLx6XNx_N6Q/exec"
name = st.text_input("Enter name:")
if st.button("Submit"):
    response = requests.post(web_app_url, data={'name': name})
    if response.ok:
        result = response.json()
        if result.get("found"):
            st.success(f"Name '{name}' was found in the sheet.")
        else:
            st.error(f"Name '{name}' was not found in the sheet.")
    else:
        st.error("Failed to connect to the Google Apps Script.")


csv_url = "https://docs.google.com/spreadsheets/d/14ExBLiXSqPKFI6jBvwGH63b1LiItPp64To68d36K7GE/export?format=csv"
df = pd.read_csv(csv_url)
st.write(df)


