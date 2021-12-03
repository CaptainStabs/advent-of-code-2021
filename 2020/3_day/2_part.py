import json

slopes = {
    0:{
        "x":1,
        "y":1,
    },
    1:{
        "x":3,
        "y":1

    },
    2:{
        "x":5,
        "y":1,

    },
    3:{
        "x":7,
        "y":1

    },
    4:{
        "x":1,
        "y":2
    }
}

with open("input.txt", "r", newline="", encoding="utf-8") as f:

    increase_by = 1
    tree_totals = []
    lines = []

    for line in f.readlines():
        lines.append(line.strip("\r\n"))


    for slope in slopes:
        start = 0
        print(slopes[slope])
        number_trees = 0
        # Y coordinate of 1
        for index in range(0, len(lines), slopes[slope]["y"]):
            line = lines[index]
            for index in range(increase_by + 7):
                line = line + line

            position = line[start]

            # Check if tree (#) at index
            if position == "#":
                number_trees += 1
            #     print(line[:start] + "X" + line[start+1:])
            #
            # else:
            #     print(line[:start] + "O" + line[start+1:])


            # X Coordinate increments by slope x
            start += int(slopes[slope]["x"])

            if index > 10:
                increase_by += 1


        slopes[slope]["number_trees"] = number_trees
        print("Number of trees: " + str(slopes[slope]["number_trees"]))
        tree_totals.append(number_trees)

print("Number of trees: " + str(tree_totals))
print(json.dumps(slopes, indent=4))

answer = slopes[0]["number_trees"] * slopes[1]["number_trees"] * slopes[2]["number_trees"] * slopes[3]["number_trees"] * slopes[4]["number_trees"]
print("Answer: " + str(answer))

answer = 0
for slope in slopes:
    if slope > 1:
        answer = answer * previous_slope
    elif slope == 1:
        answer = slope * previous_slope

    previous_slope = slopes[slope]["number_trees"]


print(answer)
