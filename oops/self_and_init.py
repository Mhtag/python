class Employee:
    holidays = 10   # Creating a class variable

    def __init__(self, name, salary, role):
        self.name = name
        self.salary = salary
        self.role = role

# Self is the object where this function will run
    def printdetails(self):      
        return f'Name is {self.name}, salary is {self.salary}, role is {self.role}.'

#objects
mohit = Employee('Mohit', 444, 'Unemployed')
ankit = Employee('Ankit', 500, 'employed')

# Instances
#
print(ankit.printdetails())