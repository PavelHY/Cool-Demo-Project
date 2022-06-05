food = int(input()) * 1000

food_cnt = 0

command = input()
while command != "Adopted":
    food_eaten = int(command)
    food_cnt += food_eaten
    command = input()

if food_cnt <= food:
    print(f"Food is enough! Leftovers: {food - food_cnt} grams.")
else:
    print(f"Food is not enough. You need {food_cnt - food} grams more.")
