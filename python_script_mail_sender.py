from email.message import EmailMessage
import ssl
import smtplib

email_sender = ""
email_sender_app_password = ""

email_reciever = ""

subject = "Just trying out something"

body = """
Hello!!
Just sending this mail to test out something

No need to worry!

I am not a hacker that is going tp steal ur money

"""
em = EmailMessage()

em['From'] = email_sender
em['To'] = email_reciever
em['subject'] = subject
em.set_content(body)

context = ssl.create_default_context()

with smtplib.SMTP_SSL('smtp.gmail.com', 465, context = context) as smtp:
    smtp.login(email_sender, email_sender_app_password)
    smtp.sendmail(email_sender, email_reciever, em.as_string())



