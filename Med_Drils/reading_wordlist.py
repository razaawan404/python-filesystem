def read_pass_file():

    seen = set()
    new_pass = []

    with open("pass.txt", "r") as f:

        for line in f:
            _pass = line.strip()

            if _pass == "":
                continue

            if _pass not in seen:
                seen.add(_pass)
                new_pass.append(_pass)

    for p in new_pass:
        print(p)
            
read_pass_file()