hall_price = int(input())

cake = hall_price * 0.20
drinks = cake - cake * 0.45
animator = hall_price / 3

total_money_needed = hall_price + cake + drinks + animator

print(total_money_needed)
