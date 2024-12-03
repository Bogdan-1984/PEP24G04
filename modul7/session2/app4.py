class Angajat:
    def __init__(self, nume, salar, departament):
        self.nume = nume
        self.salar = salar
        self.departament = departament

    def crestere_salar(self, procent):
        self.salar = self.salar * (100 + procent) / 100

    def __str__(self):
        return f"Nume: {self.nume}, Salar: {self.salar}. Departament : {self.departament}"

    def __repr__(self):
        return f"{self.nume}:{self.departament}"


class Angajati:
    lista_angajati: list[Angajat] = []

    def adauga_angajati(self, *args):
        self.lista_angajati.extend(list(args))

    def detalii_angajat(self):
        for angajat in self.lista_angajati:
            print(angajat)

    def get_angajati_dep(self, departament):
        return list(filter(lambda ang: ang.departament == departament, self.lista_angajati))

    def crestere_salar(self, procent):
        # for ang in self.lista_angajati:
        #     ang.crestere_salar(procent)
        list(map(lambda a: a.crestere_salar(procent), self.lista_angajati))


angajati = Angajati()
angajati.adauga_angajati(
    Angajat("George", 1000, "HR"),
    Angajat("Alex", 2000, 'instalator')
)
angajati.detalii_angajat()

print(angajati.get_angajati_dep("HR"))

angajati.crestere_salar(8)
angajati.detalii_angajat()
