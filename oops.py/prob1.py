class car:
    def __init__(self, brand, model):
     self.brand=brand
     self.model=model

    def full_name(self):
        return f"{self.brand} {self.model}"
class ElectricCar(car):
    def __init__(self,brand,model,battery_size):
        super().__init__(brand,model)
        self.battery_size=battery_size

my_tesla=ElectricCar("tesla","model s","85kwh")
print(my_tesla.full_name())    
'''
my_car=car("toyota","corolla")
print(my_car.brand)   
print(my_car.model)
my_new_car= car("tata","safari")
print(my_new_car.model)
'''