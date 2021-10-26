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

# Class method as an alternative constructor.
    @classmethod
    def from_str(cls, string):
        #params = string.split('-')
        #return cls(params[0], params[1], params[2])
        return cls(*string.split('-'))


mohit = Employee('Mohit', 555, 'Unemployed')
ankit = Employee('Ankit', 888, 'Employed')
sunil = Employee.from_str('Sunil-999-Senior')

print(sunil.printdetails())