days = int(input())

money_win = 0
total_win = 0
total_losses = 0

for _ in range(1, days + 1):
    command = input()
    daily_money = 0
    days_win = 0
    days_lose = 0

    while command != "Finish":
        result = input()
        if result == "win":
            daily_money += 20
            days_win += 1

        elif result == "lose":
            #total_losses += 1
            days_lose += 1

        command = input()

    if days_win > days_lose:
        daily_money *= 1.10
        total_win += 1
    else:
        total_losses += 1
    money_win += daily_money

if total_win > total_losses:
    money_win *= 1.20
    print(f"You won the tournament! Total raised money: {money_win:.2f}")
else:
    print(f"You lost the tournament! Total raised money: {money_win:.2f}")
