import random


def play():
    userScore = 0
    computerScore = 0
    TotalScore = userScore+computerScore

    while (TotalScore <= 9):
        user = input("'r' for rock, 'p' for paper, 's' for scissors: ")
        computer = random.choice(['r', 'p', 's'])
        if user == computer:
            print("DRAW")
            print(f"{userScore} : {computerScore}")
        elif user == 'r' and computer == 's':
            userScore += 1
            print("YOU WIN")
            print(f"{userScore} : {computerScore}")
        elif user == 'p' and computer == 'r':
            userScore += 1
            print("YOU WIN")
            print(f"{userScore} : {computerScore}")
        elif user == 's' and computer == 'p':
            userScore += 1
            print("YOU WIN")
            print(f"{userScore} : {computerScore}")
        elif computer == 'r' and user == 's':
            computerScore += 1
            print("CPU WINS")
            print(f"{userScore} : {computerScore}")
        elif computer == 'p' and user == 'r':
            computerScore += 1
            print("CPU WINS")
            print(f"{userScore} : {computerScore}")
        elif computer == 's' and user == 'p':
            computerScore += 1
            print("CPU WINS")
            print(f"{userScore} : {computerScore}")
        if (userScore == 5 and computerScore < 5):
            print("YOU WIN THE SET")
        elif (userScore < 5 and computerScore == 5):
            print("CPU WINS THE SET")


play()
