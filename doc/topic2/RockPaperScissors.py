import random

UserRock = 1
UserPaper = 2
UserScissors = 3
ComputerRock = 4
ComputerPaper = 5
ComputerScissors = 6

def Main():
    while True:
        PlayGame()
        again = input("Do you want to play again? (y/n):").strip().lower()
        if again != 'y':
            print("Thanks for playing.")
            break

def PlayGame():
    computerSelection = random.randrange(3) + 4
    while True:
        userNum = int(input("Enter 1 - Rock, 2 - Paper, 3 - Scissors:"))
        if userNum not in range(1,4):
            print("Please enter 1,2, or 3")
        else:
            break

    match computerSelection:
        case 4:
            print("Computer selected Rock.")
        case 5:
            print("Computer selected Paper.")
        case _:
            print("Computer selected Scissors")

    match computerSelection * userNum:
        case 6 | 8 | 15:
            print("Player Wins!!!")
        case 5 | 12:
            print("Computer Win!!!")
        case _:
            print("Tie")
Main()