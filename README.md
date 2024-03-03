# Email Spoofing Detection

## Overview

A Python script that checks for potential email spoofing by verifying the SPF (Sender Policy Framework) of the sender's domain against the client's IP address.

## Usage

1. **Run the Script:**

   - Ensure you have Python installed.

   ```bash
   python email_spoofing_detection.py
   ```

2. **Customize Example:**

   - Modify the `email_content` and `client_ip` variables in the script with your own values.

3. **View Results:**
   - The script will print a warning if potential email spoofing is detected.

## Example

```python
from email import message_from_string
import spf

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
```
