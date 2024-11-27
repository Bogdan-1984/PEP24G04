class Product:

    def __init__(self, name=None, price=None, stock=None):
        if name and price and stock:
            self.name = name
            self.price = price
            self.stock = stock
        else:
            self.name, self.price, self.stock = input("Give (name, price, stock) for product:").split(',')

    def __repr__(self):
        return f"{self.__class__.__name__}: ({self.name},{self.price},{self.stock})"

    def __str__(self):
        return (f"Nume: {self.name} \n"
                f"Pret: {self.price} \n"
                f"Stoc: {self.stock} \n"
                f"{40 * '-'}")


class Category:

    def __init__(self, name: str):
        self.category_name = name
        self.products = []

    def add_product(self):
        # product = input("give product:")
        product = Product()
        self.products.append(product)

    def __str__(self):
        return f"--- {self.category_name.capitalize()}"


class Shop:
    main_menu_message = 'Bun venit la magazinul Pycharm'
    main_menu_dict = {1: "Category", 2: "Produse", 3: "Iesire"}
    product_menu_dict = {1: "Adaugare", 2: "Vizualizare", 3: "Iesire la meniul principal"}
    categories = [Category('pantofi'), Category('haine')]

    def __show_menu(self, main_menu=True):
        if main_menu:
            print(self.main_menu_message)
            menu = self.main_menu_dict
        else:
            print(40 * '=' + '\n' + Product.__name__.upper().center(40, '=') + '\n' + 40 * '=')
            menu = self.product_menu_dict
        for key, value in menu.items():
            print(f'\t{key}: {value}')
        selection = input('Alegeti optiunea:')
        return selection

    def _add_product(self):
        category = input("Introduceti numele categoriei:")
        product = input("Introduceti numele produsului")
        price = input("Introduceti pretul produsului")
        stock = input("Introduceti stocul produsului")
        for cat in self.categories:
            if cat.category_name == category:
                cat.products.append(Product(product, price, stock))
                break
        else:
            new_cat = Category(category)
            new_cat.products.append(Product(product, price, stock))
            self.categories.append(new_cat)

    def products_menu(self):
        # code here
        while True:
            selection = self.__show_menu(main_menu=False)
            if selection == '1':
                self._add_product()
            elif selection == '2':
                for cat in self.categories:
                    print(40 * '=' + '\n' + "Categoria " + cat.category_name.capitalize() + '\n' + 40 * '=')
                    for prod in cat.products:
                        print(prod)
            elif selection == '3':
                break

    def run(self):
        while True:
            selection = self.__show_menu(main_menu=True)
            if selection == '1':
                print(40 * '=' + '\n' + Category.__name__.upper().center(40, '=') + '\n' + 40 * '=')
                for category in self.categories:
                    print(category)
            elif selection == '2':
                self.products_menu()
