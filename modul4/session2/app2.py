def suma(lista: list):
    return sum(lista)


def medie(lista: list):
    return sum(lista) / len(lista)


def putere(lista: list):
    result = []
    for i in lista:
        result.append(i ** 2)
    return result


meniu = {
    "1": medie,
    "2": suma,
    "3": putere,
    "4": quit

}

option = None


def get_user_numbers():
    numbers = []
    while True:
        try:
            number = int(input("give number"))
            numbers.append(number)
        except ValueError as e:
            if 'x' in str(e):
                break
            else:
                print("bad number")
    return numbers


def show_menu():
    print("""Meniu:
1. Media numerelor
2. Suma numerelor
3. Puterea numerelor din lista de numere
4. Iesire""")

    global option
    option = input("Introduceti optiunea dvs: ")


def execute(menu: dict, numbers: list):
    global option
    f = menu[option]  # extract function from dict using user input and save in variable f
    if option == '4':  # user selected Iesire
        numbers = 0  # force exit code 0
    print(f'Rezultatul: {f(numbers)}')


if __name__ == '__main__':
    n_list = get_user_numbers()
    show_menu()
    execute(meniu, n_list)
