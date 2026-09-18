import re

def extract_info():

    time_pattern = r'[0-9]{2}:[0-9]{2}:[0-9]{2}'
    ip_pattern = r'\d+\.\d+\.\d+\.\d+'
    level_pattern = r'(INFO|DEBUG|ERROR|WARN)'

    _time = []
    ips = []
    levels = []

    with open("data.log", "r") as f:

        log = f.read()

        _time = re.findall(time_pattern, log)
        ips = re.findall(ip_pattern, log)
        levels= re.findall(level_pattern, log)

    for time, ip, level in zip(_time, ips, levels):

        print(f"{{time: {time:<8}, level: {level:<5}, ip: {ip} }}")
    

extract_info()