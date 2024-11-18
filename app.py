import requests
import streamlit as st

# Streamlit interface to collect name input
st.title("Google Sheets Integration")

name = st.text_input("Enter your name:")

if name:  # Only trigger the POST request if the name is provided
    url = "https://script.google.com/macros/s/AKfycbwWmHa7QazzgSmMMLRkujc0npQ6_Zr2JP7Hki9W9VilrqgKllTiipB-HOHSSdZqDaSc7g/exec"
    data = {"name": name}  # The data you want to send (name in this case)

    # Send POST request to the Apps Script Web App
    response = requests.post(url, json=data)

    # Provide feedback based on the response status
    if response.status_code == 200:
        st.success("Data successfully sent!")
    else:
        st.error(f"Failed to send data. Status code: {response.status_code}")
