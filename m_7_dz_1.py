class Product:
    """Представляет товар с названием, весом и категорией."""
    def __init__(self, name : str, weight : float, category : str) -> None:
        """ Инициализирует товар."""
        self.name = name
        self.weight = weight
        self.category = category

    def __str__(self) -> str:
        """Возвращает строковое представление товара."""
        return f'{self.name}, {self.weight}, {self.category}'

class Shop:
    """Представляет магазин, который управляет товарами в файле."""
    def __init__(self) -> None:
        self.__file_name = "products.txt"

    def get_products(self) -> str:
        """Считывает и возвращает все товары из файла"""
        try:
            with open(self.__file_name, "r") as file:
                return file.read().strip()
        except FileNotFoundError:
            ""

    def add (self, *product) -> None:
        """Добавляет товары в файл, если их еще нет."""
        existing_products = set()
        try:
            with open(self.__file_name, "r") as file:
                existing_products = set(file.read().strip().split("\n"))
        except FileNotFoundError:
            pass

        with open(self.__file_name, "a") as file:
            for product in product:
                product_str = str(product)
                if product_str not in existing_products:
                    file.write(product_str + '\n')
                    existing_products.add(product_str)
                else:
                    print(f'Продукт {product_str} уже есть в магазине')


# Первый запуск
print("Первый запуск:")
s1 = Shop()
p1 = Product('Potato', 50.5, 'Vegetables')
p2 = Product('Spaghetti', 3.4, 'Groceries')
p3 = Product('Potato', 5.5, 'Vegetables')

print(p2)  # __str__

s1.add(p1, p2, p3)

print(s1.get_products())

print("\nВторой запуск:")
# Второй запуск для демонстрации обработки дубликатов
s2 = Shop()
s2.add(p1, p2, p3)

print(s2.get_products())

