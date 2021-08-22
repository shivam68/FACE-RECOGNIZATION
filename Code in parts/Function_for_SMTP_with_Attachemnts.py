#Creating a Function For Sending Email With Attachment!
#############################################################################################################
import email, smtplib, ssl
from getpass import getpass
from email import encoders
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import cv2
import numpy as np
import os

sender_email = "rbrishabh76@gmail.com"
receiver_email = "rbrishabh76@gmail.com"

def send_email():
    subject = "Security Alet!! Theft Detected..."
    body = """Hey,
    We found this person in front of your laptop.
    We informed you about this in case of security issues.
    The photo is attached below, recognize him."""
    password = getpass(prompt="Type your password and press enter:")

    # Create a multipart message and set headers
    message = MIMEMultipart()
    message["From"] = sender_email
    message["To"] = receiver_email
    message["Subject"] = subject
    # message["Bcc"] = receiver_email  # Recommended for mass emails

    # Add body to email
    message.attach(MIMEText(body))
   # filename = "document.pdf"  # In same directory as script

    
    # Open PDF file in binary mode
    # Add file as application/octet-stream
    # Email client can usually download this automatically as attachment
    part = MIMEBase("application", "octet-stream")
    part.set_payload(open("detected.jpg", "rb").read())

    # Encode file in ASCII characters to send by email    
    encoders.encode_base64(part)

    # Add header as key/value pair to attachment part
    part.add_header(
    "Content-Disposition",
    f"attachment; filename= detected.jpg",)

    # Add attachment to message and convert message to string
    message.attach(part)
    text = message.as_string()

    # Log in to server using secure context and send email
    context = ssl.create_default_context()
    try:
        with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
            server.login(sender_email, password)
            server.sendmail(sender_email, receiver_email, text)
            server.quit()
            return 0
    except SMTPException as error:
        print ("Error!! Something went wrong")
########################################################################################################
# Creating A Fucntion for Sending Whatsapp Message!!

#pip install pywhatkit
import pywhatkit
#python -m pip install –-upgrade Pillow
import datetime
def send_webwhatsapp():
    pywhatkit.sendwhatmsg('+918700231477', '''We found a person in front of your laptop. 
    We informed you about this in case of security issues Please Check your mail....The photo is attached below, recognize him.'''
                          ,datetime.datetime.now().hour, datetime.datetime.now().minute+2)
    return "Success"