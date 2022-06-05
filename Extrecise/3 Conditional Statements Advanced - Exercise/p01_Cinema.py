projection_type = input()
row = int(input())
columns = int(input())

income = 0

if projection_type == "Premiere":
    income = row * columns * 12.00

elif projection_type == "Normal":
    income = row * columns * 7.50

elif projection_type == "Discount":
    income = row * columns * 5.00

print(f"{income:.2f} leva")
