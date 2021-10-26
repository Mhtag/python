class Employee:
    def __init__(self, fname, lname):
        self.fname = fname
        self.lname = lname
        # self.email = f'{fname}.{lname}@email.com'

    
    def explain(self):
        return f'This employee is {self.name} {self.lname}'

    @property
    def email(self):
        if self.fname==None or self.lname==None:
            return 'Email is not found'
        return f'{self.fname}.{self.lname}@email.com'

    @email.setter
    def email(self, string):
        print('setting now')
        names = string.split('@')[0]
        self.fname = names.split('.')[0]
        self.lname = names.split('.')[1]

    @email.deleter
    def email(self):
        self.fname = None
        self.lname = None


emp1 = Employee('Mohit','Agarwal')
emp1.fname = 'Ankit'

print(emp1.email)

emp1.email = 'first.last@email.com'

print(emp1.lname)

del emp1.email

print(emp1.email)



