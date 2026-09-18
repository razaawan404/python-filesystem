import re


def extract_ip():

    ips = []

    with open("ip.log", "r") as f:

        log = f.read()

        ips = re.findall(r'\d+\.\d+\.\d+\.\d+', log)

    check_validate_ips(ips)

def check_validate_ips(ips):

    pattern = r'^((25[0-5]|2[0-4][0-9]|1[0-9][0-9]|[1-9]?[0-9])\.){3}(25[0-5]|2[0-4][0-9]|1[0-9][0-9]|[1-9]?[0-9])$'
    validated_ips = []

    for ip in ips:

        if re.fullmatch(pattern, ip):

            validated_ips.append(ip)

    for ip in validated_ips:
        print(ip)

extract_ip()
