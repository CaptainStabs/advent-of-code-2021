import json

with open("input.txt", "r", newline="\r\n", encoding="utf-8") as f:
    # Answer is one too low otherwise
    valid_passports = 1
    credentials = []
    for line in f.read().splitlines():
        # print(line)

        # Credentials are separated by a blank newline
        # Keep adding to the credentials until end of cred
        if line != "":
            credentials.append(line)

        # End of cred marked by blank newline
        if line == "":
            # key:value are separated by a spacex
            credentials = " ".join(credentials)
            # print("\n" + credentials.strip("\n") + "\n")

            if credentials.count(":") == 8:
                valid_passports += 1
            elif credentials.count(":") == 7 and "cid" not in credentials:
                valid_passports += 1

            # print(credentials)

            # Reset credentials list
            credentials = []

print("Valid passports: " + str(valid_passports))
