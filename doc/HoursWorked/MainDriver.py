from Employee import Employee

def Main():
    employee = []

    employee.append(Employee("Employee 1"))
    employee[-1].HoursWorked(Employee.SUNDAY, 2)
    employee[-1].HoursWorked(Employee.MONDAY, 4)
    employee[-1].HoursWorked(Employee.TUESDAY, 3)
    employee[-1].HoursWorked(Employee.WEDNESDAY, 4)
    employee[-1].HoursWorked(Employee.THURSDAY, 5)
    employee[-1].HoursWorked(Employee.FRIDAY, 8)
    employee[-1].HoursWorked(Employee.SATURDAY, 8)

    employee.append(Employee("Employee 2"))
    employee[-1].HoursWorked(Employee.SUNDAY, 7)
    employee[-1].HoursWorked(Employee.MONDAY, 3)
    employee[-1].HoursWorked(Employee.TUESDAY, 4)
    employee[-1].HoursWorked(Employee.WEDNESDAY, 3)
    employee[-1].HoursWorked(Employee.THURSDAY, 3)
    employee[-1].HoursWorked(Employee.FRIDAY, 4)
    employee[-1].HoursWorked(Employee.SATURDAY, 4)

    employee.append(Employee("Employee 3"))
    employee[-1].HoursWorked(Employee.SUNDAY, 3)
    employee[-1].HoursWorked(Employee.MONDAY, 3)
    employee[-1].HoursWorked(Employee.TUESDAY, 4)
    employee[-1].HoursWorked(Employee.WEDNESDAY, 3)
    employee[-1].HoursWorked(Employee.THURSDAY, 3)
    employee[-1].HoursWorked(Employee.FRIDAY, 2)
    employee[-1].HoursWorked(Employee.SATURDAY, 2)

    employee.append(Employee("Employee 4"))
    employee[-1].HoursWorked(Employee.SUNDAY, 9)
    employee[-1].HoursWorked(Employee.MONDAY, 3)
    employee[-1].HoursWorked(Employee.TUESDAY, 4)
    employee[-1].HoursWorked(Employee.WEDNESDAY, 3)
    employee[-1].HoursWorked(Employee.THURSDAY, 3)
    employee[-1].HoursWorked(Employee.FRIDAY, 4)
    employee[-1].HoursWorked(Employee.SATURDAY, 1)

    employee.append(Employee("Employee 5"))
    employee[-1].HoursWorked(Employee.SUNDAY, 3)
    employee[-1].HoursWorked(Employee.MONDAY, 5)
    employee[-1].HoursWorked(Employee.TUESDAY, 4)
    employee[-1].HoursWorked(Employee.WEDNESDAY, 3)
    employee[-1].HoursWorked(Employee.THURSDAY, 6)
    employee[-1].HoursWorked(Employee.FRIDAY, 4)
    employee[-1].HoursWorked(Employee.SATURDAY, 1)

    print("     Hours Work Report:")
    print("     Name        Total") 
    print("    -------------------")
    for emp in employee:
        print(f'     {emp.GetName()}     {emp.TotalHoursWorked()}')

Main()