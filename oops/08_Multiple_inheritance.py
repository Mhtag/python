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

    # Class method as an alternative constructor.
    @classmethod
    def from_str(cls, string):
        #params = string.split('-')
        #return cls(params[0], params[1], params[2])
        return cls(*string.split('-'))

class Player:
    var = 11
    no_of_games = 4
    def __init__(self,name,game):
        self.name = name
        self.game = game

    def printdetails(self):      
        return f'Name is {self.name}, Game plays {self.game}.'

class CoolProgrammer(Employee, Player):
    #var = 12
    pass


ankit = Employee('Ankit', 888, 'Employed')
mohit = Employee('Mohit', 1000, 'programmer')

subham = Player('Subham', 'Cricket')

rahul = CoolProgrammer('Rahul', 777, 'Programmer')

print(rahul.var)

