import re

try:
    with open("Dummy_Email_Contacts.txt", "r", encoding="utf-8") as p:
        content = p.read()
except FileNotFoundError:
    print("File not found")
else:
    email_pattern = r"[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}"
    mail_addresses = sorted(set(re.findall(email_pattern, content)))
    if mail_addresses:
        with open("Email Addresses.txt", "w", encoding="utf-8") as f:
            for addresses in mail_addresses:
                f.write(addresses + "\n")
        print("Email Extracted Successfully")
    else:
        print("No Email Address Was Found")


