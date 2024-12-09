from modul7.session2.app1 import EnumeratorCuvant

user_input = input("Introduceti un cuvant: ")
if user_input.isalpha():
    ec = EnumeratorCuvant(user_input)

    with open(f'{user_input}.txt', 'wt') as file:
        for i, litera in ec:
            file.write(f"{i}: {litera}\n")
