import re

def mask_all_sen_data(data):

    updated_log1 = re.sub(r'\d+\.\d+\.\d+\.\d+', "X.X.X.X", data)

    updated_log2 = re.sub(r'[\w._-]+@[\w-]+\.\w+', "***@***.com", updated_log1)

    print(updated_log2)

with open("sensitive_data.log", "r") as f:

    mask_all_sen_data(f.read())