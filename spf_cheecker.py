import re
from email import message_from_string
import spf

def get_domain_from_email(email):
    match = re.search(r"@[\w.]+", email)
    return match.group(1).lower() if match else None

def check_spf(sender_address, client_ip):
    try:
        policy = spf.SPF(sender_address, client_ip)
        return policy.check() == 'pass'
    except spf.SPFError:
        return False

def is_email_spoofed(raw_email, client_ip):
    email_message = message_from_string(raw_email)
    sender_address = email_message.get("From", "")
    sender_domain = get_domain_from_email(sender_address)

    if sender_domain and not check_spf(sender_address, client_ip):
        return True  # SPF check failed

    return False  # No signs of email spoofing

# Example usage
email_content = """
From: name.surname1@example.com
To: name.surname2@example.com
Subject: Important Information

This is a legitimate email from example.com.
"""

client_ip = '1.1.1.1'  # Replace with the actual client IP

if is_email_spoofed(email_content, client_ip):
    print("Warning: Possible email spoofing detected!")
else:
    print("Email appears to be legitimate.")
