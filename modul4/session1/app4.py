angajat1 = {
    'nume': 'Ana-Maria Popescu',
    'departament': 'IT',
    'ID': 3409,
    'Salar': 4560,
}
angajat2 = {
    'nume': 'Marian Muntean',
    'departament': 'IT',
    'ID': 2235,
    'Salar': 4556,
}
angajat3 = {
    'nume': 'Maria Manea',
    'departament': 'HR',
    'ID': 1908,
    'Salar': 6755,
}
angajat4 = {
    'nume': 'Oana Popa',
    'departament': 'HR',
    'ID': 1977,
    'Salar': 5400,
}
angajat5 = {
    'nume': 'David Codru',
    'departament': 'Management',
    'ID': 1988,
    'Salar': 12900,
}
lista_dict = [angajat1, angajat2, angajat3, angajat4, angajat5]


def show_high_pay_user(user_data: list, pay: int = 5000):
    for user in user_data:
        user: dict
        if user['Salar'] > pay:
            print(user['nume'], "->", f"{user['departament']}{user['ID']}")


def show_non_managers(user_data: list):
    users = []
    for user in user_data:
        user: dict
        if not user['departament'] == "Management":
            users.append(user['nume'])
    print(users)


def show_hr_pay_average(user_data: list):
    all_pay = []
    for user in user_data:
        user: dict
        if user['departament'] == "HR":
            all_pay.append(user['Salar'])
    print(sum(all_pay) / len(all_pay))


show_high_pay_user(lista_dict)
show_non_managers(lista_dict)
show_hr_pay_average(lista_dict)
