import json

with open("input.txt", "r", encoding='utf-8', newline="") as f:
    number_stats = {

    }
    # Initialize nested dictionaries and keys
    for i in range(len(f.readline())):
        number_stats[i] = {"0":0, "1":0}

    f.seek(0)
    # Get the most common for each index and store it
    for line in f.readlines():
        for i in range(len(line)):
            if "1" in line[i]:
                number_stats[i]["1"] += 1

            elif line[i] == "0":
                number_stats[i]["0"] += 1
# Most common
gamma_rate = []

# Least common
epsilon_rate = []

for dict in number_stats:
    if int(number_stats[dict]["0"]) > int(number_stats[dict]["1"]):
        gamma_rate.append("0")
        epsilon_rate.append("1")

    elif int(number_stats[dict]["0"]) < int(number_stats[dict]["1"]):
        gamma_rate.append("1")
        epsilon_rate.append("0")

gamma_decimal = int(''.join(gamma_rate), 2)
epsilon_decimal = int(''.join(epsilon_rate), 2)
print(json.dumps(number_stats, indent=4))
print(str("\nGamma rate: {}\nEpsilon rate: {}\nMultiplied: {}").format(gamma_decimal, epsilon_decimal, gamma_decimal * epsilon_decimal))
