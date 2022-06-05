windows_num = int(input())
tape_win = input()
delivery = input()

price = 0

if tape_win == "90X130":
    price = windows_num * 110
    if 60 >= windows_num > 30:
        price = price - price * 0.05
    elif windows_num > 60:
        price = price - price * 0.08

elif tape_win == "100X150":
    price = windows_num * 140
    if 80 >= windows_num > 40:
        price = price - price * 0.06
    elif windows_num > 60:
        price = price - price * 0.10

elif tape_win == "130X180":
    price = windows_num * 190
    if 50 >= windows_num > 20:
        price = price - price * 0.07
    elif windows_num > 50:
        price = price - price * 0.12

elif tape_win == "200X300":
    price = windows_num * 250
    if 50 >= windows_num > 25:
        price = price - price * 0.09
    elif windows_num > 50:
        price = price - price * 0.14

if delivery == "With delivery":
    price += 60

if windows_num > 99:
    price = price - price * 0.04

if windows_num < 10:
    print("Invalid order")
else:
    print(f"{price:.2f} BGN")
