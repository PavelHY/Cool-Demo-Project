shipment_kg = float(input())
command = input()
distance = int(input())
money = 0

if command == "standard":
    if 0 <= shipment_kg <= 1:
        money = distance * 0.03
    elif 1 <= shipment_kg <= 10:
        money = distance * 0.05
    elif 10 <= shipment_kg <= 40:
        money = distance * 0.10
    elif 40 <= shipment_kg <= 90:
        money = distance * 0.15
    elif 90 <= shipment_kg <= 150:
        money = distance * 0.20
else:
    if 0 <= shipment_kg < 1:
        money = distance * 0.03 + ((0.03 * 0.80 * shipment_kg) * distance)

    elif 1 <= shipment_kg <= 10:
        money = distance * 0.05 + ((0.05 * 0.40 * shipment_kg) * distance)
    elif 10 <= shipment_kg <= 40:
        money = distance * 0.10 + ((0.10 * 0.05 * shipment_kg) * distance)
    elif 40 <= shipment_kg <= 90:
        money = distance * 0.15 + ((0.15 * 0.02 * shipment_kg) * distance)
    elif 90 <= shipment_kg <= 150:
        money = distance * 0.20 + ((0.20 * 0.01 * shipment_kg) * distance)

print(f"The delivery of your shipment with weight of {shipment_kg:.3f} kg. would cost {money:.2f} lv.")