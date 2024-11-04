previous = 1


def calculate(n):
    global previous
    r = n * previous
    previous = r
    return r


while True:
    number = input("Introduceti numarul: ")
    if number == 'q':
        break
    number = int(number)
    result = calculate(number)
    print(f"Rezultatul este: {result}")
