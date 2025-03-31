from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
from pathlib import Path
from string import Template
import smtplib

template = Template(Path("template").read_text())

email_account = "test@gmail.com"
email_password = "test"
path_to_photo = Path("kostia.png")

messsage = MIMEMultipart()
messsage["from"] = "Kostiantyn Teltov"
messsage["to"] = email_account
messsage["subject"] = "This is a test"

body = template.substitute({"name": "John"})
# body = template.substitute(name="John") - alternative

messsage.attach(MIMEText(body, "html"))
messsage.attach(MIMEImage(path_to_photo.read_bytes()))

with smtplib.SMTP(host="smtp.gmail.com", port=587) as smpt:
    smpt.ehlo()
    smpt.starttls()
    smpt.login(email_account, email_password)
    smpt.send_message(messsage)
    print("Sent...")
