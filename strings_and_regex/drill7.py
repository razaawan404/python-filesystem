import re

text = "Order #101 shipped, order #202 delayed, order #303 cancelled"

print(re.search(r'[0-9]+', text).group())

print(re.findall(r'[0-9]+', text))

data = re.findall(r'[0-9]+\s[a-zA-Z]+', text)

for d in data:

    print(d)
