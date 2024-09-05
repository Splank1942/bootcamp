class Car:
    def __init__(self, make, model, year, tires):
        self.make = make
        self.model = model
        self.year = year
        self.tires = tires
    
    def start_engine(self):
        print(f"The {self.year} {self.make} {self.model}'s engine starts, it has {self.tires} tires.")

my_car = Car("Toyota", "Corolla", 2020, 4)
my_car2 = Car("Lexus", "NX 300 F Sport", 2018, 4)
my_car.start_engine()
my_car2.start_engine()
