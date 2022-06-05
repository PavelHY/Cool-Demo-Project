player_one = input()
player_two = input()

points_player_one = 0
points_player_two = 0
command = input()
while command != "End of game":
    player_one_card = int(command)
    player_two_card = int(input())
    if player_one_card == player_two_card:
        print("Number wars!")
        player_one_card = int(input())
        player_two_card = int(input())
        if player_one_card > player_two_card:
            print(f"{player_one} is winner with {points_player_one} points")
        else:
            print(f"{player_two} is winner with {points_player_two} points")
        break
    if player_one_card > player_two_card:
        points_player_one += player_one_card - player_two_card
    elif player_two_card > player_one_card:
        points_player_two += player_two_card - player_one_card
    command = input()
if command == "End of game":
    print(f"{player_one} has {points_player_one} points")
    print(f"{player_two} has {points_player_two} points")
