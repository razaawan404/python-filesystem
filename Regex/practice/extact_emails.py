import re


def extract_email(log):

    #extracted_emails = re.findall(r'[\w.-]+@[\w.-]+\.\w+', log)
    extracted_emails = re.findall(r'[a-zA-Z0-9._-]+@[a-zA-Z0-9.-]+\.[a-zA-Z0-9]+', log)

    for email in extracted_emails:

        print(email)

with open("email.log", 'r') as f:
    extract_email(f.read())