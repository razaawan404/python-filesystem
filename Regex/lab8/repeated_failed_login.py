import re
from collections import Counter

def read_log():

    pattern = r'(\d+\.\d+\.\d+\.\d+).*(failed)'
    failed_ip = []
    ip_counter = {}

    with open("ip.log", "r") as f:

        log = f.read()

        failed_ip = re.findall(pattern, log)

    for ips in failed_ip:

        ip = ips[0]

        if ip not in ip_counter:

            ip_counter[ip] = 1
        else:
            ip_counter[ip] += 1

    print("[FLAGGED IPS]")
    for key, val in ip_counter.items():

        if val >= 3:

            print(f"[-] {key:<15} failed {val:<2} times")
        
        
read_log()