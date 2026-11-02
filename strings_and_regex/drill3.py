import re

html = "<b>Buy now</b> and <b>save big</b> today, <i>ignore this</i>, <b>test me through this</b>"

words_in_html = re.findall(r'<b>(.*?)</b>', html)

for i in words_in_html:

    word = i.split(' ')

    print(f"{i.upper()} ({len(word)} words)")