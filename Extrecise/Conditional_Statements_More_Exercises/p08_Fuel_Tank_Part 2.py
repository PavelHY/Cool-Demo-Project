fuel = input()
volume_fuel = float(input())
club_card = input()

money = 0

if fuel == "Gas":
    if club_card == "Yes":
        money = volume_fuel * (0.93 - 0.08)
    else:
        money = volume_fuel * 0.93

elif fuel == "Gasoline":
    if club_card == "Yes":
        money = volume_fuel * (2.22 - 0.12)
    else:
        money = volume_fuel * 2.22

elif fuel == "Diesel":
    if club_card == "Yes":
        money = volume_fuel * (2.33 - 0.08)
    else:
        money = volume_fuel * 2.33
if 20 <= volume_fuel <= 25:
    print(f"{money - (money * 0.08):.2f} lv.")
elif volume_fuel > 25:
    print(f"{money - (money * 0.10):.2f} lv.")
else:
    print(f"{money:.2f} lv.")
    