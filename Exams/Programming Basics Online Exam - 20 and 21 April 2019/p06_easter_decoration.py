customers = int(input())
total_money = 0

for _ in range(customers):
    type_of_purchase = input()
    counter = 0
    money = 0
    while type_of_purchase != "Finish":
        if type_of_purchase == "basket":
            money += 1.50
            counter += 1
        elif type_of_purchase == "wreath":
            money += 3.80
            counter += 1
        elif type_of_purchase == "chocolate bunny":
            money += 7
            counter += 1

        type_of_purchase = input()
    if counter % 2 == 0:
        money = money - money * 0.20
    total_money += money
    print(f"You purchased {counter} items for {money:.2f} leva.")
average = total_money / customers
print(f"Average bill per client is: {average:.2f} leva.")

