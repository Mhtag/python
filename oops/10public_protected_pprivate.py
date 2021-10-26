class Employee:
    holidays = 10   # Creating a class variables.
    var = 10
    _protec = 9         # Protected variables can be used by classes and sub classes.
    __private =  7      # Private Variables  can be used by only this class.   

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
        return cls(*string.split('-'))

emp = Employee('Mohit', 222, 'programmer')

print(emp._protec)
print(emp.__private)