luggage_bugger_20_kg = float(input())
luggage_kg = float(input())
days = int(input())
luggage_num = int(input())

price = 0

if luggage_kg < 10:
    price = luggage_bugger_20_kg * 0.20 * luggage_num

elif 10 <= luggage_kg <= 20:
    price = luggage_bugger_20_kg * 0.50 * luggage_num

elif luggage_kg > 20:
    price = luggage_bugger_20_kg * luggage_num

if days < 7:
    price *= 1.40
elif 7 <= days <= 30:
    price *= 1.15
elif days > 30:
    price *= 1.10

print(f"The total price of bags is: {price:.2f} lv. ")
