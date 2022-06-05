fat = int(input())
proteins = int(input())
carbohydrates = int(input())
calories = int(input())
percentage_H2O = int(input())

total_fat = ((fat / 100) * calories) / 9
total_proteins = ((proteins / 100) * calories) / 4
total_carbohydrates = ((carbohydrates / 100) * calories) / 4

food_wait = total_proteins + total_carbohydrates + total_fat
calories_for_one_gr = calories / food_wait
if percentage_H2O != 0:

    calories_per_gram = (100 - percentage_H2O) * calories_for_one_gr / 100

    print(f"{calories_per_gram:.4f}")