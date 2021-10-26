class Employee:
    holidays = 10   # Creating a class variable
    var = 10

    def __init__(self, name, salary, role):
        self.name = name
        self.salary = salary
        self.role = role

    # Self is the object where this function will run
    def printdetails(self):      
        return f'Name is {self.name}, salary is {self.salary}, role is {self.role}.'

    @classmethod
    def change_holidays(cls, newholidays):
        cls.holidays = newholidays 

    def __add__(self, other):
        return self.salary + other.salary

    def __truediv__(self, other):
        return self.salary / other.salary

    def __str__(self):
        return f'Name is {self.name}, salary is {self.salary}, role is {self.role}.'

    def __repr__(self):
        return f"Employee['{self.name}', {self.salary}, '{self.role}']"


emp1 = Employee('Mohit',500,'programmer')
emp2 = Employee('Ankit', 1000, 'Buisness')


print(emp1/emp2)

print(emp1)