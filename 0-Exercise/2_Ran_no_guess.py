# Guess a number

import random as r
a = 0
b = 100

r_no = r.randint(a, b)

for i in range(10):
    guess = int(input('Guess a no. between {} and {}: '.format(a, b)))

    if guess == r_no:
        print('You Won')
    elif guess > r_no:
        print('Enter a small no.')
    else:
        print('Enter a bigger no.')
