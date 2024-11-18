import streamlit as st
import requests

# Web app URL from Google Apps Script
url = "https://script.google.com/macros/s/AKfycbznlffgWfUxLqix1FLQGEKXpZaXj3mHs0cZq6fGE2iN79YKz2SpKKWfNsImDOvfdvVX/exec"

# Google Sheets URL (replace with your actual Google Sheets URL)
sheet_url = "https://docs.google.com/spreadsheets/d/1WL1kmqjkMLjNAavhUhNptuSaZ7-7vQEycnDVoDz7mAk/edit"  # Replace with your sheet URL

# Title of the Streamlit app
st.title("Google Sheets Integration")

# Inputs for data
name = st.text_input("Enter your name:")

# When all inputs are filled, send the data to Google Apps Script
if name:
    # Prepare the data to send in the POST request
    data = {"name": name}

    # Send the POST request to the web app URL
    response = requests.post(url, json=data)

    # Handle the response
    if response.status_code == 200:
        st.success("Data successfully sent!")
        st.markdown(f"Click [here](<{sheet_url}>) to view the updated Google Sheets.")
    else:
        st.error(f"Failed to send data. Status code: {response.status_code}")
