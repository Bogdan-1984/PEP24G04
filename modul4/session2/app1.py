def age_average():
    nr_participanti = int(input("Cati participanti avem la sondaj: "))
    total_age = []
    for user_number in range(1, nr_participanti + 1):
        while True:
            try:
                user_age = int(input(f"Introduceti varsta participantului {user_number} : "))
                break
            except Exception:
                print(f"Nu ati introdus un format valid pentru participantul {user_number}")

        total_age.append(user_age)
    age_average = sum(total_age) / len(total_age)
    return age_average

if __name__ == '__main__':
    print(f"Media de varsta a participantilor la sondajul de opinie este: {age_average()}")
