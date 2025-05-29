from BirthdayGuesser import BirthdayGuesser

def Main():
    guesser = BirthdayGuesser()
    day = 0

    while True:
        currGrid = guesser.GetCurrentDayGrid()
        for row in range(BirthdayGuesser.GRID_SIZE):
            for column in range(BirthdayGuesser.GRID_SIZE):
                print(f"{currGrid[row][column]:4}", end=" ")
            print()
        print()

        answer = input("Is your birthday in this set? (y/n)").strip().lower()
        if answer == 'y':
            day += guesser.GetAddDays()
        
        if not guesser.NextGrid():
            break

    print(f"Your birthday is {day}.")

Main()