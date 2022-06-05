start = int(input())
end = int(input())

start_1 = int(start / 1000)
start_2 = int((start / 100) % 10)
start_3 = int((start / 10) % 10)
start_4 = int(start % 10)

end_1 = int(end / 1000)
end_2 = int((end / 100) % 10)
end_3 = int((end / 10) % 10)
end_4 = int(end % 10)

for num_1 in range(start_1, end_1 + 1):
    for num_2 in range(start_2, end_2 + 1):
        for num_3 in range(start_3, end_3 + 1):
            for num_4 in range(start_4, end_4 + 1):
                if num_1 % 2 != 0 and num_2 % 2 != 0 and num_3 % 2 != 0 and num_4 % 2 != 0:
                    print(f'{num_1}{num_2}{num_3}{num_4}', end=' ')