import streamlit as st

def display_landing_page():
    st.write("Login")
    email = st.text_input("Enter your email:", "")
    if st.button("Login"):
        st.session_state.page = 'profile_info'  # Set the page to account info
 
def display_profile_info_page():
    st.write("Account Info")
    
    
