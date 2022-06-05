import math

record = float(input())
meters = float(input())
time_per_1meters = float(input())

distance = meters * time_per_1meters
extra_time = float(math.floor(meters / 15) * 12.5)

total_time = (distance + extra_time)

if total_time >= record:
    print(f"No, he failed! He was {total_time - record:.2f} seconds slower.")
elif record > total_time:
    print(f" Yes, he succeeded! The new world record is {total_time:.2f} seconds.")