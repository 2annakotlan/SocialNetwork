import streamlit as st
import requests
import pandas as pd

# URL of your Google Apps Script
web_app_url = "https://script.google.com/macros/s/AKfycbzpnW2AmxdMTr7qhE0b-Sx4pgqnUgpT4_T8lP1Nbk4jHryR_dGxi6j-ReEWLx6XNx_N6Q/exec"

# Input field for the name to be deleted
name = st.text_input("Enter the name to remove:")

# Button to trigger the delete operation
if st.button("Delete Name"):
    if name:  # Check if the name input is not empty
        # Send a POST request to delete the name
        response = requests.post(web_app_url, data={'name': name})
        
        # Check the response from the Google Apps Script
        if response.text == "Row deleted successfully":
            st.success(f"Name '{name}' has been successfully removed.")
        elif response.text == "Name not found":
            st.error(f"Name '{name}' was not found in the list.")
        else:
            st.error("An error occurred while trying to delete the name.")
    else:
        st.error("Please enter a name to delete.")

# Optionally display the current data in the sheet
csv_url = "https://docs.google.com/spreadsheets/d/14ExBLiXSqPKFI6jBvwGH63b1LiItPp64To68d36K7GE/export?format=csv"
df = pd.read_csv(csv_url)
st.write(df)
