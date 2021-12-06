with open("example.txt", "r", newline="", encoding="utf-8") as f:
    for i, line in enumerate(f.readlines()):
        if i == 0:
            winning_numbers = line.split(",")

        if line == "\n":
            continue

        
