import sys

film_num = int(input())

smallest = sys.maxsize
biggest = -sys.maxsize
best_move = ""
worst_move = ""
rating_box = 0

for _ in range(1, film_num + 1):
    film_name = input()
    rating = float(input())
    rating_box += rating

    if rating > biggest:
        biggest = rating
        best_move = film_name

    if rating < smallest:
        smallest = rating
        worst_move = film_name

average_rating = rating_box / film_num

print(f"{best_move} is with highest rating: {biggest:.1f}")
print(f"{worst_move} is with lowest rating: {smallest:.1f}")
print(f"Average rating: {rating_box / film_num:.1f}")
