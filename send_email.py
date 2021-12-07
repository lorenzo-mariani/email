import imghdr
import mimetypes
import os
import smtplib

from email.message import EmailMessage

server = input('Type the SMTP server you want to connect to: ')
port = int(input('Type the port you want to connect to: '))

sender_email = input('Type you email address: ')
sender_password = input('Type your password: ')

contacts = []
c_num = int(input('How many contacts do you want to send the email to? '))

for i in range (c_num):
    c = input(f'Type contact n.{i+1}: ')
    contacts.append(c)

subject = input('Type the subject of the email: ')
body = input('Type the body of the email: ')

msg = EmailMessage()
msg['Subject'] = subject
msg['From'] = sender_email
msg['To'] = ', '.join(contacts)
msg.set_content(body)

while True:
    to_attach = (input('Do you want to attach files? Type "yes" or "no": ')).lower()

    if to_attach == 'yes' or to_attach == 'no':
        break
    else:
        print('ERROR! You have to answer with "yes" or "no"')

if to_attach == 'yes':
    files_to_attach = []
    f_num = int(input('How many files do you want to attach? '))

    for i in range (f_num):
        f = input(f'Type the path to attachment n.{i+1}: ')
        files_to_attach.append(f)

    for file in files_to_attach:
        path = file
        file_name = os.path.basename(path)
        mime_type, _ = mimetypes.guess_type(path)
        mime_type, mime_subtype = mime_type.split('/', 1)

        with open(path, 'rb') as p:
            msg.add_attachment(p.read(), maintype=mime_type, subtype=mime_subtype, filename=file_name)

with smtplib.SMTP_SSL(server, port) as smtp:
    smtp.login(sender_email, sender_password)
    smtp.send_message(msg)
