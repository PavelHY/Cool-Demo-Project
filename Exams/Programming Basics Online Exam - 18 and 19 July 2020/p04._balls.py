import math

n = int(input())

total_points = 0
red_balls = 0
orange_balls = 0
yellow_balls = 0
white_balls = 0
other_colors_balls = 0
divider_from_black_balls = 0

for _ in range(1, n + 1):
    ball_colors = input()

    if ball_colors == "red":
        red_balls += 1
        total_points += 5
    elif ball_colors == "orange":
        orange_balls += 1
        total_points += 10
    elif ball_colors == "yellow":
        yellow_balls += 1
        total_points += 15
    elif ball_colors == "white":
        white_balls += 1
        total_points += 20
    elif ball_colors == "black":
        divider_from_black_balls += 1
        total_points = math.floor(total_points / 2)
    else:
        other_colors_balls += 1

print(f"Total points: {total_points}")
print(f"Red balls: {red_balls}")
print(f"Orange balls: {orange_balls}")
print(f"Yellow balls: {yellow_balls}")
print(f"White balls: {white_balls}")
print(f"Other colors picked: {other_colors_balls}")
print(f"Divides from black balls: {divider_from_black_balls}")
