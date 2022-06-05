pen_price = float(input())
markers_price = float(input())
cleaning_chemical_price = float(input())
percentage_discount = float(input()) / 100

pen_price = pen_price * 5.80
markers_price = markers_price * 7.20
cleaning_chemical_price = cleaning_chemical_price * 1.20

total_price = pen_price + markers_price + cleaning_chemical_price
price_discount = total_price - (total_price * percentage_discount)
print(price_discount)