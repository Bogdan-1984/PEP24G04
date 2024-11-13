MENU = """
Meniu:
1. Vizualizare stoc
2. Adaugare produs
3. Stergere produs
4. Iesire
"""
ACTIONS = {'1': quit, '2': quit, '3': quit, '4': quit, }
STOCK = {}
print(MENU)
selection = input(':')
assert selection in ACTIONS
f = ACTIONS[selection]
f()
