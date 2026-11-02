import re

logs = [
    "2030-03-14 ERROR [db] Connection failed after 3 retries",
    "2030-03-14 INFO [web] Server started on port 8080",
    "2030-03-15 ERROR [web] Timeout after 30 seconds",
    "2030-03-15 WARN [db] Slow query: 2500 ms",
]

for line in logs: 

    if 'ERROR' in line:
    
        data = re.findall(r'[0-9]{4}-[0-9]{2}-[0-9]{2}|\[.*\].*', line)

        print(data)

   