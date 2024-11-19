import streamlit as st
import requests
import pandas as pd

# The URL of your deployed Google Apps Script web app
web_app_url = "https://script.google.com/macros/s/AKfycbzpnW2AmxdMTr7qhE0b-Sx4pgqnUgpT4_T8lP1Nbk4jHryR_dGxi6j-ReEWLx6XNx_N6Q/exec"

# Streamlit app code
st.title("Enter Your Name")

# Input box for the user to enter their name
name = st.text_input("Enter your name:")

# Add an action choice for the user
action = st.selectbox("What would you like to do?", ["Append", "Delete"])

if st.button("Submit"):
    # Send the name and action to the Google Apps Script
    if name:  # Ensure the name is not empty
        response = requests.post(web_app_url, data={'name': name, 'action': action})
        if response.status_code == 200:
            st.success("Name successfully submitted!")
        else:
            st.error(f"Failed to submit. Status code: {response.status_code}")
    else:
        st.warning("Please enter a name.")

# Load the data into a DataFrame from the Google Sheet
csv_url = "https://docs.google.com/spreadsheets/d/14ExBLiXSqPKFI6jBvwGH63b1LiItPp64To68d36K7GE/export?format=csv"
df = pd.read_csv(csv_url)

# Display the data in the app
st.write(df)
