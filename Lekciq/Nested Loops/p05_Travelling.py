destination = input()

while destination != "End":
    budget = float(input())
    money = 0
    while budget > money:
        earned_money = float(input())
        money += earned_money
        if money < 0:
            break

    print(f"Going to {destination}!")

    destination = input()

