'''
This program is a number-guessing game
'''

import sys
from random import randint

print("This is an interactive guessing game!\n\
You have to enter a number between 1 and 99 to find out the secret number.\n\
Type 'exit' to end the game.\n\
Good luck!")

answer = randint(1, 99)
# answer = 42
ATTEMPTS = 0

while True:
    print('\nWhat\'s your guess between 1 and 99?')
    try:
        user_input = input()
        ATTEMPTS += 1
    except EOFError:
        print("\033[93mInput cannot be empty!\033[0m")
        continue
    if user_input == 'exit':
        print("Goodbye!")
        sys.exit()
    else:
        try:
            n = int(user_input)
            if n < 1 or n > 99:
                raise ValueError
        except ValueError:
            print(f'\033[93m{user_input} is not a number between 1 and 99. Try again!\033[0m')
            continue

    if n > answer:
        print("Too high!")
        continue
    if n < answer:
        print("Too low!")
        continue
    if answer == 42:
        print(
            "The answer to the ultimate question of life, the universe and everything is 42.")
    else:
        print("Congratulations, you've got it!")
    if ATTEMPTS == 1:
        print("Congratulations! You got it on your first try!")
    else:
        print(f"You won in {ATTEMPTS} attempts!")
    break
