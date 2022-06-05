lily_age = int(input())
washer_price = float(input())
single_toy_price = int(input())

total_cnt = 0
total_money_saved = 0

for current_age in range(1, lily_age + 1):
    if current_age % 2 != 0:
        total_cnt +=1
    else:
        money_given = (current_age * 5) - 1
        total_money_saved += money_given

toys_money = total_cnt * single_toy_price
total_money_saved +=toys_money

if total_money_saved >= washer_price:
    print(f"Yes! {total_money_saved - washer_price:.2f}")
else:
    print(f"No! {washer_price - total_money_saved:.2f}")

