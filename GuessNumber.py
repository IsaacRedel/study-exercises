# Just "game guess number"

import random


random_number = random.randint(1, 10)
hit = False
while hit == False:
    guess = int(input('Guess a number between 0 and 10: '))
    if guess > random_number:
        print('Your guess was too high, please try again')
    elif guess < random_number:
        print('Your guess was too low, please try again')
    elif guess == random_number:
        hit = True
        print('Good job! you got it right!')
