# generator

def generator_name():
    for i in range(10):
        yield i

gen1 = generator_name()

for i in gen1:
    print(i)

gen2 = (i for i in range(10))
print(type(gen2))