class Employee:
    SUNDAY = 0
    MONDAY = 1
    TUESDAY = 2
    WEDNESDAY = 3
    THURSDAY = 4
    FRIDAY = 5
    SATURDAY = 6
    DAYS_IN_WEEK = 7

    def __init__(self, name: str):
        self.name = name
        self.hours = [0] * self.DAYS_IN_WEEK

    def GetName(self):
        return self.name
    
    def HoursWorked(self, day, hours):
        if self.SUNDAY <= day <= self.SATURDAY:
            self.hours[day] = hours

    def TotalHoursWorked(self):
        return sum(self.hours)