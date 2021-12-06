import json

class ValidatePassports():
    def __init__(self, credential):
        self.credential = credential

    def validate_byr(self):
        if len(self.credential["byr"]) == 4:
            if int(self.credential["byr"]) <= 2002 and int(self.credential["byr"]) >= 1920:
                self.credential["byr"]["valid"] = True
            else:
                self.credential["byr"]["valid"] = False
        else:
            self.credential["byr"]["valid"] = False

    def validate_iyr(self):
        if len(self.credential["iyr"]) == 4:
            if int(self.credential["iyr"] >= 2010 and int(self.credential["iyr"] <= 2020):
                self.credential["iyr"]["valid"] = True
            else:
                self.credential["iyr"]["valid"] = False

        else:
            self.credential["iyr"]["valid"] = False

    def validate_eyr(self):
        if len(self.credential["eyr"]) == 4:
            if int(self.credential["eyr"] >= 2020) and int(self.credential["eyr"]) <= 2030:
                self.credential["eyr"]["valid"] = True
            else:
                self.credential["eyr"]["valid"] = False
        else:
            self.credential["eyr"]["valid"] = False

    def validate_hgt(self):
        if self.credential["hgt"][-2:] == "cm":
            if int(self.credential["hgt"][:-2]) >= 150 and int(self.credential["hgt"][:-2] <= 193):
                self.credential["hgt"]["valid"] = True
            else:
                self.credential["hgt"]["valid"] = False

        elif self.credential["hgt"][-2:] == "in":
            if int(self.credential["hgt"]) >= 59 and int(self.credential["hgt"]) <= 76:
                self.credential["hgt"]["valid"] = True
            else:
                self.credential["hgt"]["valid"] = False

    def validate_hcl(self):
        if self.credential["hcl"][0] == "#" and self.credential["hcl"][1:].isalnum():
            self.credential["hcl"]["valid"] = True
        else:
            self.credential["hcl"]["valid"] = False

    def validate_ecl





with open("example.txt", "r", newline="\r\n", encoding="utf-8") as f:
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
            credentials = credentials.split(" ")
            credential = {}

            for key_value in credentials:
                kv = key_value.split(":")
                credential[kv[0]] = kv[1]

            print(json.dumps(credential, indent=2))

            # credential_dict = {}
            print("\n" + str(credentials) + "\n")


            if credentials.count(":") == 8:
                valid_passports += 1
            elif credentials.count(":") == 7 and "cid" not in credentials:
                valid_passports += 1

            # print(credentials)

            # Reset credentials list
            credentials = []

print("Valid passports: " + str(valid_passports))
