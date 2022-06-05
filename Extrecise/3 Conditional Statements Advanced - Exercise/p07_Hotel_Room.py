mount = input()
nights_num = float(input())

studio_price = 0
apartment_price = 0

if mount == "May" or mount == "October":
    studio_price = 50 * nights_num
    apartment_price = 65 * nights_num
    if 7 < nights_num <= 14:
        studio_price = studio_price - studio_price * 0.05
    elif nights_num > 14:
        apartment_price = apartment_price - apartment_price * 0.10
        studio_price = studio_price - studio_price * 0.30
elif mount == "June" or mount == "September":
    apartment_price = 68.70 * nights_num
    studio_price = 75.20 * nights_num
    if nights_num > 14:
        studio_price = studio_price - studio_price * 0.20
        apartment_price = apartment_price - apartment_price * 0.10

elif mount == "July" or mount == "August":
    apartment_price = 77 * nights_num
    studio_price = 76 * nights_num
    if nights_num > 14:
        apartment_price = apartment_price - apartment_price * 0.10

print(f"Apartment: {apartment_price:.2f} lv.")

print(f"Studio: {studio_price:.2f} lv.")
