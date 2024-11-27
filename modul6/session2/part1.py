class Car:
    def __init__(self, color='blue', doors=4, length=2.5):
        self.color = color
        self.doors = doors
        self.length = length

    def new_method(self):
        print(self.color and self.doors)

car = Car()

def get_car_info(car: Car):
    car_attribute = input("What attribute of the car to show: ")
    try:
        result = getattr(car, car_attribute)
    except AttributeError:
        print(f"Your car does not have the attribute: {car_attribute}")
        return
    if callable(result):  # check if the object passed as argument can be executed -- ()
        result()
    else:
        print(f"Car Attribute {car_attribute} has value: {result}", )

get_car_info(car)

print(hasattr(car, "example"))
print(hasattr(car, "price"), 'Car has no price')
setattr(car, "price", 100)
print(hasattr(car, "price"), f'Car price is {car.price}') # it will have .price

# car.__getattribute__()