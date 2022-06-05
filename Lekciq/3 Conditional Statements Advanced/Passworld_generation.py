from string import ascii_letters, digits, punctuation
import random

signs = ascii_letters + digits + punctuation
length = 12

password = ''.join(random.sample(signs, length))

print(password)
