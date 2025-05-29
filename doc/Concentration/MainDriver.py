from Concentration import Concentration
import os
import time

def Main():
    while True:
        PlayGame()
        again = input("Would you like to play again? (y/n): ").strip().lower()
        if again != 'y':
            print("Thanks for playing")

def PlayGame():
    game   = Concentration()
    game.NewGame()
    matched = [False] * len(game.board)

    print("Welcome to the Concentration Game!")
    while not game.GameOver():
        # 1st pick
        DisplayBoard(game.board, matched)
        idx1 = GetValidIndex("Select the first card to flip: ",
                              len(game.board),
                              matched)
        # show only idx1 flipped
        DisplayBoard(game.board, matched, flipped=[idx1])

        # 2nd pick
        idx2 = GetValidIndex("Select the second card to flip: ",
                              len(game.board),
                              matched)
        # show both idx1 & idx2 flipped
        DisplayBoard(game.board, matched, flipped=[idx1, idx2])

        # check match
        if game.CorrectMatch(idx1, idx2):
            print("It's a match!")
            matched[idx1] = matched[idx2] = True
        else:
            print("Not a match.")
        time.sleep(2)   # give player a moment to see
    print("Congratulations! You’ve matched all the pairs!")


def DisplayBoard(board, matched, flipped=None):
    if flipped is None:
        flipped = []

    ClearScreen()
    print("Board:")
    for i in range(len(board)):
        if matched[i]:
            # already matched → show blank
            value = "   "
        elif i in flipped:
            # currently flipped → show the card’s face
            value = f"{board[i]:3d}"
        else:
            # face-down → show index
            value = f"{i:3d}"
        print(f"[ {value} ]", end=" ")
        if (i + 1) % 4 == 0:
            print()
    print()


def ClearScreen():
    os.system('cls' if os.name == 'nt' else 'clear')

def GetValidIndex(prompt, maxIndex, matched):
    while True:
        try:
            idx = int(input(prompt))
            if 0 <= idx < maxIndex and not matched[idx]:
                return idx
            else:
                print("Invalid index or card already matched. Try again.")
        except ValueError:
            print("Please enter a valid integer.")

if __name__ == "__main__":
    Main()
