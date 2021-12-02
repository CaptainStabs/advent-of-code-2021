with open("input.txt", "r", newline="\n", encoding="utf-8") as f:
    previous_number = 0
    total_greater_than = 0

    for line in f.readlines():
        if int(line) > int(previous_number):
            total_greater_than += 1

        previous_number = line

    # Remove one as the first number doesn't count.
    print(total_greater_than - 1)
