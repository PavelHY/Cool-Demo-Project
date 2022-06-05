drink = input()
sugar = input()
num_drinks = int(input())

price = 0

if drink == "Espresso":
    if sugar == "Without":
        espresso = 0.90 * num_drinks
        price = espresso - espresso * 0.35
    elif sugar == "Normal":
        price = 1 * num_drinks
    elif sugar == "Extra":
        price = 1.20 * num_drinks
    if num_drinks >= 5:
        price = price - price * 0.25

elif drink == "Cappuccino":
    if sugar == "Without":
        cappuccino = 1 * num_drinks
        price = cappuccino - cappuccino * 0.35
    elif sugar == "Normal":
        price = 1.20 * num_drinks
    elif sugar == "Extra":
        price = 1.60 * num_drinks

elif drink == "Tea":
    if sugar == "Without":
        tea = 0.50 * num_drinks
        price = tea - tea * 0.35
    elif sugar == "Normal":
        price = 0.60 * num_drinks
    elif sugar == "Extra":
        price = 0.70 * num_drinks

if price > 15:
    price = price - price * 0.20

print(f"You bought {num_drinks} cups of {drink} for {price:.2f} lv.")