import re


print(re.search(r'a+', "aaa").group())
print(re.search(r'a*', "aaa").group())
print(re.search(r'a?', "aaa").group())