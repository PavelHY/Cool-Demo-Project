egg_num = int(input())
red_edd = 0
orange_egg = 0
blue_egg = 0
green_egg = 0

max_num_of_egg = 0
color = ""

for _ in range(egg_num):
    color_egg = input()
    if color_egg == "red":
        red_edd += 1
    elif color_egg == "orange":
        orange_egg += 1
    elif color_egg == "blue":
        blue_egg += 1
    elif color_egg == "green":
        green_egg += 1

if red_edd > max_num_of_egg:
    max_num_of_egg = red_edd
    color = "red"
if orange_egg > max_num_of_egg:
    max_num_of_egg = orange_egg
    color = "orange"
if blue_egg > max_num_of_egg:
    max_num_of_egg = blue_egg
    color = "blue"
if green_egg > max_num_of_egg:
    max_num_of_egg = green_egg
    color = "green"

print(f"Red eggs: {red_edd}")
print(f"Orange eggs: {orange_egg}")
print(f"Blue eggs: {blue_egg}")
print(f"Green eggs: {green_egg}")
print(f"Max eggs: {max_num_of_egg} -> {color}")
