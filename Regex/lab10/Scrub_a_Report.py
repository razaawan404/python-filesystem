import re

def read_data():

    ip_pattern = r'\d+\.\d+\.\d+\.\d+'
    email_pattern = r'[a-zA-Z0-9_.-]+@[a-zA-Z0-9]+\.[a-zA-Z]{2,3}'
    ph_no_pattern = r'\+92\s[0-9]{3}\s[0-9]{7}'

    with open("sensitive_data.log", "r") as f:

        log = f.read()

        text1 = check_ip(ip_pattern, log)
        text2 = check_emails(email_pattern, text1)
        final_report = check_phone_no(ph_no_pattern, text2)

        print(final_report)

def check_ip(pattern, log):

    updated_text = re.sub(pattern, "[IP REMOVED]", log)

    return updated_text

def check_emails(pattern, log):

    updated_text = re.sub(pattern, "[EMAIL REMOVED]", log)

    return updated_text

def check_phone_no(pattern, log):

    updated_text = re.sub(pattern, "[PHONE REMOVED]", log)

    return updated_text

read_data()

