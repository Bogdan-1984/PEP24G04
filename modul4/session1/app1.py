# Module 4 #pbma 1

print('Name of this script is: ', __name__)


def check_password(password):
    digit = False
    special = False
    length = False
    if len(password) >= 7:
        length = True
    for character in password:
        if character in ['!', '@', '%']:
            special = True
        if character.isdigit():
            digit = True
        if special and digit and length:
            print("Parola este corecta ")
            return True
    if not special:
        print("Parola trebuie sa contina caractere speciale")
    if not digit:
        print("Parola trebuie sa contina cel putin o cifra")
    if not length:
        print("Parola nu are lugimea mai mare de 7 caractere")


if __name__ == "__main__":
    while True:
        password = input("Introduceti parola: ")
        if check_password(password):
            break
