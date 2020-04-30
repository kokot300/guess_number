#!/usr/bin/python3

from random import randint


def random_number():
    return randint(1, 100)


def game():
    secret_number = random_number()
    print('Hi, I am a python program. I have thought a number from 1 to 100. \n Type q to quit')
    # game main loop
    while True:
        user_number = str(input('Can you guess it? \n'))
        try:
            user_number = int(user_number)
            if user_number == secret_number:
                secret_number = random_number()
                print("you won! \n let's do it again!")
            elif user_number > secret_number:
                print('that is too much!')
            else:
                print('that is not enough!')
        except:
            if user_number == 'q':
                print("see you soon \n")
                break
            else:
                print('Oops, it is not an integer number. Try again')
    return 0


if __name__ == '__main__':
    game()
