budget = float(input())
statisticians = int(input())
clothing = float(input())

if statisticians > 150:
    clothing = clothing - (clothing * 0.10)

decor = budget * 0.10
price_clothing = clothing * statisticians
total_price = decor + price_clothing

if total_price > budget:
    print("Not enough money!")
    print(f"Wingard needs {total_price - budget:.2f} leva more.")
else:
    print("Action!" )
    print(f"Wingard starts filming with {budget - total_price:.2f} leva left.")