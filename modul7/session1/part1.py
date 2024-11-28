iterable_object = "He" #llo World"

iterator = iterable_object.__iter__()
first_object = iterator.__next__()
print(first_object)
second_object = iterator.__next__()
print(second_object)
# third_object = iterator.__next__()
# print(third_object)


class TriangleIterator:
    def __init__(self, sides: list):
        self.sides = sides

    def __iter__(self):
        return self

    def __next__(self):
        if not self.sides:
            raise StopIteration
        return self.sides.pop()


class Triangle:
    def __init__(self, A=1, B=1, C=1, AB=60, BC=60, CA=60):
        self.A = A
        self.B = B
        self.C = C
        self.AB = AB
        self.BC = BC
        self.CA = CA

    def __iter__(self):
        return TriangleIterator([('A', self.A), ('B', self.B), ('C', self.C)])


t = Triangle()

for side_name, side_value in t:
    print(f'Side {side_name} has value: {side_value}')