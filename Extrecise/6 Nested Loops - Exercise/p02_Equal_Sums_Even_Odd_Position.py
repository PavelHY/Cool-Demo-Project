first_number = int(input())
second_number = int(input())

for number in range(first_number, second_number + 1):
    number_to_str = str(number)
    odd_cnt = 0
    even_cnt = 0

    for index, digit in enumerate(number_to_str):
        if index % 2 == 0:
            even_cnt += int(digit)
        else:
            odd_cnt += int(digit)

    if even_cnt == odd_cnt:
        print(number, end=" ")
        