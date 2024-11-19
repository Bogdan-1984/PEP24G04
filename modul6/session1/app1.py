class Product:

    def __init__(self):
        self.name, self.price, self.stock = input("Give (name, price, stock) for product:").split(',')

    def __repr__(self):
        return (f"{self.__class__.__name__}: ({self.name},{self.price},{self.stock})")

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

    # ADD method to represent category and to convert to string


class Shop:
    main_menu_message = 'Bun venit la magazinul Pycharm'
    main_menu_dict = {1: "Category", 2: "Produse", 3: "Iesire"}
    categories = [Category('pantofi')]

    def run(self):
        while True:
            print(self.main_menu_message)
            for key, value in self.main_menu_dict.items():
                print(f'\t{key}: {value}')
            selection = input('Alegeti optiunea:')
            if selection == '1':
                for category in self.categories:
                    print(category)
