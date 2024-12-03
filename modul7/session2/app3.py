user_input = input("Introduceti salariile separate cu virgula: ")
crestere_salariala = int(input("Introduceti procentul de marire: "))
lista_salarii = user_input.split(",")
lista_salarii_int = list(map(lambda s: int(s), lista_salarii))
salarii_marite = list(map(lambda s: s * (100 + crestere_salariala) / 100, lista_salarii_int))
for salar_marit in salarii_marite:
    print(salar_marit)
