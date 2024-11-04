previous = 1

def calculate(n):
    global previous
    r = n * previous
    previous = r
    return r

while True:
    number = input("introduceti un numar: ")
    if number == "q".upper():
        break
    number = int(number)
    result = calculate(number)
    print(result)
