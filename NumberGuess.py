from multiprocessing.resource_sharer import stop
import random


def guess(x):
    guessCount = 0
    random_number = random.randint(1, x)
    attempt = 0
    while(attempt != random_number and guessCount <= 4):
        attempt = int(input(f"Guess a number between 1 and {x}: "))
        guessCount += 1
        if attempt < random_number:
            print("Try again. Too low")
        elif attempt > random_number:
            print("Try again. Too High")
        elif attempt == random_number:
            print("YOU GOT IT!!")
    if(guessCount > 4 and attempt != random_number):
        print("YOU FREAKING FAILED!!! LMAO!!!")


guess(7)
