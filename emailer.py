from email.message import EmailMessage
import ssl
import smtplib

import dotenv
from dotenv import load_dotenv
import os

subject = 'BlueStarMasterList Update'
body = """ 
BlueStarMasterList has been updated 
"""

dotenv.load_dotenv()

def sendMail(subject: str, body:str):
    emailSender = os.getenv('EMAILSENDER')
    emailPassword = os.getenv('APPPASSWORD')
    emailReceiver = os.getenv('EMAILRECEIVER')

    em = EmailMessage()
    em['From'] = emailSender
    em['To'] = emailReceiver
    em['Subject'] = subject
    em.set_content(body)

    context = ssl.create_default_context()

    with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as smtp:
        smtp.login(emailSender, emailPassword)
        smtp.sendmail(emailSender, emailReceiver, em.as_string())

def sendMailWithAttachement(subject: str, body:str, attachementPath: str, attachmentName: str):
    emailSender = os.getenv('EMAILSENDER')
    emailPassword = os.getenv('APPPASSWORD')
    emailReceiver = os.getenv('EMAILRECEIVER')

    em = EmailMessage()
    em['From'] = emailSender
    em['To'] = emailReceiver
    em['Subject'] = subject

    with open(attachementPath, 'rb') as f:
        em.add_attachment(f.read(), maintype='image', subtype='png', filename=attachmentName)

    context = ssl.create_default_context()

    with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as smtp:
        smtp.login(emailSender, emailPassword)
        smtp.sendmail(emailSender, emailReceiver, em.as_string())

if __name__ == '__main__':
    sendMail(subject, body)

