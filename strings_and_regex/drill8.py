import re

text = "I like cats, dogs, and Caterpillars but not Dogma"

print(re.findall(r'\bcats\b|\bdogs\b', text))

print(re.search(r'Cat', text).group())

print(re.search(r'Cat(erpillar|s)', text).group(0, 1))