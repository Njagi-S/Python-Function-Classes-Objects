# 1.Define a class Rectangle with attributes width and height.Add methods area and perimeter to calculate the area and perimeter of the rectangle.Instantiate a few rectangle objects and print their area and perimeter.
class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height
    
    def area(self):
        return self.width * self.height
    
    def perimeter(self):
        return 2 * (self.width + self.height)
rec1 = Rectangle(46,90)
rec2 = Rectangle(60,20)
rec3 = Rectangle(80,35)
print(f"The area of the first rectangle is {rec1.area()} while the perimeter is {rec1.perimeter()}")
print(f"The area of the second rectangle is {rec2.area()} while the perimeter is {rec2.perimeter()}")
print(f"The area of the third rectangle is {rec3.area()} while the perimeter is {rec3.perimeter()}")

# 2.Create a class Employee with attributes name and salary.Add a method give_raise that increases the salary by a given percentage.Instantiate an employee, give them a raise, and display their new salary.
class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def give_raise(self, percentage):
        raise_amount = self.salary * (percentage / 100)
        self.salary += raise_amount
        return self.salary

    def display_salary(self):
        return f"{self.name}'s new salary is: {self.salary:.2f} Ksh."


# Instantiate an employee
employee = Employee("John Doe", 50000)

# Give them a raise
employee.give_raise(10)

# Display their new salary
print(employee.display_salary())

# 3.Create a base class Vehicle with attributes brand and model.
# Create two subclasses Car and Motorcycle that inherit from Vehicle and add unique methods to each subclass (e.g., honk for Car and rev_engine for Motorcycle).
# Instantiate both subclasses and call their methods.
class Vehicle:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

class Car(Vehicle):
    def honk(self):
        return f"Vehicle Brand: {self.brand}, Model: {self.model} and it goes Beep!"


class Motorcycle(Vehicle):
    def rev_engine(self):
        return f"Vehicle Brand: {self.brand}, Model: {self.model} and it goes Vroom! Vroom!"


# Instantiate the Car subclass
my_car = Car("Toyota", "Corolla")
print(my_car.honk())          # Call the honk method

# Instantiate the Motorcycle subclass
my_motorcycle = Motorcycle("Harley-Davidson", "Street 750")
print(my_motorcycle.rev_engine())     # Call the rev_engine method



class Animal:
    def __init__(self,name):
        self.name = name
        
    def sound(self):
        return f"{self.name} is a Cow and it Moos!,"

class Cow(Animal):
    def __init__(self,name,breed):
        super ().__init__(name)
        self.breed = breed
        
    def sound(self):
        parent_sound = super().sound()
        return f"{parent_sound} the breed is a {self.breed}"
    

mycow = Cow("John","Fresian")
print(mycow.sound())