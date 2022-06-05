k_first_num_1_digit = int(input())
l_first_num_2_digit = int(input())
m_second_num_1_digit = int(input())
n_second_num_2_digit = int(input())
counter = 0
has_end = False

for first_num_1_digit in range(k_first_num_1_digit, 8 + 1):
    for first_num_2_digit in range(9, l_first_num_2_digit + 1):
        for second_num_1_digit in range(m_second_num_1_digit, 8 + 1):
            for second_num_2_digit in range(9, n_second_num_2_digit + 1):

                if first_num_1_digit % 2 == 0 or second_num_1_digit % 2 == 0 or first_num_2_digit % 2 != 0 or second_num_2_digit % 2 != 0:
                    first_num = first_num_1_digit * 10 + first_num_2_digit
                    second_num = second_num_1_digit * 10 + second_num_2_digit
                    if first_num == second_num:
                        print("Cannot change the same player.")
                    else:
                        print(f"{first_num_1_digit}{first_num_2_digit} - {second_num_1_digit}{second_num_2_digit}")
                        counter += 1
                    if counter >= 6:
                        has_end = True
                    if has_end:
                        break



