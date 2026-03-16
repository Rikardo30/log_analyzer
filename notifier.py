#A simple Api alerting script using a telegram bot
#Make sure to keep your token and chat id separate in an ignored file to protect your data
#The next goal is to move over to slack instead of telegram in order to have a more professional environment

#Allows us to pull sensitive data from our .env file
from dotenv import load_dotenv
import os
import requests

load_dotenv()
TOKEN = os.getenv("TELEGRAM_TOKEN")
CHAT_ID = os.getenv("TELEGRAM_ID")
#We will call this function in our brute force detection script
def send_telegram_alert(ip, count):
    url = f"https://api.telegram.org/bot{TOKEN}/sendMessage"
    payload = {
        "chat_id": CHAT_ID,
        "text": f"Brute-force attack detected from {ip} with {count} failed attempts."
    }
    requests.post(url, data=payload)
