chicken = float(input()) * 10.35
fish = float(input()) * 12.40
vegetarian_meal = float(input()) * 8.15
delivery = 2.50

order_price = chicken + fish + vegetarian_meal
dessert = order_price * 0.20

total_price = order_price + delivery + dessert

print(f"{total_price}")