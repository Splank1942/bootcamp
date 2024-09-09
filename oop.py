class Car:
    def __init__(self, make, model, year, tires, tiretype, color):
        self.color = color
        self.make = make
        self.model = model
        self.tires = tires
        self.tiretype = tiretype
        self.year = year    
        
    def start_engine(self):
        print(f"The {self.color} {self.year} {self.make} {self.model}'s engine starts, it has {self.tires} {self.tiretype} tires.")

class Tesla(Car):
    def __init__(self, make, model, year, tires, tiretype, color, battery_life):
        super().__init__(make, model, year, tires, tiretype, color)
        self.battery_life = battery_life
    
    def charge_battery(self):
        print(f"the battery life of the {self.make} {self.model} is {self.battery_life}")

my_car = Car("Toyota", "Corolla", 2020, 4, "All-Terrain", "Red")
my_car2 = Car("Lexus", "NX 300 F Sport", 2018, 4, "Sport", "Onyx")
tesla = Tesla("Tesla", "Model X", 2022, 4, "Sport", "Black", "12 Years")
my_car.start_engine()
my_car2.start_engine()
tesla.start_engine()
tesla.charge_battery()