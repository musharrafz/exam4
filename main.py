from email.message import EmailMessage
import smtplib
from dotenv import load_dotenv

load_dotenv()
import os

message = EmailMessage()
message['from'] = os.getenv('ML')
message['to'] = os.getenv('TO')
message['subject'] = "Ibragimov Musharraf exam_modul_4"
with open("musharraf.txt", 'r') as file:
    file_data = file.read()
    file_name = file.name
message.add_attachment(file_data, subtype="octet-stream", filename=file_name)

with open("main.py", 'r') as file:
    file_data = file.read()
    file_name = file.name
message.add_attachment(file_data, subtype="octet-stream", filename=file_name)

HOST = os.getenv('HOST')
PORT = os.getenv('PORT')
EMAIL = os.getenv('ML')
PASSWORD = os.getenv('PASS')
with smtplib.SMTP_SSL(HOST, PORT) as server:
    server.login(EMAIL, PASSWORD)
    server.send_message(message)
