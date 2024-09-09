class Person:
    def __init__(self, f_name, l_name):
        self.f_name = f_name
        self.l_name = l_name
    
    def introduce(self):
        print(f"Hello my name is {self.f_name} {self.l_name}")

class Employee(Person):
    def __init__(self, f_name, l_name, employee_id):
        super().__init__(f_name, l_name) 
        self.employee_id = employee_id 
    def introduce(self):
        print(f"Hello my name is {self.f_name} {self.l_name}, my employee ID is: {self.employee_id}")    

person1 = Person("Aric", "Abbott")
employee1 = Employee("Aric", "Abbott", 521094)

person1.introduce()
employee1.introduce()


class Shape:
    def __init__(self, color):
        self.color = color

    def description(self):
        print(f"The Shape is {self.color}")

class Square(Shape):
    def __init__(self, color, side_length):
        super().__init__(color)
        self.side_length = side_length

    def description(self):
        print(f"The Square is {self.color} and has a side length of {self.side_length}")    
shape1 = Shape("Black")
square1 = Square("Black", 5)

shape1.description()
square1.description()


class Vehicle:
    def __init__(self, wheels):
        self.wheels = wheels
    
    def drive(self):
        print("The vehicle is driving")

class Car(Vehicle):
    def __init__(self, wheels, speed):
        super().__init__(wheels)
        self.speed = speed
    def drive(self):
        if self.speed >= 1: 
            print(f"The car is driving at {self.speed} mph")
        else:
            print("The car is driving.")    

vehicle1 = Vehicle(4)
vehicle2 = Car(4, 50)

vehicle1.drive()
vehicle2.drive()

class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height
    
    def area(self):
        print(self.width * self.height)
class Square(Rectangle):
    def __init__(self, width, height):
        super().__init__(width, height)
    
    def perimeter(self):
        print((self.width * 2) + (self.height * 2))

rectangle = Rectangle(5, 3)
square = Square(4, 5)

rectangle.area()
square.perimeter()




                  



    



