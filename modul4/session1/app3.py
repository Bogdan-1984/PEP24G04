def colecteaza_credentiale():
    credentiale = {}

    for i in range(1, 4):
        utilizator = input(f"Introduceti utilizatorul PC-ului {i}: ")
        parola = input(f"Introduceti parola PC-ului {i}: ")
        credentiale[utilizator] = parola

    return credentiale


def afiseaza_credentiale(credentiale):
    for utilizator, parola in credentiale.items():
        print(f"{utilizator} -> {parola}")


credentiale = colecteaza_credentiale()
afiseaza_credentiale(credentiale)
