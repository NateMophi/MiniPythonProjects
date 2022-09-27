import random


# def guess(x):
#     guessCount = 0
#     random_number = random.randint(1, x)
#     attempt = 0
#     while(attempt != random_number and guessCount <= 4):
#         attempt = int(input(f"Guess a number between 1 and {x}: "))
#         guessCount += 1
#         if attempt < random_number:
#             print("Try again. Too low")
#         elif attempt > random_number:
#             print("Try again. Too High")
#         elif attempt == random_number:
#             print("YOU GOT IT!!")
#     if(guessCount > 4 and attempt != random_number):
#         print("YOU FREAKING FAILED!!! LMAO!!!")

def ComputerGuess(x):
    low = 1
    high = x
    feedback = ""
    while(feedback != "c"):
        if low != high:
            computer_attempt = random.randint(low, high)
        else:
            computer_attempt = low
        feedback = input(
            f"Is {computer_attempt} too high (H), too low (L) or correct (C)??".lower())
        if feedback == "h":
            high = computer_attempt-1
        elif feedback == "l":
            low = computer_attempt + 1
    print(f"Yay the computer guessed my number {computer_attempt}, correctly")


ComputerGuess(25)
