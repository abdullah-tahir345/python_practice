# Class/Static variable are the variable whose single copy is available for all the objects/instances. And it's access in a 
# class using cls.variable_name and using class_name.variable_name outside the class.

class Person:
    student = 'Yes'          #Static/Class Variable -- Class Namespace
    
    def __init__(self, name, age):
        self.name = name     #Instance Variable
        self.age = age       #Instance Variable

    def access_instance_variable(self):
        print('Name : ', self.name)
        print('Age : ', self.age)              #Access the instance variable
        
    @classmethod
    def access_class_variable(cls):
        print('Is Student : ', cls.student)    #Access class/static variable inside the class
        

per1 = Person('Abdullah', 25)      # -- Instance Namespace
per2 = Person('Hamza', 21)         # -- Instance Namespace
per3 = Person('Umair', 18)         # -- Instance Namespace

# Access instance variable and class variable for 1st object
per1.access_instance_variable()
Person.access_class_variable()

print()
# Change the value of class/static varible to no
Person.student = 'No'
per1.access_instance_variable()
Person.access_class_variable()
print()

# Change the class/static variable name using object name
per2.student = 'Will be student'
per2.access_instance_variable()
print('Is Student : ',per2.student)