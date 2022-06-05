import sys
num = int(input())

smallest = sys.maxsize
biggest = -sys.maxsize

for i in range(0, num):
    numbers = int(input())
    if numbers > biggest:
        biggest = numbers
    if numbers < smallest:
        smallest = numbers

print(f"Max number: {biggest}")
print(f"Min number: {smallest}")
