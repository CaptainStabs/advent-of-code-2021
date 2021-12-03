with open("input.txt", "r", encoding='utf-8', newline="") as f:
    line_list = []
    for line in f.readlines():
        line_list.append(line.rstrip("\r\n"))

    # print(line_list[1])
    # print(line_list[2:])

    for i, number in enumerate(line_list):
        # Current number is in position x
        i += 1

        for j, second_number in enumerate(line_list[i:]):
            # print(f"{int(number) * int(second_number)}")
            j += 1

            for third_number in line_list[j:]:
                if int(number) + int(second_number) + int(third_number) == 2020:
                    print(str("{} + {} + {} = {}").format(number, second_number, third_number, int(number) + int(second_number) + int(third_number)))
                    print(str("{} * {} * {} = {}").format(number, second_number, third_number, int(number) * int(second_number) * int(third_number)))
