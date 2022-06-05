egg = int(input())
sold_egg = 0
is_no_egg = False
command = input()
while command != "Close":
    egg_num = int(input())
    if egg >= 0:
        if command == "Fill":
            egg += egg_num
        if egg >= egg_num:
            if command == "Buy":
                egg -= egg_num
                sold_egg += egg_num
        else:
            is_no_egg = True
            break
    command = input()
if is_no_egg:
    print("Not enough eggs in store!")
    print(f"You can buy only {egg}.")
else:
    print("Store is closed!")
    print(f"{sold_egg} eggs sold.")
