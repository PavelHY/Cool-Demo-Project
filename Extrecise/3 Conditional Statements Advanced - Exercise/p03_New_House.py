flower = input()
num_per_flower = int(input())
budget = int(input())

price = 0

if flower == "Roses":
    price = num_per_flower * 5
    if num_per_flower > 80:
        price = price - price * 0.10
elif flower == "Dahlias":
    price = num_per_flower * 3.80
    if num_per_flower > 90:
        price = price - price * 0.15
elif flower == "Tulips":
    price = num_per_flower * 2.80
    if num_per_flower > 80:
        price = price - price * 0.15
elif flower == "Narcissus":
    price = num_per_flower * 3
    if num_per_flower < 120:
        price = price + price * 0.15
elif flower == "Gladiolus":
    price = num_per_flower * 2.50
    if num_per_flower < 80:
        price = price + price * 0.20

if budget >= price:
    print(f"Hey, you have a great garden with {num_per_flower} {flower}"
          f" and {budget - price:.2f} leva left.")
elif price > budget:
    print(f"Not enough money, you need {price - budget:.2f} leva more.")
