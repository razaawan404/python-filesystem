import re

def pass_strenght_checker(password):

    check_passed = True

    print(f"[{password}]")

    if not re.search(r'.{8,}', password):

        print("[-] length less than 8")
        check_passed = False

    if not re.search(r'[A-Z]', password):

        print("[-] Dont contain any Upper-case")
        check_passed = False

    if not re.search(r'[a-z]', password):

        print("[-] Dont contain any lower-case")
        check_passed = False

    if not re.search(r'\d', password):

        print("[-] Dont contain any digit")
        check_passed = False

    if not re.search(r'[!@#$%]', password):

        print("[-] Dont contain any symbols")
        check_passed = False

    if (check_passed):

        print("[+] Strong Password")

    
    #print(f"[+] Valid Password: {password}")

    print()
    print()

with open("passwords.txt", "r") as f:

    for pass_ in f:

        pass_strenght_checker(pass_.strip())