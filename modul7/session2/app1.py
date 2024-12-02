class EnumeratorCuvant:
    def __init__(self, cuvant: str):
        self.cuvant = cuvant
        self.i = 0

    def __iter__(self):
        return self

    def __next__(self):
        # todo
        return valoare


for i, litera in EnumeratorCuvant("alfabet"):
    print(f"{i}: {litera}")
