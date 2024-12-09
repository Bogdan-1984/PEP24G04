class A:
    def __init__(self, name, number):
        self.name = name
        self.number = number

    def __eq__(self, other):
        return self.number == other.number and self.name == other.name


a1 = A('x', 3)
a2 = A('x', 3)

print(a1 == a2)
