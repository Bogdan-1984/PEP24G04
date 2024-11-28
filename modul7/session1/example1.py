class CarIterator:
    def __init__(self, atr: list):
        self.atr = atr

    def __iter__(self):
        return self

    def __next__(self):
        if not self.atr:
            raise StopIteration
        return self.atr.pop()


class Car:
    def __init__(self, color='blue', doors=4, length=2.5):
        self.color = color
        self.doors = doors
        self.length = length

    def __iter__(self):
        result = []
        for atr in self.__dir__():
            if not atr.startswith("__"):
                result.append(atr)
        return CarIterator(result)


car = Car()
# print(car.__dir__())
for element in car:
    print(element)
