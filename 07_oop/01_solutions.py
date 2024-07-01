class Car:
    totalcars=0

    def __init__(self, brand, model):
        self.__brand = brand
        self.__model = model
        Car.totalcars+=1

    def get_brand(self):
        return self.__brand + " !"
    
    def display_detail(self):
        return f"{self.__brand}{self.__model}"    

    def fuel_type(self):
        return("Petrol or Diesel")    
    @property
    def model(self):
        return self.__model

class ElectricCar(Car):
    def  __init__(self, brand, model, battery_size):
        super().__init__(brand, model)
        self.battery_size=battery_size

    def display_detail(self):
        return f"{self.brand} {self.model}, Battery Size: {self.battery_size}"
    
    def fuel_type(self):
        return("Electric Charge")  



petrol_car=Car("Mercedes", " E 250")
# petrol_car.model="City"
print(petrol_car.model)  










# petrol_car=Car("Mercedes", " E 250")
# print(petrol_car.fuel_type())  

# my_tesla=ElectricCar("Tesla", " Model S", " 85kWh")
# print(my_tesla.fuel_type()) 

# my_car2=Car("Audi", " A 5")
# print(petrol_car.display_detail())  

# my_car3=ElectricCar("Audi", " E-Tron GT", " 60kWh")
# print(my_tesla.display_detail) 


# print("Total car production: ", Car.totalcars)




# print(my_tesla.brand)  
# print(my_tesla.get_brand())  

# my_car= Car("Toyota", " Corolla")
# print(my_car.display_detail())

# my_new_car=Car("Honda", " Civic")
# print(my_new_car.display_detail())