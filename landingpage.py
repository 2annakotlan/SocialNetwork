import streamlit as st

def get_landing_page():
  if st.button('Student Sign In'):
      st.session_state.page = "create_account_page"

