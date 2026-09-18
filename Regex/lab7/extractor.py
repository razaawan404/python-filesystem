import re

def url_extractor():

    pattern = r'https?://[a-zA-Z0-9.-]+(?::[0-9]+)?(?:/.*)?'

    urls = []

    with open("url.log", "r") as f:

        log = f.read()

        urls = re.findall(pattern, log)

    for url in urls:

        if "http:" in url:

            print(f"{url:<55}---> [INSECURE]")
        else:

            print(f"{url:<55}---> [SECURE]")

url_extractor()