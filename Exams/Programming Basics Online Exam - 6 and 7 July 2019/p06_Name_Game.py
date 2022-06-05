import sys

max_points = -sys.maxsize
winner_name_1 = ""

name = input()

while name != "Stop":
    winner_points_1 = 0
    # winner_points_2 = 0
    for letter in name:
        number = int(input())
        if number == ord(letter):
            winner_points_1 += 10
        else:
            winner_points_1 += 2
        if winner_points_1 >= max_points:
            max_points = winner_points_1
            winner_name_1 = name
    name = input()
print(f"The winner is {winner_name_1} with {max_points} points!")