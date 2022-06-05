import math

magnolias_num = int(input()) * 3.25
hyacinths_num = int(input()) * 4
roses_num = int(input()) * 3.50
cacti_num = int(input()) * 8
gift_price = float(input())

price = magnolias_num + hyacinths_num + roses_num + cacti_num
total_price = price - price * 0.05

if total_price >= gift_price:
    print(f"She is left with {math.floor(total_price - gift_price)} leva.")
else:
    print(f"She will have to borrow {math.ceil(gift_price - total_price)} leva.")
