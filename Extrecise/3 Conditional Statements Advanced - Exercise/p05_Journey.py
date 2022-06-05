budget = float(input())
sumer_winter = input()

price = 0
destination = ""
rest_in: str = ""

if budget <= 100:
    destination = "Bulgaria"
    if sumer_winter == "summer":
        price = budget * 0.30
        rest_in = "Camp"
    else:
        price = budget * 0.70
        rest_in = "Hotel"
elif budget <= 1000:
    destination = "Balkans"
    if sumer_winter == "summer":
        price = budget * 0.40
        rest_in = "Camp"
    else:
        price = budget * 0.80
        rest_in = "Hotel"
elif budget > 1000:
    price = budget * 0.90
    destination = "Europe"
    rest_in = "Hotel"

print(f"Somewhere in {destination}")
print(f"{rest_in} - {price:.2f}")
