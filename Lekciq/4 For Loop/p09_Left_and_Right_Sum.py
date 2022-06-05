n = int(input())

left_sum = 0
right_sum = 0

for i in range(1, n + 1):
    l_sum = int(input())
    left_sum += l_sum

for j in range(1, n + 1):
    r_sum = int(input())
    right_sum += r_sum

if left_sum == right_sum:
    print(f"Yes, sum = {left_sum}")
else:
    diff = abs(right_sum - left_sum)
    print(f"No, diff = {diff}")
