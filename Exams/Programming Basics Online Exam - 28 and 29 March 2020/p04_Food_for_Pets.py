import math
days = int(input())
total_food = float(input())

cookies_percent = 0
dog_food_cnt = 0
cat_food_cnt = 0

for i in range(1, days + 1):
    dog_food = int(input())
    cat_food = int(input())

    dog_food_cnt += dog_food
    cat_food_cnt += cat_food

    if i % 3 == 0:
        cookies_percent += (dog_food + cat_food) * 0.10

food_eaten_together = cat_food_cnt + dog_food_cnt

print(f"Total eaten biscuits: {round(cookies_percent)}gr.")
print(f"{(food_eaten_together / total_food) * 100:.2f}% of the food has been eaten.")
print(f"{dog_food_cnt / food_eaten_together * 100:.2f}% eaten from the dog.")
print(f"{cat_food_cnt / food_eaten_together * 100:.2f}% eaten from the cat.")
