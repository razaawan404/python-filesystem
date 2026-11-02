import re

phones = ["415-555-1234", "555-1234", "(415) 555-1234", "hello", "415-555-1234-4444"]

for ph in phones:

    if re.match(r'^([0-9]+\-){1,2}[0-9]+$', ph):

        print(f"{ph:<20} -> valid")

    elif re.search(r'^\([0-9]+\)\s([0-9]+\-?){2}', ph):

        print(f"{ph:<20} -> valid")

    else:

        print(f"{ph:<20} -> invalid")