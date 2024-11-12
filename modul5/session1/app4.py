import random


def comparare(x, y):
    # functie care va compara numerele extrase cu cele alese
    pass


def numere():
    # functie pentru extragerea numerelor
    all_49 = list(range(1, 50))
    results = list()
    for _ in range(6):
        selection = random.choice(all_49)
        all_49.remove(selection)
        results.append(selection)
    return results


def alegere():
    # functie pentru alegerea numerelor de catre user
    return numere()


while True:
    print("Se va juca 6/49. Alegeti 6 numere intre 1 si 49.")
    user_numbers = alegere()
    winning_numbers = numere()
    guesed_number = comparare(user_numbers, winning_numbers)
    if guesed_number == 6:
        break