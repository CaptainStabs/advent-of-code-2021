with open("input.txt", "r", newline="\r\n", encoding="utf-8") as f:
    total = 0
    valid_passwords = 0
    for line in f.readlines():
        line = line.rstrip("\r\n").split(" ")

        min_num = int(line[0].split("-")[0]) - 1
        max_num = int(line[0].split("-")[1]) - 1


        letter = line[1].rstrip(":")

        password = line[2]

        occurrences = password.count(letter)

        # valid_passwords = 0
        min_letter = False
        max_letter = False

        if password[min_num] == letter:
            min_letter = True

        if password[max_num] == letter:
            max_letter = True

        if max_letter and min_letter:
            print("Invalid password: " + str(line))
            continue

        elif password[min_num] != letter and password[max_num] != letter:
            print("Invalid password: " + str(line))
            continue
        else:
            valid_passwords += 1
            print("Valid password: " + str(line))

    print(valid_passwords)
