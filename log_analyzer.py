# This script analyzes the auth.log file to extract IP addresses, usernames, and determine if login attempts were successful or not.
import re
#File path that will be analyzed.
LOG_PATH = 'auth.log'

#Defines what we are looking for in the log file
#In this case we want to extract the IP address and the username from each line of the log file. 
#We also want to determine if the login attempt was successful or not based on whether the line contains "Failed" or "Accepted".
def analyze_log():
    ip_pattern = r'\d+\.\d+\.\d+\.\d+'
    pattern = r'(\S+) from'

    with open(LOG_PATH, 'r') as file:

        for line in file:
            ip_match = re.search(ip_pattern, line)
            user_match = re.search(pattern, line)
            if "Failed" in line: #If the line contains "Failed", we consider it an invalid login attempt.
                status = "INVALID"
            elif "Accepted" in line: #If the line contains "Accepted", we consider it a valid login attempt.
                status = "VALID"
            if ip_match and user_match:
                print(f'[{ip_match.group(0)}] [{user_match.group(1)}] {status}')

if __name__ == "__main__":
    analyze_log()