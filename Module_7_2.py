class Product:
    def __init__(self, name, weight, category):
        self.name = str(name)
        self.weight = float(weight)
        self.category = str(category)

    def __str__(self):
        return f"{self.name}, {self.weight}, {self.category}\n"

class Shop:
    __file_name = "products.txt"
    def get_products(self):
        with open(self.__file_name) as file:
            return file.read()
    def add(self, *products):
        for product in products:
            with open(self.__file_name, 'a') as file:
                file_old = self.get_products()
                if product.name in file_old:
                    print(f'Продукт {product.name} уже есть в магазине')
                else:
                    file.write(str(product))

s1 = Shop()
p1 = Product('Potato', 50.5, 'Vegetables')
p2 = Product('Spaghetti', 3.4, 'Groceries')
p3 = Product('Potato', 5.5, 'Vegetables')

print(p2)

s1.add(p1, p2, p3)

print(s1.get_products())