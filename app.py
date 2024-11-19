import streamlit as st
import requests

# The URL of your deployed Google Apps Script web app
web_app_url = "https://script.google.com/macros/s/AKfycbzpnW2AmxdMTr7qhE0b-Sx4pgqnUgpT4_T8lP1Nbk4jHryR_dGxi6j-ReEWLx6XNx_N6Q/exec"

# Streamlit app code
st.title("Enter Your Name")

# Input box for the user to enter their name
name = st.text_input("Enter your name:")

if st.button("Submit"):
    if name:
        # Send the name to the Google Apps Script
        response = requests.post(web_app_url, data={'name': name})
        
        if response.status_code == 200:
            st.success(f"Name '{name}' has been saved successfully!")
        else:
            st.error("There was an error saving the name.")
    else:
        st.warning("Please enter a name.")
