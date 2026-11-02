import re

text = "Name: Eve Age: 30"

finding = re.search(r'Name: ([a-zA-Z0-9]+) Age: ([0-9]+)', text)

print(finding.groups())