'''
import streamlit as st
from googlesheets import get_sheets_service, append_row_to_sheet

st.set_page_config(page_title="Add Info", layout="centered")
st.title("Add Your Information")

with st.form(key="input_form"):
    name = st.text_input("Name:")
    friends = st.text_area("Friends (comma separated):", value="")
    interests = st.text_area("Interests (comma separated):")
    activities = st.text_area("Activities (comma separated):", value="")
    submit = st.form_submit_button("Submit")

if submit:
        friends = friends if friends else ""
        activities = activities if activities else ""
        df = append_row_to_sheet(get_sheets_service(), name, friends, interests, activities)
        st.success("Info added!")
        st.write(df)
else:
        st.warning("Please fill in 'Name' and 'Interests'.")
'''

import streamlit as st
from google.oauth2.service_account import Credentials
from googleapiclient.discovery import build
from email.mime.text import MIMEText
import base64

def create_gmail_service():
    credentials = Credentials.from_service_account_info(
        st.secrets["google_service_account"], 
        scopes=['https://www.googleapis.com/auth/gmail.send']
    )
    return build('gmail', 'v1', credentials=credentials)

def create_message(sender, to, subject, body):
    message = MIMEText(body)
    message['to'] = to
    message['from'] = sender
    message['subject'] = subject
    return {'raw': base64.urlsafe_b64encode(message.as_bytes()).decode()}

def send_email(service, sender, recipient, subject, body):
    message = create_message(sender, recipient, subject, body)
    try:
        sent_message = service.users().messages().send(userId='me', body=message).execute()
        st.success(f"Email sent successfully! Message Id: {sent_message['id']}")
    except Exception as error:
        st.error(f"An error occurred: {error}")

# Streamlit App
st.title("Send Email with Gmail API")

recipient = st.text_input("Recipient Email")
subject = st.text_input("Subject")
body = st.text_area("Email Body")

if st.button("Send Email"):
    service = create_gmail_service()
    sender = "your-service-account-email@example.com"  # Replace with a verified sending email
    if recipient and subject and body:
        send_email(service, sender, recipient, subject, body)
    else:
        st.warning("Please fill in all fields.")
