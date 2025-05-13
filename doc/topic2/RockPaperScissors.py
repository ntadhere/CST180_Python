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
    pass
Main()