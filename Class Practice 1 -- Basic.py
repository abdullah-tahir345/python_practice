
class Car:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self.speed = 0
        
    def accelerate(self, amount):
        self.speed = self.speed + amount
        return self.speed
    
    def brake(self, amount):
        if self.speed > 0:
            self.speed = self.speed - amount
            if self.speed > 0:
                return self.speed
            else:
                return 'Speed must be greater than zero.'
        else:
            return 'Speed already zero.'
        
    def get_speed(self):
        return self.speed
    
    def get_info(self):
        x = f"{self.make}, {self.model}, {self.year} and {self.speed}."
        return x
    
# Test Case 1: Create a car object
car1 = Car("Toyota", "Camry", 2022)

# Test Case 2: Accelerate the car
print(car1.accelerate(30))

# Expected Result: Speed of the car increased to 30 mph
print(car1.get_info())

# Test Case 3: Brake the car
print(car1.brake(10))

# Expected Result: Speed of the car decreased to 20 mph
print(car1.get_info())

# Test Case 4: Ensure speed doesn't go below 0 when braking
car1.brake(25)

# Expected Result: Speed of the car is at a minimum of 0 mph
print(car1.get_info())

# Test Case 5: Create another car object
car2 = Car("Ford", "Mustang", 2023)

# Expected Result: Car object created with initial speed 0
print(car2.get_info())