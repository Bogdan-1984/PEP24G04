# # classes
#
# class Car:
#     color = "white"
#     # pass
#
# car = Car()
# print(type(car))
# print(type('car'))
# print('Color of the car from class Car is: ', Car.color)
# print('Color of the car from class Car is: ', Car.color)
# print('Color of the car from object car is: ', car.color)
#
# print("Change color")
# car1 = Car()
# car2 = Car()
# print(car1.color)
# print(car2.color)
# car1.color = "yellow"
# car2.color = "blue"
# print(car1.color)
# print(car2.color)
# print('Color from construction:', Car.color)
# Car.color = 'new color'
# print(Car.color)
# car3 = Car()
# print(f"color of car3 is: {car3.color}")
import random


# class Car:
#
#     def __init__(self, color: str):
#         print(id(self))
#         self.color = color
#         self.doors = input("give number of doors:")
#         # self.color = random.choice(['blue', 'green', 'black'])
#
# car1 = Car('green')
# print(id(car1))
# print(car1.color)
# print(car1.doors)
#
# car2 = Car('blue')
# print(id(car2))
# print(car2.color)
# print(car2.doors)

class Car:

    def __init__(self, color: str):
        # print(id(self))
        self.color = color

    def turn_left(self):
        print(id(self))
        print("turning left")

car1 = Car('yellow')
# Car.turn_left('test')
print(id(car1))
car1.turn_left()
