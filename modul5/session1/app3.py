def medie_elevi():
    name = input('Introdueti numele elevului: ')
    grades = input('Introduceti notele elevului separate prin virgula:')

    list_grades = grades.split(',')
    all_grades = []
    for grade in list_grades:
        # try:
        #     grade = float(grade)
        # except:
        #     print("Not a valid grade")
        # else:
        #     all_grades.append(grade)
        assert grade.isnumeric(), f"Grade {grade} is not a number"
        assert 0 <= float(grade) <= 10, f"Grade {grade} is not within 0-10"
        grade = float(grade)
        all_grades.append(grade)

    average = sum(all_grades) / len(all_grades)
    print(f'Media este: {average}')
    if average >= 5:
        print(f'{name} a trecut clasa.')
    else:
        print(f'{name} a picat clasa.')


if __name__ == "__main__":
    medie_elevi()
