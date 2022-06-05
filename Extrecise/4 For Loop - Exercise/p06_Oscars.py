actor_name = input()
academy_points = float(input())
judge_num = int(input())

total_points = academy_points

for i in range(0, judge_num):
    judge_name = input()
    points_from_judge = float(input())

    total_points += ((len(judge_name) * points_from_judge) / 2)

    if total_points >= 1250.5:
        print(f"Congratulations, {actor_name} got a nominee for leading role with {total_points:.1f}!")
        break
if total_points < 1250.5:
    print(f"Sorry, {actor_name} you need {1250.5 - total_points:.1f} more!")
