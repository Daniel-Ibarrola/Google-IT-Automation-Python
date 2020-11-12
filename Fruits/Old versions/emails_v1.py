#!/usr/bin/env python3

import email.message
import mimetypes
import os.path
import smtplib

def generate_email(sender, recipient, subject, body, attachment_path):
    """Creates an email with an attachmnet"""
    #Basic email formatting
    message = email.message.EmailMessage()
    message['From'] = sender
    message['To'] = recipient
    message['Subject'] = subject
    message.set_content(body)

    #Process the attachmnet and add it to the email
    attachment_filename = os.path.basename(attachment_path)
    mime_type, _ = mimetypes.guess_type(attachment_path)
    mime_type, mime_subtype = mime_type.split('/', 1)

    with open(attachment_path, 'rb') as ap:
        message.add_attachment(ap.read(), maintype=mime_type, subtype=mime_subtype, filename=attachment_filename)

    return message

def send(message):
    """Sends the mesage to the configured SMTP server."""
    mail_server = smtplib.SMTP('localhost')
    mail_server.send_message(message)
    mail_server.quit()


msg = generate_email('dis96051@gmail.com',
         'dis96051@gmail.com',
         'Upload Completed - Online Fruit Store',
         'All fruits are uploaded to our website successfully. A detailed list is attached to this email.',
         'processed.pdf')
print(msg)
