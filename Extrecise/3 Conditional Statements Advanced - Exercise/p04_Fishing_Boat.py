budget = int(input())
season = input()
fishman = int(input())

price = 0

if season == "Spring":
    price = 3000
elif season == "Summer" or season == "Autumn":
    price = 4200
elif season == "Winter":
    price = 2600

if fishman <= 6:
    price = price - price * 0.1
elif 7 <= fishman <= 11:
    price = price - price * 0.15
elif fishman >= 12:
    price = price - price * 0.25

if fishman % 2 == 0 and season != "Autumn":
    price = price -  price * 0.05

if budget >= price:
    print(f"Yes! You have {budget - price:.2f} leva left.")
elif budget < price:
    print(f"Not enough money! You need {price - budget:.2f} leva.")
