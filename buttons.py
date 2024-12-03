def display_email_buttons(login_target_page, signup_target_page):
    email = st.text_input("Email:")
    
    if st.button("Login"):
        if email.endswith("@gmail.com"): 
            st.session_state.page = target_page
        else:
            st.error("Invalid email. Please use a Gmail address.")
    
    if st.button("Sign Up"):
        # Check if email starts with "admin"
        if not email.startswith("admin"):
            st.error("Sign-up failed! Please use an admin email.")
        # Check if email ends with "@gmail.com"
        elif email.endswith("@gmail.com"):
            st.warning("Account already exists. Logging in...")
        # If both checks pass
        else:
            st.success("Sign-up successful! Please log in.")
