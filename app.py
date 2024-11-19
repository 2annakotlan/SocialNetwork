import streamlit as st
import requests
import pandas as pd

# The URL of your deployed Google Apps Script web app
web_app_url = "https://script.google.com/macros/s/AKfycbzpnW2AmxdMTr7qhE0b-Sx4pgqnUgpT4_T8lP1Nbk4jHryR_dGxi6j-ReEWLx6XNx_N6Q/exec"

# Streamlit app code
st.title("Delete the Last Row")

# Add an action choice for the user
action = st.selectbox("What would you like to do?", ["Delete"])

if st.button("Submit"):
    if action == "Delete":
        action_value = "delete"
        st.write(f"Sending action: {action_value} to delete the last row.")

        # Send only the action to the Google Apps Script for deletion
        response = requests.post(web_app_url, data={'action': action_value})

        # Log the response for debugging
        st.write("Response Status Code:", response.status_code)
        st.write("Response Content:", response.text)

        if response.status_code == 200:
            st.success(response.text)  # Display the exact message returned from the Apps Script
        else:
            st.error(f"There was an error. Status Code: {response.status_code} - {response.text}")

# Load the data into a DataFrame from the Google Sheet
csv_url = "https://docs.google.com/spreadsheets/d/14ExBLiXSqPKFI6jBvwGH63b1LiItPp64To68d36K7GE/export?format=csv"
df = pd.read_csv(csv_url)

# Display the data in the app
st.write(df)
