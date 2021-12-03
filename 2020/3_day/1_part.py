with open("input.txt", "r", newline="", encoding="utf-8") as f:
    start = 0
    number_trees = 0
    increase_by = 1

     # Y coordinate of 1
    for index, line in enumerate(f.readlines()):
        for index in range(increase_by + 5):
            line = line.strip("\r\n")
            line = line + line


        position = line[start]

        # Check if tree (#) at index
        if position == "#":
            number_trees += 1
            print(line[:start] + "X" + line[start+1:])

        else:
            print(line[:start] + "O" + line[start+1:])



        # X Coordinate increments by 3
        start += 3
        if index > 10:
            increase_by += 1

print("Number of trees: " + str(number_trees))
