import math

height = int(input())
width = int(input())
percent = int(input())

area = math.ceil((height * width * 4) - (height * width * 4) * percent / 100)

while area >= 0:
    command = input()
    if command == "Tired!":
        print(f"{area} quadratic m left.")
        break
    paint = int(command)
    area -= paint

    if area < 0:
        if area == 0:
            print("All walls are painted! Great job, Pesho!")
        elif paint > 0:
            print(f"All walls are painted and you have {-area} l paint left!")

