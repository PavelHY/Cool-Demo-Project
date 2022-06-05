sea = int(input())
mountain = int(input())

money = 0
sea_cnt = 0
mountain_cnt = 0

while True:
    command = input()
    if command == "Stop":
        break
    elif command == "sea":
        if sea == 0:
            continue
        else:
            money += 680
            sea -= 1
    elif command == "mountain":
        if mountain == 0:
            continue
        else:
            money += 499
            mountain -= 1
    if sea <= 0 and mountain <= 0:
        print("Good job! Everything is sold.")
        break


print(f"Profit: {money} leva.")


