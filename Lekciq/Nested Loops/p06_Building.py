number_floors = int(input())
number_flats = int(input())

flat_number = 0
flat_name = 0

for floor in range(number_floors, 0, -1):
    for flat in range(number_flats):
        flat_number = floor * 10 + flat

        if floor == number_floors:
            flat_name = f"L{flat_number}"
        elif floor % 2 != 0:
            flat_name = f"A{flat_number}"
        else:
            flat_name = f"O{flat_number}"
        print(flat_name, end=" ")
    print()
