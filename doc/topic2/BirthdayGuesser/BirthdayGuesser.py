class BirthdayGuesser:
    GRID_SIZE = 4
    MAX_GUESS = 5

    def __init__(self):  # fixed constructor
        self.CurrDayGrid = 0
        self.dates = [
            [
                [1, 3, 5, 7],
                [9, 11, 13, 15],
                [17, 19, 21, 23],
                [25, 27, 29, 31]
            ],
            [
                [2, 3, 6, 7],
                [10, 11, 14, 15],
                [18, 19, 22, 23],
                [26, 27, 30, 31]
            ],
            [
                [4, 5, 6, 7],
                [12, 13, 14, 15],
                [20, 21, 22, 23],
                [28, 29, 30, 31]
            ],
            [
                [8, 9, 10, 11],
                [12, 13, 14, 15],
                [24, 25, 26, 27],
                [28, 29, 30, 31]
            ],
            [
                [16, 17, 18, 19],
                [20, 21, 22, 23],
                [24, 25, 26, 27],
                [28, 29, 30, 31]
            ]
        ]

    def GetCurrentDayGrid(self):
        return self.dates[self.CurrDayGrid]

    def GetAddDays(self):  # renamed to match Main
        return self.dates[self.CurrDayGrid][0][0]

    def NextGrid(self):
        if self.CurrDayGrid < self.MAX_GUESS - 1:
            self.CurrDayGrid += 1
            return True
        return False
