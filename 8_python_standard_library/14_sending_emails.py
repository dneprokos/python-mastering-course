from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
from pathlib import Path
import smtplib

email_account = "test@gmail.com"
email_password = "test"
path_to_photo = Path("kostia.png")

messsage = MIMEMultipart()
messsage["from"] = "Kostiantyn Teltov"
messsage["to"] = email_account
messsage["subject"] = "This is a test"

messsage.attach(MIMEText("Body", "plain"))
messsage.attach(MIMEImage(path_to_photo.read_bytes()))

with smtplib.SMTP(host="smtp.gmail.com", port=587) as smpt:
    smpt.ehlo()
    smpt.starttls()
    smpt.login(email_account, email_password)
    smpt.send_message(messsage)
    print("Sent...")
