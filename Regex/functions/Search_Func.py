import re

def search_text(pattern, text):

    result = re.search(pattern, text)

    if result:
        print("Found " + result.group())
    else:
        print("Not Found")

search_text(r'\d+', "my age is 25, 12 is the up")
search_text(r'\d+', "no numbers here")