import streamlit as st

def display_dataframe(df):
    st.write("Here is the data:")
    st.dataframe(df)

def get_user_input():
    return st.text_input("Enter a name to add:")
