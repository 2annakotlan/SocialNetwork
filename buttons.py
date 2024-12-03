import streamlit as st

def display_button(label, target_page):
    if st.button(label):
        st.session_state.page = target_page
        
def display_email_buttons(login_target_page, signup_target_page):
    email = st.text_input("Email:")
    existing_domain = "@gmail.com"
    non_existing_domain = "@yahoo.com"
    
    if st.button("Login"):
        if email == f"admin{existing_domain}"
            st.session_state.page = login_target_page
        elif not email.startswith(f"admin"):
            st.error("Please use an admin email")
        elif not email.endswith(existing_domain): 
            st.error("Please use an existing domain")

    if st.button("Sign Up"):
        if email == f"admin{non_existing_domain}"
            st.session_state.page = signup_target_page
        elif not email.startswith(f"admin"):
            st.error("Please use an admin email")
        elif not email.endswith(non_existing_domain): 
            st.error("Domain already exists")

