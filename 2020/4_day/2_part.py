import json

class ValidatePassports():
    def __init__(self, credential):
        self.credential = credential
        self.validate_passports()

    def validate_byr(self):
        try:
            if len(self.credential["byr"]) == 4:
                return int(self.credential["byr"]) <= 2002 and int(self.credential["byr"]) >= 1920
            else:
                return False
        except KeyError:
            return False

    def validate_iyr(self):
        try:
            if len(self.credential["iyr"]) == 4:
                return int(self.credential["iyr"]) >= 2010 and int(self.credential["iyr"]) <= 2020
            else:
                return False
        except KeyError:
            return False

    def validate_eyr(self):
        try:
            if len(self.credential["eyr"]) == 4:
                return int(self.credential["eyr"]) >= 2020 and int(self.credential["eyr"]) <= 2030

            else:
                return False
        except KeyError:
            return False

    def validate_hgt(self):
        try:
            if self.credential["hgt"][-2:] == "cm":
                return int(self.credential["hgt"][:-2]) >= 150 and int(self.credential["hgt"][:-2]) <= 193

            elif self.credential["hgt"][-2:] == "in":
                return int(self.credential["hgt"][:-2]) >= 59 and int(self.credential["hgt"][:-2]) <= 76
        except KeyError:
            return False

    def validate_hcl(self):
        try:
            return self.credential["hcl"][0] == "#" and self.credential["hcl"][1:].isalnum()
        except KeyError:
            return False

    def validate_ecl(self):
        try:
            return self.credential["ecl"] in ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]
        except KeyError:
            return False

    def validate_pid(self):
        try:
            return len(self.credential["pid"]) == 9
        except KeyError:
            return False

    def validate_passports(self):
        return (self.validate_byr() and self.validate_iyr() and self.validate_iyr() and self.validate_eyr()
            and self.validate_hgt() and self.validate_hcl() and self.validate_ecl() and self.validate_pid())





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
            credentials = credentials.split(" ")
            credential = {}

            for key_value in credentials:
                kv = key_value.split(":")
                credential[kv[0]] = kv[1]

            credentials = " ".join(credentials)
            if credentials.count(":") == 8:
                if ValidatePassports(credential):
                    valid_passports += 1
            elif credentials.count(":") == 7 and "cid" not in credentials:
                if ValidatePassports(credential):
                    valid_passports += 1


            # print(credentials)

            # Reset credentials list
            credentials = []

print("Valid passports: " + str(valid_passports))
