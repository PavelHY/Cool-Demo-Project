import math

tournaments = int(input())
start_points = int(input())

points = 0
w = 0
sf = 0
f = 0

for i in range(1, tournaments+1):
    stage_of_the_tournament = input()

    if stage_of_the_tournament == "W":
        points += 2000
        w += 1
    elif stage_of_the_tournament == "F":
        points += 1200
        f += 1
    elif stage_of_the_tournament == "SF":
        points += 720

total_points = points + start_points
average_points = points / tournaments
percentage_wins = w / tournaments * 100

print(f"Final points: {math.floor(total_points)}")
print(f"Average points: {math.floor(average_points)}")
print(f"{percentage_wins:.2f}%")
