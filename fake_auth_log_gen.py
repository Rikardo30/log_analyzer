"""
fake_auth_log_generator.py
Generates a fake SSH auth.log file for SIEM testing purposes.
"""
import random
import datetime

#     CONSTANTS
LOG_FILE = "auth.log"
LOG_ENTRIES = 50
USER = ["alice", "bob", "charlie", "dave", "tommy", "james", "jen", "darcy", "tom", "kevin", "darla"]
HOSTS = ["172.16", "192.168", "10"]
ATTACKER_IPS = ["192.168.1.100", "10.0.0.55", "172.16.5.22"]

# generates random log entries for both succesful and failed login attempts
def generate_fake_auth_log():
    with open(LOG_FILE, 'a') as f:
        for i in range(LOG_ENTRIES):
            random_user = random.choice(USER) + "_" + str(random.randint(1, 1000))
            random_ip = random.choice(HOSTS) + "." + str(random.randint(1, 254)) + "." + str(random.randint(1, 254))
            time_stamp = datetime.datetime.now().strftime('%b %d %H:%M:%S')
            denied_accept = random.choice(["Failed password for invalid user", "Accepted password for"])
            log_entry = f"{time_stamp} server sshd[{random.randint(1000,9999)}]: {denied_accept} {random_user} from {random_ip} port 22 ssh2\n"
            f.write(log_entry)
# generates additional log entries to simulate brute force attack traffic
def generate_attack_traffic():
    with open(LOG_FILE, 'a') as f:
        for i in range(random.randint(15, 25)):
            random_user = random.choice(USER) + "_" + str(random.randint(1, 1000))
            time_stamp = datetime.datetime.now().strftime('%b %d %H:%M:%S')
            attacker_entry = f"{time_stamp} server sshd[{random.randint(1000,9999)}]: Failed password for invalid user {random_user} from {random.choice(ATTACKER_IPS)} port 22 ssh2\n"
            if random.random() < 0.7:  # 70% chance to generate
                f.write(attacker_entry)

if __name__ == "__main__":
    generate_fake_auth_log()
    generate_attack_traffic()