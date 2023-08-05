from email.message import EmailMessage
import ssl
import smtplib
import imghdr

import dotenv
from dotenv import load_dotenv
import os

# subject = 'BlueStarMasterList Update'
# body = """
# BlueStarMasterList has been updated
# """

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
    em.set_content(body)

    with open(attachementPath, 'rb') as f:
        subType = imghdr.what(f.name)
        em.add_attachment(f.read(), maintype='image', subtype=subType, filename=attachmentName)

    context = ssl.create_default_context()

    with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as smtp:
        smtp.login(emailSender, emailPassword)
        smtp.send_message(em)
#
# if __name__ == '__main__':
#     sendMail(subject, body)

