
import os
import smtplib
from email.message import EmailMessage
email_adress = os.environ.get('email_adress')
email_pass = os.environ.get('email_pass')

msg=EmailMessage()
msg['Subject']=str(input('Enter message subject : \n'))
msg['From']=email_adress
msg.set_content(str(input('Enter message text : \n')))
msg['To']=str(input('Enter the reciever : \n'))


with smtplib.SMTP_SSL('smtp.gmail.com',465) as smtp:
    smtp.login(email_adress,email_pass)

    smtp.send_message(msg)

print('Email sent !')

