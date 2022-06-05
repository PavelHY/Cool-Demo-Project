budget = float(input())
extras_nim = int(input())
clothing_price = float(input())

total_price = 0
decor = budget * 0.10

if extras_nim >= 150:
    clothing_price = clothing_price - clothing_price * 0.10

clothing_for_all = clothing_price * extras_nim
total_price = clothing_for_all + decor

if total_price > budget:
    print('Not enough money!')
    print(f"Wingard needs {total_price - budget:.2f} leva more.")

else:
    print("Action!")
    print(f"Wingard starts filming with {budget - total_price:.2f} leva left.")

