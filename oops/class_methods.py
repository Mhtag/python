class Employee:
    holidays = 10   # Creating a class variable

    def __init__(self, name, salary, role):
        self.name = name
        self.salary = salary
        self.role = role

# Self is the object where this function will run
    def printdetails(self):      
        return f'Name is {self.name}, salary is {self.salary}, role is {self.role}.'

# class method will access class and instances from class
    @classmethod
    def change_holidays(cls, newholidays):
        cls.holidays = newholidays 

mohit = Employee('Mohit',555,'programmer')

mohit.change_holidays(20)

print(mohit.holidays)