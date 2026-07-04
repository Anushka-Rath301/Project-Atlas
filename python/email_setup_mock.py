import smtplib 
import os
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from dotenv import load_dotenv

load_dotenv()

SMTP_SERVER="smtp.gmail.com"
SMTP_PORT=587
EMAIL_ADDRESS=os.getenv("EMAIL_ADDRESS")
EMAIL_PASSWORD=os.getenv("EMAIL_PASSWORD")

def send_email(recipient_mail,subject,body):
    try:
        msg=MIMEMultipart()
        msg["From"]=EMAIL_ADDRESS
        msg["To"]=recipient_mail
        msg["Subject"]=subject

        msg.attach(MIMEText(body,'plain'))

        with smtplib.SMTP(SMTP_SERVER,SMTP_PORT) as server:
            server.starttls()
            server.login(EMAIL_ADDRESS,EMAIL_PASSWORD)
            server.sendmail(EMAIL_ADDRESS,recipient_mail,msg.as_string())
        
        print("Email Sent Successfully")

    except Exception as e:
        print(f"Error sending mail:{e}")

if __name__=="__main__":
    recipient_mail="anushkamusic25@gmail.com"
    subject="FAULT DETECTED"
    body="This is a test email"
    send_email(recipient_mail,subject,body)

