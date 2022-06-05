km = int(input())
day_time = input()

money_box: int = 0

if 0 < km < 20:
    if day_time == "day":
        money_box = 0.70 + 0.79 * km
    elif day_time == "night":
        money_box = 0.7 + 0.90 * km

elif 20 >= km < 100:
    money_box = 0.09 * km

elif km >= 100:
    money_box = 0.06 * km

print(f'{money_box:.2f}')
