'''
import smtplib
import random
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

def send_email():
  sender_email = "noreply.socialnetworkapp@gmail.com"
  sender_password = "mmfg chsp hbhz hhav"  

  user_email = input("Enter your email address: ")
  
  # Generate a random 4-digit verification code
  verification_code = random.randint(1000, 9999)
  
  # Set up the SMTP server
  server = smtplib.SMTP('smtp.gmail.com', 587)
  server.starttls()  
  server.login(sender_email, sender_password)
  
  # Create the email message
  subject = "Your Verification Code"
  body = f"Your verification code is: {verification_code}"
  msg = MIMEMultipart()
  msg['From'] = sender_email
  msg['To'] = user_email
  msg['Subject'] = subject
  msg.attach(MIMEText(body, 'plain'))
  
  # Send the email
  server.sendmail(sender_email, user_email, msg.as_string())
  server.quit()
  
  print("Verification code sent successfully!")
  
  # Ask the user to input the verification code
  user_code = input("Enter the verification code sent to your email: ")
  
  # Check if the input code matches the generated verification code
  if user_code == str(verification_code):
      print("Email verified successfully!")
  else:
      print("Invalid verification code. Please try again.")
      
'''
