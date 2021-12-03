import json

with open("test.txt", "r", encoding='utf-8', newline="") as f:
    lines = []

    # Get the most common for each index and store it
    for line in f.readlines():
        line = line.strip("\r\n")

        lines.append(line)

# while len(lines) != 1:
index = 1

# Need to keep an unmodified copy of the file for CO2 step
lines2 = lines

for index in range(len(lines[0])):
    ones = 0
    zeroes = 0

    remove_indexes = []

    for line in lines:
        for line_2 in lines:
                if int(line_2[index]) == 1:
                    ones += 1

                elif int(line_2[index]) == 0:
                    zeroes += 1

        # print(str("Ones: {}, Zeroes: {}").format(ones, zeroes))
        if zeroes > ones:
            most_common = 0

        elif zeroes < ones:
            most_common = 1

        elif zeroes == ones:

            print("\nNumbers are equal!")
            print(zeroes, ones)
            print(str(lines) + "\n")
            most_common = 1

        # print("Most common: " + str(most_common))
        # print("Index: " + str(index

        if int(line[index]) != most_common:
            print(str("Removing line: {}, most_common {} not found at index {}").format(line, most_common, index))
            remove_indexes.append(lines.index(line))

    # Reverse list to not mess with indexes
    print("\nBefore: " + str(lines))
    for indexes in sorted(remove_indexes, reverse=True):
        # print(remove_indexes)
        lines.pop(indexes)

    print("After: " + str(lines) + "\n")

    if len(lines) == 1:
        oxygen_generator_rating = int(lines[0], 2)
        break

print("\n\n\nFinding CO2 stuff\n\n\n")

# Variable list2 value was updated off of old deleted list, leaving previous answer only...
# Have to get it again...
with open("test.txt", "r", encoding='utf-8', newline="") as f:
    lines2 = []

    # Get the most common for each index and store it
    for line in f.readlines():
        line = line.strip("\r\n")

        lines2.append(line)

# Find CO2 Scrubber
for index in range(len(lines2[0])):
    ones = 0
    zeroes = 0

    remove_indexes = []

    for line in lines2:
        for line_2 in lines2:
                if int(line_2[index]) == 1:
                    ones += 1

                elif int(line_2[index]) == 0:
                    zeroes += 1

        # print(str("Ones: {}, Zeroes: {}").format(ones, zeroes))
        if zeroes > ones:
            least_common = 1

        elif zeroes < ones:
            least_common = 0

        elif zeroes == ones:

            print("\nNumbers are equal!")
            print(str(lines) + "\n")
            least_common = 0

        # print("Most common: " + str(most_common))
        # print("Index: " + str(index

        if int(line[index]) != least_common:
            print(str("Removing line: {}, least common {} not found at index {}").format(line, least_common, index))
            remove_indexes.append(lines2.index(line))

    # Reverse list to not mess with indexes
    print("\nBefore: " + str(lines2))
    for indexes in sorted(remove_indexes, reverse=True):
        # print(remove_indexes)
        lines2.pop(indexes)

    print("After: " + str(lines2) + "\n")

    if len(lines2) == 1:
        co2_scrubber_rating = int(lines2[0], 2)
        break


print(str("Oxygen Generator Rating: {}, C02 Scrubber Rating: {}").format(oxygen_generator_rating, co2_scrubber_rating))
print(str("Life Support Rating: {}").format(oxygen_generator_rating * co2_scrubber_rating))

# # Most common
# gamma_rate = []
#
# # Least common
# epsilon_rate = []

#
# for dict in number_stats:
#     if int(number_stats[dict]["0"]) > int(number_stats[dict]["1"]):
#         gamma_rate.append("0")
#         epsilon_rate.append("1")
#
#     elif int(number_stats[dict]["0"]) < int(number_stats[dict]["1"]):
#         gamma_rate.append("1")
#         epsilon_rate.append("0")
#
#
#
# gamma_decimal = int(''.join(gamma_rate), 2)
# epsilon_decimal = int(''.join(epsilon_rate), 2)
# print(json.dumps(number_stats, indent=4))
# print(str("\nGamma rate: {}\nEpsilon rate: {}\nMultiplied: {}").format(gamma_decimal, epsilon_decimal, gamma_decimal * epsilon_decimal))
