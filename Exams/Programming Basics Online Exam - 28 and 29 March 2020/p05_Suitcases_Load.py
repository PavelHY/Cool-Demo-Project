load_capacity = float(input())

suitcase_cht = 0

command = input()
while command != "End" or load_capacity <= 0:
    suitcase = float(command)
    suitcase_cht += 1
    if suitcase_cht % 3 == 0:
        suitcase *= 1.10

    load_capacity -= suitcase
    if load_capacity <= 0:
        suitcase_cht -= 1
        break
    command = input()

if command == "End":
    print("Congratulations! All suitcases are loaded!")

if load_capacity <= 0:
    print("No more space!")

print(f"Statistic: {suitcase_cht} suitcases loaded.")