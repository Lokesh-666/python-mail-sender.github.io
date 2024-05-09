import smtplib
import ssl
import os
from email.message import EmailMessage

def send_email(sender_email, sender_password, receiver_email, subject, body):
    # Create a secure SSL context
    context = ssl.create_default_context()
    
    # Initialize EmailMessage object
    email = EmailMessage()
    email['From'] = sender_email
    email['To'] = receiver_email
    email['Subject'] = subject
    email.set_content(body)
    
    try:
        # Connect to SMTP server and send email
        with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as smtp:
            smtp.login(sender_email, sender_password)
            smtp.send_message(email)
        print("Email sent successfully!")
    except Exception as e:
        print(f"An error occurred: {e}")

def main():
    sender_email = os.getenv("SENDER_EMAIL")
    sender_password = os.getenv("SENDER_PASSWORD")
    receiver_email = input("Enter receiver's email address: ")
    subject = input("Enter email subject: ")
    body = input("Enter email body: ")

    send_email(sender_email, sender_password, receiver_email, subject, body)

if __name__ == "__main__":
    main()
