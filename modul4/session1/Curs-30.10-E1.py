def check_password(password):
    digit = False
    special = False
    length = False

    if len(password) >= 7:
        length = True
    for characters in password:
        if characters in ["%", "!", "@"]:
            special = True
        if characters.isdigit():
            digit = True
        if special and digit and length:
            print("parola este corecta")
            return True
    if not special:
        print("Parola trebuie sa contina una din urmatoarele caractere: %, !, @.")
    if not digit:
        print("Parola trebuie sa contina cel putin o cifra")
    if not length:
        print("Parola trebuie sa aiba lungimea mai mare de 7 caractere.")


while True:
    password = input("Introduceti o parola: ")
    if check_password(password):
        break