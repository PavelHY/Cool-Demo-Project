player_name = input()

points = 301
successful_shots = 0
unsuccessful_shots = 0

command = input()
while command != "Retire":
    current_points = int(input())
    successful_shots += 1
    if command == "Double":
        current_points = 2 * current_points
    elif command == "Triple":
        current_points = 3 * current_points

    if current_points > points:
        unsuccessful_shots += 1
        successful_shots -= 1
        command = input()
        continue
    elif current_points == points:
        print(f"{player_name} won the leg with {successful_shots} shots.")
        break

    if command == "Single":
        points -= current_points
    elif command == "Double":
        points -= current_points
    elif command == "Triple":
        points -= current_points
    command = input()
if command == "Retire":
    print(f"{player_name} retired after {unsuccessful_shots} unsuccessful shots.")

