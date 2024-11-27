iterable_object = "He" #llo World"

iterator = iterable_object.__iter__()
first_object = iterator.__next__()
print(first_object)
second_object = iterator.__next__()
print(second_object)
third_object = iterator.__next__()
print(third_object)