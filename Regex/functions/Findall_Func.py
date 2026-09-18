import re

page = """From: ali@test.com
        To: bob@test.com
        Sub: Hello

        From: admin@test.com
        To: sam@test.com
        Sub: Alert"""

html = """<html>
<head>
<title>Test</title>
</head>
<body>

<h1>Hello</h1>

<p>User: ali@test.com</p>

<a href="https://example.com">Example</a>
<a href="https://test.com/login">Login</a>
<a href="https://test.com/admin">Admin</a>
<a href="https://blog.test.com/post">Blog</a>

<img src="https://test.com/img/logo.png">

<form action="https://test.com/login" method="POST">
<input name="email">
<input name="pass">
<button>Login</button>
</form>

</body>
</html>"""

log = """10:01 INFO 192.168.1.10 ali@test.com login
10:02 INFO 10.0.0.5 /home 200
10:03 WARN 172.16.0.20 bob@test.com failed
10:04 ERROR 192.168.1.15 db failed
10:05 INFO 10.0.0.8 /login 200
10:06 WARN 172.16.0.20 bob@test.com failed
10:07 INFO 192.168.1.10 ali@test.com logout
10:08 INFO 8.8.8.8 /index 200
10:09 ERROR 192.168.1.20 timeout"""

def find_All(pattern, file):

    result = re.findall(pattern, file)

    return result

# extract all emails from a page
emails = re.findall(r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,4}', page)

# extract all IPs from a log
ips = re.findall(r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}', log)

# extract all URLs
urls = re.findall(r'https?://[^\s]+', html)

print("Emails: ", emails)
print("Ips: ", ips)
print("Urls: ", urls)