[Python SIEM Lite]
A lightweight Security Information and Event Management (SIEM) tool built in Python. I built this project to understand what enterprise tools like Splunk and Wazuh are actually doing under the hood — parsing logs, extracting indicators, and firing alerts when something looks wrong.

[What it does]

Generates realistic fake SSH auth.log files to simulate both normal traffic and brute force attacks
Parses log files using regex to extract IP addresses and usernames from each event
Detects brute force login attempts by counting failed logins per IP and alerting when a threshold is exceeded
(In progress) Sends real-time alerts to a messaging platform when an attack is detected


[Project Structure]
SIEM/
├── fake_auth_log_gen.py      # Generates fake SSH auth.log with normal and attack traffic
├── log_analyzer.py           # Parses logs and extracts IPs, usernames, and login status
├── brute_force_detector.py   # Detects brute force patterns and fires alerts
├── auth.log                  # Generated log file (not tracked in git)
└── .env                      # API tokens and secrets (not tracked in git)

[How to run it]
1. Generate a fake log file:
bashpython fake_auth_log_gen.py
2. Analyze the log:
bashpython log_analyzer.py
3. Run brute force detection:
bashpython brute_force_detector.py

[Example output]
[+] User: jen_718 | IP: 192.168.76.23 | INVALID
[+] User: alice_478 | IP: 172.16.157.12 | VALID
[!] BRUTE FORCE DETECTED: 192.168.1.100 — 9 failed attempts
[!] BRUTE FORCE DETECTED: 10.0.0.55 — 6 failed attempts

[Why I built this]
I'm studying cybersecurity with a focus on Detection Engineering. Most learning resources tell you how to use SIEM tools, but not how they work. Building one from scratch — even a simple version — forced me to understand log structure, pattern matching, and detection logic at a level that using Splunk alone never would have.
This is an active project. Upcoming stages include Telegram/Slack alerting, CSV report exports, and eventually connecting it to real Wazuh logs from my homelab.

Stack

Python 3
re — regex parsing
datetime / random — log generation
requests — alerting (coming in Stage 4)


Author
Built by Ricardo — cybersecurity student and tech lover based in Houston, TX working toward a Cybersecurity career.