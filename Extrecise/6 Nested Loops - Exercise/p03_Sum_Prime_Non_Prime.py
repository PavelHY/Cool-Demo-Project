from math import sqrt
from math import ceil

prime_sum = 0
non_prime_sum = 0

command = input()
while command != 'stop':
    # We have a number
    curr_number = int(command)

    # First we take care of special (edge) cases
    if curr_number < 0:
        # If the number is negative
        print('Number is negative.')
        command = input()
        continue

    if curr_number < 1:
        non_prime_sum += curr_number
    else:
        # We have curr_number and we should check if the number is prime
        # Here it is an algorithm for finding prime numbers
        # By default we assume that the number is prime and we will try to prove the opposite
        is_prime = True
        for div in range(2, curr_number):
            if curr_number % div == 0:
                is_prime = False
                break

        if is_prime:
            prime_sum += curr_number
        else:
            non_prime_sum += curr_number

    command = input()

print(f'Sum of all prime numbers is: {prime_sum}')
print(f'Sum of all non prime numbers is: {non_prime_sum}')