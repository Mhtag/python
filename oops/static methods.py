class Employee:
    holidays = 10   # Creating a class variable

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

    @classmethod
    def from_dash(cls, string):
        return cls(*string.split('-'))

    @staticmethod
    def print_good(string):
        print('This is good ' + string)

mohit = Employee('Mohit', 554, 'programmer')
ankit = Employee('Ankit', 888, 'buisness')

print(mohit.print_good(ankit))