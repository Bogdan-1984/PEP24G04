# # lambda functions
# c = int(input("give c: "))
#
# my_sum = lambda a, b: a + b + c
#
# print(my_sum(1, 2))
#
# c = int(input("give c: "))
#
#
# def my_sum(a, b):
#     return a + b + c
#
#
# print(my_sum(1, 2))

# map function
c = int(input("give c: "))
# def my_sum(a):
#     return a + c

# result = map(my_sum, [1,  4])
result = map(lambda a: a + c, [1,  4])
print(result)
print(list(result))


# filter function

result = filter(lambda a: a + c, [1,  4])
print(result)
print(list(result))