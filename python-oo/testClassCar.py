from car import Car
car = Car('Hb20','Hyundai','2016')
print("Car Name - " + car.name)
print("Make - " + car.make)
print("Year - " + car.year)
print("Value x in class Car - " + Car.x)
print("Value x in variable car - " + car.x)
print("Call function drive - " + car.drive())
car.hello('teste')

car.show();