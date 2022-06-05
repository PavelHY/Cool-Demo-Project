import sys

easter_cakes_num = int(input())

winner_points = -sys.maxsize
chef_name = ""

for _ in range(easter_cakes_num):
    chef = input()
    points = 0
    command = input()
    while command != "Stop":
        rating = int(command)
        points += rating
        command = input()

    print(f"{chef} has {points} points.")

    if points > winner_points:
        winner_points = points
        chef_name = chef
        print(f"{chef_name} is the new number 1!")
print(f"{chef_name} won competition with {winner_points} points!")
