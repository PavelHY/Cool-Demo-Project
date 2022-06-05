import math

serial = input()
time_for_1episode = float(input())
rest_time = float(input())

lunch_time = rest_time * 0.125
rest = rest_time * 0.25

left_time = rest_time - lunch_time - rest

if left_time >= time_for_1episode:
    print(f"You have enough time to watch {serial} and left with "
          f"{math.ceil(left_time - time_for_1episode)} minutes free time.")
else:
    print(f"You don't have enough time to watch {serial}, you need "
          f"{math.ceil(time_for_1episode - left_time)} more minutes.")
