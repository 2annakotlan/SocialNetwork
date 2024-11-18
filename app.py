import streamlit as st

name = st.text_input("Please enter your name:")

if name:
  st.write(f"Your name is: {name}")
