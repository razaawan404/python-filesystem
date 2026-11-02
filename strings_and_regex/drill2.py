import re


text = "Report dates: 3/14/2030, 12-1-2029, 07/04/2031"

dates = re.findall(r'\d+[-/]\d+[-/]\d+', text)

for date in dates:

    parts = re.split(r'[-/]', date)

    month = parts[0]
    day = parts[1]
    year = parts[2]

    print(f"{year}-{month.zfill(2)}-{day.zfill(2)}")