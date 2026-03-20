"""
slack_notifier.py
Sends Slack alerts when brute force activity is detected.
"""
from dotenv import load_dotenv
import os
import requests

load_dotenv()
SLACK_WEBHOOK = os.getenv("SLACK_WEBHOOK")

def send_slack_alert(ip, count):
    payload = {
        "text": f"Brute-force attack detected from {ip} with {count} failed attempts."
    }
    response = requests.post(SLACK_WEBHOOK, json=payload)
    if response.status_code != 200:
        print(f"[!] Alert failed to send: {response.text}")
    else:
        print(f"[+] Slack alert sent for {ip}")

if __name__ == "__main__":
    send_slack_alert("192.168.1.100", 8)