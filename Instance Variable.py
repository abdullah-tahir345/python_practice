# Instance variables are the variables in the class whose seprate copy is created for every object.
# Let's check it with an example

class Person(object):
    def __init__(self, name):
        self.name = name   #Instance variable
        self.age = 25      #Instance variable
        
    def print_info(self):
        print(f'Name : {self.name}')
        print(f'Age : {self.age}')
        
per1 = Person('Abdullah')
per2 = Person('Hamza')
per3 = Person('Usman')

# Instance variable of other object doesn't change if we change instance variable of other objects.

per1.name = 'Umair'

# Here instance variable value change from 'Abdullah' to 'Umair' but it doesn't change the value of other objects like
# per2 and per3. Let's check how to access the instance variable inside the class and outside the class.

# 1. Inside the class self.variable_name
# 2. Outside the class

print(per1.name)
print(per2.name)
print(per3.name)

print(per1.age)
print(per2.age)
print(per3.age)

