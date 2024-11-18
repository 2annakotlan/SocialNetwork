import streamlit as st

# Use Streamlit's text_input for user input
name = st.text_input("Please enter your name:")

# Display the user's input if provided
if name:
    st.write(f"Your name is: {name}")
