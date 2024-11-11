import random

options = {'p': 'piatra', 'f': 'foarfeca', 'h': 'hartie'}


def get_winner(user_selection, computer_selection):
    if user_selection == computer_selection:
        return None
    if user_selection == 'h':
        if computer_selection == 'f':
            return False
        if computer_selection == 'p':
            return True
    if user_selection == 'f':
        if computer_selection == 'h':
            return True
        if computer_selection == 'p':
            return False
    if user_selection == 'p':
        if computer_selection == 'f':
            return True
        if computer_selection == 'h':
            return False


def game():
    options_list = []
    for key, value in options.items():
        option = f"{key} ({value})"
        options_list.append(option)
    options_string = ", ".join(options_list)
    name = input("Introduceti numele: ")
    user_selection = input(f"Introduceti optiunea [{options_string}, q pentru a iesi]: ")
    if user_selection not in options:
        print("Optiune invalida. Incearca dinnou")
    computer_selection = random.choice(list(options.keys()))
    print(f"> {name} : {user_selection} \n"
          f"> Server : {computer_selection}")
    result = get_winner(user_selection, computer_selection)
    if result is True:
        print(f"{name} Ai Castigat! ")
    elif result is False:
        print("Computerul a castigat!")
    elif result is None:
        print("Egalitate")


if __name__ == "__main__":
    game()
