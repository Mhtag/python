class Employee:
    holidays = 10   # Creating a class variable
    pass

#objects
mohit = Employee()
ankit = Employee()

# Instances
mohit.name = 'Mohit'
mohit.salary = 444
mohit.role = 'unemployed'

ankit.name = 'Ankit'
ankit.salary = 555
ankit.role = 'unemployed'

print(ankit.holidays)

# if i want to change the class variable 

Employee.holidays = 8      # changed the class intance 
print(Employee.holidays)

# Now if I want to change the class variable by the help of object or instances
print(ankit.__dict__)

ankit.holidays=11            # only changed holidays for this particular instance.
                             # it will not change the holiday variable for whole class     

print(ankit.__dict__)
# here when we print ankit instance we are getting holidays as its aditional instance

print(Employee.holidays)
print(Employee.__dict__)




