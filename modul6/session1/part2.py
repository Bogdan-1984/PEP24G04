# builtin methods

class Car:

    def __init__(self, color: str, nr_of_seats=5):
        self.color = color
        self.nr_of_seats = nr_of_seats

    def __str__(self):
        return f"{self.color.capitalize()} car with {self.nr_of_seats} seats"

    def __repr__(self):
        return f"{self.color.capitalize()} car with {self.nr_of_seats} seats"


car1 = Car('blue')
print(car1)
car2 = Car('yellow')
car3 = Car('green')
cars = [car1, car2, car3]
# str(car)
print(cars)
