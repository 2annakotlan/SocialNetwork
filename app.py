import streamlit as st
from pages import *

if 'page' not in st.session_state:
    st.session_state.page = 'landing_page'
if st.session_state.page == 'landing_page':
    display_landing_page()
if st.session_state.page == 'profile_info':
    display_student_login_page()
if st.session_state.page == 'admin_login_page':
    display_admin_login_page()
if st.session_state.page == 'student_login_page':
    display_student_login_page()
if st.session_state.page == 'student_profile_page':
    display_student_profile_page()
if st.session_state.page == 'student_landing_page':
    display_student_landing_page()
if st.session_state.page == 'admin_landing_page':
    display_admin_landing_page()
