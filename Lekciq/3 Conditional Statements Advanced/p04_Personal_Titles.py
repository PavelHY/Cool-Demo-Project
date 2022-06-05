yars = float(input())
gender = input()

if yars >= 16 and gender == "m":
    print("Mr.")
elif yars < 16 and gender == "m":
    print("Master")
elif yars >= 16 and gender == "f":
    print("Ms.")
elif yars < 16 and gender == "f":
    print("Miss")
    