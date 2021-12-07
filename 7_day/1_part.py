with open("input.txt", "r", newline="", encoding="utf-8") as f:
    line = f.read().strip("\r\n")
    positions = sorted([int(i) for i in line.split(",")])
    # print(positions)

    p = len(positions)
    print(p)

    m1 = positions[p//2]
    m2 = positions[p//2-1]
    m = m1 + m2 // 2
    m -= 1
    print(m)

    fuel_spent = 0
    for i in range(len(positions)):
        if positions[i] == m:
            continue
        else:
            if positions[i] > m:
                fuel_spent += positions[i] - m
                # print(str("- Move from {} to {}: {} fuel").format(positions[i], m, positions[i] - m))
            else:
                fuel_spent += m - positions[i]
                # print(str("- Move from {} to {}: {} fuel").format(positions[i], m, m - positions[i]))

    print("\nTotal fuel spent:", fuel_spent)
