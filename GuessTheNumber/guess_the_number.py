import random

random_number = random.randint(1, 100)
chance = 5

while chance > 0:
    guess = int(input('Your guess: '))

    if guess >= 1 and guess <= 100:
        if guess == random_number:
            print('Congratulations! Your answer is correct')
        if guess < random_number:
            print('Too Low')
            chance -= 1
            print(f'Chance: {chance}')
        if guess > random_number:
            print('Too High')
            chance -= 1
            print(f'Chance: {chance}')
        if chance == 0:
            print('Your chance is over!')
    else:
        print('Your guess must be between 1 and 100!')