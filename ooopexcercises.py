class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.area = self.height * self.width
        self.perimeter = (self.height * 2) + (self.width * 2)
    
    def get_area(self):
        print(self.area)
    def get_perimeter(self):
        print(self.perimeter)    




rec = Rectangle(4, 5)

rec.get_area()
rec.get_perimeter()



class Person:
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender
    
    def introduction(self):
        print(f"This is {self.name}, he is {self.age} years old and is a {self.gender}!")

p1 = Person("Aric", "34", "Male")    


p1.introduction()

class Book:
    def __init__(self, title, author, genre):
        self.title = title
        self.author = author
        self.genre = genre

    def get_title(self):
        print(f"The title of the book is {self.title}")
    def get_author(self):
        print(f"The author of the book is {self.author}")
    def get_genre(self):
        print(f"The genre of the book is {self.genre}")
book1 = Book("Horus Rising", "Dan Abnett", "Sci-Fi - Warhammer 40k" )


book1.get_title()
book1.get_author()
book1.get_genre()


class Student:
    def __init__(self, name, age, major, GPA):
        self.name = name
        self.age = age
        self.major = major
        self.GPA = GPA
    
    def get_name(self):
        print(f"The name of the student is {self.name}")
    def get_age(self):
        print(f"The age of the student is {self.age}")
    def get_major(self):
        print(f"The student's major is {self.major}")
    def get_GPA(self):
        print(f"The student's GPA is  {self.GPA}")
    def get_grade(self):
        if {self.GPA} == 4:
            g = "A"
        elif {self.GPA} in range(3,4):
            g = "B"
        elif {self.GPA} in range(2,3):
            g = "C"
        elif {self.GPA} in range(1,2):
            g = "D"
        else:
            g = "F"
        print(f"The student's Grade is a {g}")
student1 = Student("Aric", "34", "Computer Science", int(3.8))

student1.get_name()
student1.get_age()
student1.get_major()
student1.get_GPA()
student1.get_grade()



class Animal:
    def __init__(self,name, species):
        self.name = name
        self.species = species
    
    def get_name(self):
        print(f"The animal's name is {self.name}")
    def get_species(self):
        print(f"the animal's species is {self.species}")
    def eat(self):
        print(f"{self.name} the {self.species} is eating {food}")  
    def sleep(self):
        print(f"{self.name} the {self.species} is sleeping")      


animal1 = Animal("Harry", "Hiena")

animal1.get_name()
animal1.get_species()
food = input("what food do you give the animal? ")        
animal1.eat()
animal1.sleep()