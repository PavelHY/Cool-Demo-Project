import math
day_off = float(input())
target_time_for_play = 30000

working_days = 365 - day_off

time_for_play = working_days * 63 + day_off * 127

difference = abs(target_time_for_play - time_for_play)
hour = difference // 60
minutes = difference % 60

if target_time_for_play >= time_for_play:
    print("Tom sleeps well")
    print(f'{round(hour)} hours and {round(minutes)} minutes less for play')
else:
    print('Tom will run away')
    print(f'{round(hour)} hours and {round(minutes)} minutes more for play')
