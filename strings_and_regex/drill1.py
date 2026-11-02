import re

raw = "  Name: John_Doe99 | Email: John.Doe@TEST.com | Phone: (415) 555-1234  "

def cleaning(raw_str):

    my_list = raw_str.split("|")

    clean_list = [item.strip() for item in my_list]

    extracting(clean_list)
    
    
def extracting(clean_list):

    match_name = re.search(r'^Name:\s[a-zA-Z0-9_.-]+', clean_list[0])
    
    name = match_name.group(0) if match_name else "No match found"

    match_email = re.search(r'^Email:\s[a-zA-Z0-9._-]+@[a-zA-Z0-9_-]+\.[a-zA-Z]{2,3}', clean_list[1])

    raw_email = match_email.group(0)

    if match_email:

        lower_email = raw_email.lower()
    else:
    
        print("No match found")


    match_phone_number = re.search(r'^Phone:\s.*', clean_list[2])

    phone_no = match_phone_number.group(0) if match_phone_number else "No match found"

    print(f"Name:  {name}")
    print(f"Email: {lower_email}")
    print(f"Phone: {phone_no}") 
     
cleaning(raw)