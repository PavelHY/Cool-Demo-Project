import sys

n = int(input())

# Data Aggregation we need pre-defined variables with default values
# Sum -> By default is always 0
# Multiplication -> By default is always 1
# Max Number -> By default is always the smallest possible number
# Min Number -> By default is always the biggest possible number
num_sum = 0
max_num = -sys.maxsize
# n-iteration for loop
for i in range(0, n):
    # On every iteration we read a number
    # After the end of the iteration we lose the information about read number
    # We cannot know what was the previous number!!!
    curr_num = int(input())

    # Since we are loosing the number at the end of the iteration
    # We must do operations with the number NOW!!!
    if curr_num > max_num:
        # On the first iteration this is always TRUE!
        max_num = curr_num
    num_sum += curr_num

# Up to here: we have the sum of ALL numbers and the max number
# Sum of the other numbers (without max)
num_sum -= max_num

if num_sum == max_num:
    print('Yes')
    print(f'Sum = {num_sum}')
else:
    diff = abs(num_sum - max_num)
    print('No')
    print(f'Diff = {diff}')