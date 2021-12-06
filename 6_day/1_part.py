from tqdm import tqdm

def calculate_fish(days):
    with open("input.txt", "r", newline="", encoding="utf-8") as f:
        line = f.readline()
        fish_list = line.split(",")

        for day in tqdm(range(days)):
            for i in range(len(fish_list)):
                if fish_list[i] == 0:
                    fish_list[i] = 6
                    fish_list.append(8)
                else:
                    # Couldn't decrement here
                    fish_list[i] = int(fish_list[i]) - 1
            # print(str("After  {} day:  {}").format(day, fish_list))

        print("Total fish: " + str(len(fish_list)))

calculate_fish(80)
# Will never finish
calculate_fish(256)
