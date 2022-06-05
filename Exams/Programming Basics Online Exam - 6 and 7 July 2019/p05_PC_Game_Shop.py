game_sold = int(input())

hearthstone = 0
fornite = 0
overwatch = 0
others = 0

for _ in range(1, game_sold + 1):
    game = input()

    if game == 'Hearthstone':
        hearthstone += 1
    elif game == 'Fornite':
        fornite += 1
    elif game == 'Overwatch':
        overwatch += 1
    else:
        others += 1

print(f"Hearthstone - {hearthstone / game_sold * 100:.2f}%")
print(f"Fornite - {fornite / game_sold * 100:.2f}%")
print(f"Overwatch - {overwatch / game_sold * 100:.2f}%")
print(f"Others - {others / game_sold * 100:.2f}%")
