import math
import sys

easter_cakes_num = int(input())
max_sugar = -sys.maxsize
max_flour = -sys.maxsize
sugar_cnt = 0
flour_cnt = 0

for _ in range(easter_cakes_num):
    sugar = int(input())
    flour = int(input())
    sugar_cnt += sugar
    flour_cnt += flour
    if sugar >= max_sugar:
        max_sugar = sugar
    if flour >= max_flour:
        max_flour = flour

total_sugar_needed = sugar_cnt / 950.0
total_flour_needed = flour_cnt / 750.0

print(f"Sugar: {math.ceil(total_sugar_needed)}")
print(f"Flour: {math.ceil(total_flour_needed)}")
print(f"Max used flour is {max_flour} grams, max used sugar is {max_sugar} grams.")
