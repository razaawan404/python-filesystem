import re

text = "My IP is 192.168.1.1 and backup is 10.0.0.5"

# search - finds first match
result = re.search(r'\d+\.\d+\.\d+\.\d+', text)
print(result.group())

# findall - finds all matches
results = re.findall(r'\d+\.\d+\.\d+\.\d+', text)
print(results)