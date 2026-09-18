import re

def find_error(log):

    for line in log:
    
        if re.search(r'[\d\s:-]+(ERROR|WARN)', line):

            print(line.strip())

with open("error.log", "r") as f:
    find_error(f)