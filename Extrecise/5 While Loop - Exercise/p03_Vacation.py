trip_cost = float(input())
cash_available = float(input())

days_spend_money = 0
days_cnt = 0

while cash_available < trip_cost and days_spend_money < 5:
    type_of_action = input()
    money = float(input())
    days_cnt += 1

    if type_of_action == "spend":
        cash_available -= money
        days_spend_money += 1
        if cash_available < 0:
            cash_available = 0

    elif type_of_action == "save":
        cash_available += money
        days_spend_money = 0

if days_spend_money == 5:
    print("You can't save the money.")
    print(days_cnt)

if cash_available >= trip_cost:
    print(f"You saved the money for {days_cnt} days.")
