width = int(input())
length = int(input())
height = int(input())

free_space = width * length * height

while True:
    command = input()

    if command == "Done":
        break

    boxes = int(command)
    free_space -= boxes

    if free_space <= 0:
        break

if command == "Done" or free_space > 0:
    print(f"{free_space} Cubic meters left.")
else:
    print(f"No more free space! You need {abs(free_space)} Cubic meters more.")


