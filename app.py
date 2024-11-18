import streamlit as st
import requests

# Web app URL from Apps Script
url = "https://script.google.com/macros/s/AKfycbwDhkYaN5UXnZwZ8Zdhy0M13wAG5c9gQ3jHWShRMFZndeiqU-IkjE10L6dFYuPTChvUeQ/exec"

# Google Sheets URL (replace with your actual Google Sheets URL)
sheet_url = "https://docs.google.com/spreadsheets/d/1WL1kmqjkMLjNAavhUhNptuSaZ7-7vQEycnDVoDz7mAk/edit"  # Replace with your sheet URL

# Title of the Streamlit app
st.title("Google Sheets Integration")

# Input for the name
name = st.text_input("Enter your name:")

if name:
    # Prepare the data to send in the POST request
    data = {"name": name}

    # Send the POST request to the web app URL
    response = requests.post(url, json=data)

    # Handle the response
    if response.status_code == 200:
        st.success("Data successfully sent!")
        
        # Display the link to Google Sheets that the user can click
        st.markdown(f"Click [here](<{sheet_url}>) to view the updated Google Sheets.")
    else:
        st.error(f"Failed to send data. Status code: {response.status_code}")
