import math

tournaments = int(input())
won_points = int(input())

new_points = 0
tournaments_win = 0

for _ in range(tournaments):
    stage_of_the_tournament = input()
    if stage_of_the_tournament == "W":
        new_points += 2000
        tournaments_win += 1
    elif stage_of_the_tournament == "F":
        new_points += 1200
    elif stage_of_the_tournament == "SF":
        new_points += 720

final_points = won_points + new_points
print(f"Final points: {final_points}")

average_points = math.floor(new_points / tournaments)
print(f"Average points: {average_points}")

percent_of_win_tournaments = tournaments_win / tournaments * 100
print(f"{percent_of_win_tournaments:.2f}%")
