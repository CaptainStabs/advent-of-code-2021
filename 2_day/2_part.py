with open("input.txt", "r", encoding="utf-8", newline="") as f:
    horizontal_position = 0
    depth = 0
    aim = 0

    for line in f.readlines():
        if "forward" in line:
            forward_amount = int(line.split(" ")[1])
            horizontal_position += forward_amount

            if aim != 0:
                depth += forward_amount * aim

        if "down" in line:
            aim += int(line.split(" ")[1])

        if "up" in line:
            aim -= int(line.split(" ")[1])

print(str("Horizontal position: {hp}, Depth: {depth}").format(hp = horizontal_position, depth= depth))
print(str("Multiplied: {}").format(horizontal_position * depth))
