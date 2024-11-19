import streamlit as st
import requests

# The URL of your deployed Google Apps Script web app
web_app_url = "https://script.google.com/macros/s/AKfycbzpnW2AmxdMTr7qhE0b-Sx4pgqnUgpT4_T8lP1Nbk4jHryR_dGxi6j-ReEWLx6XNx_N6Q/exec"

st.title("Manage Names in Dataset")

# Input box for the user to enter their name
name = st.text_input("Enter the name:")

# Add Name Button
if st.button("Add Name"):
    if name:
        # Send the name with action 'add' to the Google Apps Script
        response = requests.post(web_app_url, data={'action': 'add', 'name': name})
        
        # Log the response for debugging
        st.write("Response Status Code:", response.status_code)
        st.write("Response Content:", response.json())
        
        if response.status_code == 200:
            response_data = response.json()
            if response_data.get("success"):
                st.success(response_data.get("message"))
            else:
                st.error(response_data.get("message"))
        else:
            st.error(f"There was an error. Status Code: {response.status_code}")
    else:
        st.warning("Please enter a name.")

# Delete Name Button
if st.button("Delete Name"):
    if name:
        # Send the name with action 'delete' to the Google Apps Script
        response = requests.post(web_app_url, data={'action': 'delete', 'name': name})
        
        # Log the response for debugging
        st.write("Response Status Code:", response.status_code)
        st.write("Response Content:", response.json())
        
        if response.status_code == 200:
            response_data = response.json()
            if response_data.get("success"):
                st.success(response_data.get("message"))
            else:
                st.error(response_data.get("message"))
        else:
            st.error(f"There was an error. Status Code: {response.status_code}")
    else:
        st.warning("Please enter a name.")


import pandas as pd

# Publicly shared Google Sheet CSV link
csv_url = "https://docs.google.com/spreadsheets/d/14ExBLiXSqPKFI6jBvwGH63b1LiItPp64To68d36K7GE/export?format=csv"

# Load the data into a DataFrame
df = pd.read_csv(csv_url)

# Print the DataFrame
st.write(df)

