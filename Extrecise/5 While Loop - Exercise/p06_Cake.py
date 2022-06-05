width = int(input())
length = int(input())

cake = width * length

command = input()
while command != "STOP":
    pieces = int(command)
    cake -= pieces

    if cake <= 0:
        print(f"No more cake left! You need {abs(cake)} pieces more.")
        break
    command = input()
else:
    print(f"{abs(cake)} pieces are left.")


