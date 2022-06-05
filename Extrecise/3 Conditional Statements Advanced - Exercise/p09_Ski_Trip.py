day = int(input()) - 1
rent_tape = input()
rate = input()

price = 0

if rent_tape == "room for one person":
    price = day * 18.00

elif rent_tape == "apartment":
    price = day * 25.00
    if day < 10:
        price = price - price * 0.30
    elif 10 <= day <= 15:
        price = price - price * 0.35
    else:
        price = price - price * 0.50
elif rent_tape == "president apartment":
    price = day * 35.00
    if day < 10:
        price = price - price * 0.10
    elif 10 <= day <= 15:
        price = price - price * 0.15
    else:
        price = price - price * 0.20

if rate == "positive":
    price = price + price * 0.25
else:
    price = price - price * 0.10

print(f"{price:.2f}")
