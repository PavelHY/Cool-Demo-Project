import math
hours = int(input())
minutes = int(input()) + 15

total_time = hours * 60 + minutes
new_hours = total_time / 60
new_minutes = total_time % 60
new_hours = math.floor(new_hours)


if new_hours > 23:
    new_hours = 0

hours = 0

if new_minutes > 59:
    new_minutes -= 60
    new_hours +=1


print(f'{new_hours}:{new_minutes:02d}')
