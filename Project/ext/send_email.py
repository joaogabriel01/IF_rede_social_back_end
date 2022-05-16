import smtplib
import email.message
import os
from dotenv import load_dotenv

load_dotenv()

class SendEmail():
    def send_email(body, subject, to):
        body_email = body

        message = email.message.Message()
        message['Subject'] = subject
        message['From'] =  os.getenv("EMAIL")
        message['To'] = to
        password = os.getenv("PASSWORD_EMAIL")
        message.add_header('Content-Type', 'text/html')
        message.set_payload(body_email)

        s = smtplib.SMTP('smtp.gmail.com: 587')
        s.starttls()

        s.login(message['From'],password)
        s.sendmail(message['From'], [message['To']],message.as_string().encode('utf-8'))