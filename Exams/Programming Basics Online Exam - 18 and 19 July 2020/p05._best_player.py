best_score = 0
best_player = ""
player_name = input()
while player_name != "END":

    current_goals = int(input())

    if current_goals > best_score:
        best_score = current_goals
        best_player = player_name

    if current_goals >= 10:
        break
    player_name = input()
print(f"{best_player} is the best player!")
if current_goals >= 3:
    print(f"He has scored {best_score} goals and made a hat-trick !!!")

else:
    print(f"He has scored {best_score} goals.")