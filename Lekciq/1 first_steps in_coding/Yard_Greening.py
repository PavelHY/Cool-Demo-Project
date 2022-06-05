metr_kv = float(input())

price_for_garden = metr_kv * 7.61

disccount_price = price_for_garden * 0.18
total_price = price_for_garden - disccount_price

print(f"The final price is: {total_price} lv.")
print(f"The discount is: {disccount_price} lv.")