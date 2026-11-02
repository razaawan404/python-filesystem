import re

usernames = ["cool_Guy99", "bad username!", "X", "valid_one_123456789012345"]


for names in usernames:

    if len(names) < 3:

        print(f"{names:<20} -> invalid (too short, needs 3-20 chars)")

    if len(names) > 20:

        print(f"{names:<20} -> invalid (too long, {len(names)} chars > 20)")

    