import re

page = """From: ali@test.com
        To: bob@test.com
        Sub: Hello

        From: admin@test.com
        To: sam@test.com
        Sub: Alert"""

log = """10:01 INFO 192.168.1.10 ali@test.com login
10:02 INFO 10.0.0.5 /home 200
10:03 WARN 172.16.0.20 bob@test.com failed
10:04 ERROR 192.168.1.15 db failed
10:05 INFO 10.0.0.8 /login 200
10:06 WARN 172.16.0.20 bob@test.com failed
10:07 INFO 192.168.1.10 ali@test.com logout
10:08 INFO 8.8.8.8 /index 200
10:09 ERROR 192.168.1.20 timeout"""

def replace_text(pattern, replacement, text):

    newText = re.sub(pattern, replacement, text)

    print("Old text: " + text)
    print("New Text: " + newText)


# mask all IPs in a log
replace_text(r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}', "X.X.X.X", log)

# mask all emails
replace_text(r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,4}', "***@***.com", page)