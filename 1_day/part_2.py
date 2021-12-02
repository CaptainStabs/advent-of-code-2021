with open("input.txt", "r", newline="\r\n", encoding="utf-8") as f:
    num_list = []
    for line in f.readlines():
        num_list.append(line.rstrip("\r\n"))
    # num_list = ['a','b','c','d','e','f','g','h','i','j','k','l','m','o','p','q','r','s','t','u','v','w','x','y','z']
    size = 3
    step = 1
    slide_list = [num_list[x:x + size] for x in range(0, len(num_list) - size + 1, step)]

    totals = []
    for inner_list in slide_list:
        if len(inner_list) == 3:
            inner_list_total = 0
            for number in inner_list:
                inner_list_total += int(number)
            totals.append(inner_list_total)

    previous_total = 0
    total_greater_than = 0

    for total in totals:
        if total > previous_total:
            total_greater_than += 1

        previous_total = total # I forgot this

    print(total_greater_than - 1)
