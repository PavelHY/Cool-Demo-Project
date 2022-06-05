nylon = float(input())
dye = float(input())
thinner = float(input())
hour_needed = float(input())

nylon =(nylon + 2) * 1.50  # 18
dye = (dye + (dye * 0.10)) * 14.50   # 175.45
thinner = thinner * 5.00   # 20.00

sum_materials = nylon + dye + thinner + 0.40
builders_money_needed = (sum_materials * 0.30) * hour_needed
total_price = sum_materials + builders_money_needed

print(f"{total_price}")