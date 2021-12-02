
with open("input.txt", "r", encoding="utf-8", newline="") as f:
    horizontal_position = 0
    depth = 0

    for line in f.readlines():
        if "forward" in line:
            horizontal_position += int(line.split(" ")[1])

        if "down" in line:
            depth += int(line.split(" ")[1])

        if "up" in line:
            depth -= int(line.split(" ")[1])

print(str("Horizontal position: {hp}, Depth: {depth}").format(hp = horizontal_position, depth= depth))
print(str("Multiplied: {}").format(horizontal_position * depth))
