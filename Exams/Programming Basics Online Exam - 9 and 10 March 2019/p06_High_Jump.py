desired_height = int(input())
desired_height_30 = desired_height - 30
unsuccessful = 0
jump_cnt = 0
is_successful = False
jump_score = int(input())
while True:
    for i in range(1, 3 + 1):
        jump_cnt += 1
        if jump_score > desired_height_30:
            desired_height_30 += 5
            unsuccessful = 0
            break
        else:
            unsuccessful += 1
            if unsuccessful >= 3:
                is_successful = True
            break
    if is_successful:
        print(f"Tihomir failed at {desired_height_30}cm after {jump_cnt} jumps.")
        break
    jump_score = int(input())
if desired_height_30 >= desired_height:
    print(f"Tihomir succeeded, he jumped over {desired_height_30}cm after {jump_cnt} jumps.")







