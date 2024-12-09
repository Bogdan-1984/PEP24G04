from datetime import datetime


class Elev:
    def __init__(self, nume, data_nasterii: datetime):
        self.name = nume
        self.data_nasterii = data_nasterii

    def __repr__(self):
        return f'{self.name}:{self.data_nasterii}'

    def days_to_birthday(self):
        date_now = datetime.now()
        date_birthday = datetime(date_now.year, self.data_nasterii.month, self.data_nasterii.day)
        return date_birthday - date_now


with open('data.txt', 'r') as file:
    lines = file.readlines()
elevi = list(
    map(
        lambda t: Elev(t.split("/")[0], datetime.strptime(t.split("/")[1].strip(), '%Y-%m-%d')),
        lines
    )
)
print(elevi)

for elev in elevi:
    print(elev.days_to_birthday())
