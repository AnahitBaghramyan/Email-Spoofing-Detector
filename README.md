# Email Spoofing Detection Readme

## Description

This Python script checks for email spoofing by verifying the sender's domain using SPF (Sender Policy Framework) and the client's IP address. It parses an email message and performs SPF checks to determine if the email is potentially spoofed.

## Features

- **Domain Extraction:** Extracts the sender's domain from the email address.
- **SPF Check:** Utilizes the SPF library to verify the legitimacy of the sender's domain.
- **Email Spoofing Detection:** Detects potential email spoofing based on SPF check results.

## Usage

1. Provide the email content in the `email_content` variable.
2. Replace the `client_ip` variable with the actual client IP address.
3. Run the script to check for email spoofing.

## Functions

### `get_domain_from_email(email)`

Extracts the domain from the given email address.

### `check_spf(sender_address, client_ip)`

Performs SPF checks on the sender's domain using the provided sender address and client IP.

### `is_email_spoofed(raw_email, client_ip)`

Checks if the email is potentially spoofed based on SPF results.

## Example Usage

```python
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
```
