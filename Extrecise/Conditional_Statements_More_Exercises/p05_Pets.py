import math

days_gone = int(input())
food_for_pets_left = int(input())   # 10
dog_food = float(input())   # 1
cat_food = float(input())   # 1
turtle_food = float(input()) / 1000   # 1200

dog_food_needed = dog_food * days_gone
cat_food_needed = cat_food * days_gone
turtle_food_needed = turtle_food * days_gone

total_food = dog_food_needed + cat_food_needed + turtle_food_needed

if total_food <= food_for_pets_left:
    food_left = math.floor(food_for_pets_left - total_food)
    print(f"{food_left} kilos of food left.")

else:
    food_need = math.ceil(total_food - food_for_pets_left)
    print(f"{food_need} more kilos of food are needed.")
