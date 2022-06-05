deposit_sum = float(input())
months = int(input())
annual_percent = float(input()) /100

month_gain = (deposit_sum * annual_percent) / 12
final_sum = deposit_sum + (months * month_gain)

print(final_sum)