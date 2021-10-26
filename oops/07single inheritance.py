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

class Programmer(Employee):
    def __init__(self, name, salary, role, languages):
        self.name = name
        self.salary = salary
        self.role = role
        self.languages = languages


    def printprog(self):
        return f'Programmer name is {self.name}, salary is {self.salary} and role is {self.role}, the languages are {self.languages}'



ankit = Employee('Ankit', 888, 'Employed')
sunil = Employee.from_str('Sunil-999-Senior')

mohit = Programmer('Mohit', 1000, 'programmer', 'python')
micku = Programmer('Micku' ,800, 'programmer', 'Python')



print(mohit.printprog())
print(mohit.printdetails())