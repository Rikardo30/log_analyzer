# Simple brute-force attack detection script for SSH login attempts
import re

#Constants
LIMIT = 5
LOG_PATH = 'auth.log'

def detect_brute_force():
#The pattern to extract IP adresses from the log file.
    ip_pattern = r'\d+\.\d+\.\d+\.\d+'
    ip_attempts = {}

    with open(LOG_PATH, 'r') as file:
        for line in file:
            ip_match = re.search(ip_pattern, line)
            if "Failed" in line and ip_match:
                ip = ip_match.group(0)
                ip_attempts[ip] = ip_attempts.get(ip, 0) + 1
                
    for ip, count in ip_attempts.items():
        if count >= LIMIT:
            print(f'[!] BRUTE FORCE DETECTED: {ip} — {count} failed attempts')

if __name__ == "__main__":
    detect_brute_force()
