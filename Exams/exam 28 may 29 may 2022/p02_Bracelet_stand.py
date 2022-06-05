money_per_day = float(input()) * 5
own_money_per_day = float(input()) * 5
cost = float(input())
present_cost = float(input())

total_money = (money_per_day + own_money_per_day) - cost

if total_money >= present_cost:
    print(f"Profit: {total_money:.2f} BGN, the gift has been purchased.")
else:
    print(f"Insufficient money: {present_cost - total_money:.2f} BGN.")

