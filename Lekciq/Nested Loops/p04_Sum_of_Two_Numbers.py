starting_interval = int(input())
final_interval = int(input())
combination = 0
magic_number = int(input())
flag = False

for first_num in range(starting_interval, final_interval + 1):
    for second_num in range(starting_interval, final_interval + 1):

        combination += 1

        if first_num + second_num == magic_number:
            flag = True
            print(f"Combination N:{combination} ({first_num} + {second_num} = {magic_number})")
            break
    if flag:
        break

if not flag:
    print(f"{combination} combinations - neither equals {magic_number}")
