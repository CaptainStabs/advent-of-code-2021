with open("input.txt", "r", newline="\r\n", encoding="utf-8") as f:
    total = 0
    for line in f.readlines():
        line = line.split(" ")

        min_num = int(line[0].split("-")[0])
        max_num = int(line[0].split("-")[1])

        letter = line[1].rstrip(":")

        password = line[2]

        occurrences = password.count(letter)

        if occurrences <= max_num and occurrences >= min_num:
            total += 1

    print(total)
