fuel = input()
tank_capacity = int(input())

if fuel == "Diesel":
    if tank_capacity >= 25:
        print(f"You have enough diesel.")
    else:
        print(f"Fill your tank with diesel!")
elif fuel == "Gasoline":
    if tank_capacity < 25:
        print(f"Fill your tank with gasoline!")
    else:
        print(f"You have enough gasoline.")
elif fuel == "Gas":
    if tank_capacity >= 25:
        print(f"You have enough gas.")
    else:
        print(f"Fill your tank with gas!")
else:
    print("Invalid fuel!")
