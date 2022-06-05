football_team = input()
matches_num = int(input())

total_points = 0
W = 0
D = 0
L = 0

for _ in range(1, matches_num + 1):
    result = input()

    if result == "W":
        W += 1
        total_points += 3
    elif result == "D":
        D += 1
        total_points += 1
    elif result == "L":
        L += 1

if matches_num <= 0:
    print(f"{football_team} hasn't played any games during this season.")

else:
    print(f"{football_team} has won {total_points} points during this season.")
    print('Total stats:')
    print(f"## W: {W}")
    print(f"## D: {D}")
    print(f"## L: {L}")
    print(f"Win rate: {W / matches_num * 100:.2f}%")
