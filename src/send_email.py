import json
import smtplib
from email.message import EmailMessage

def send_email():
    email_path = "./data/emails.json"
    email_content = "./data/templates/temp.txt"
     
    # Fetching Emails in this part
    with open(email_path) as file:
        recipients = json.load(file)
    
    if not recipients:
        print("No emails found in emails.json")
        print("Please add some emails first ...")
        return
    
    # Fetching Email content 
    with open(email_content) as file:
        content = file.read()
    
    if not content.strip():
        print("Your email is empty...")
        print("Write one before sending...")
        return
    
    # Email details

    # sender_email = input("Enter your gmail : ")
    # sender_password = input("Enter password : ")
    sender_email = "letscheckit2007@gmail.com"
    sender_password = "yerv iiag khkq abzd"
    subject = input("Enter email Subject : ")

    # Preparing Email
    msg = EmailMessage()
    msg['From'] = sender_email
    msg['Subject'] = subject
    msg.set_content(content)

    # Conforming 
    confirm = input("Are you sure you want to send this email.  y/n  : ")
    if confirm.lower() != 'y':
        print("Canceled")
        return
    
    # Sending the Email
    with smtplib.SMTP_SSL("smtp.gmail.com", 465) as smtp:
        smtp.login(sender_email, sender_password)

        for r in recipients:
            msg['To'] = r
            smtp.send_message(msg)
            del msg['To']


print("\nEmails sent successfully!")

    