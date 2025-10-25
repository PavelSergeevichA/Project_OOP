class Product:
    """Класс с данными о продукте"""
    name: str
    description: str
    price: float
    quantity: int

    def __init__(self, name, description, price, quantity):
        """Метод для инициализации экземпляра класса. Задаем значения атрибутам экземпляра."""
        self.name = name
        self.description = description
        self.quantity = quantity
        self._price = 0.0
        self.price = price

    @property
    def price(self):
        """Возвращает приватное значение цены."""
        return self._price

    @price.setter
    def price(self, new_price):
        """Устанавливает новое значение цены с проверкой."""
        if new_price <= 0:
            print("Цена не должна быть нулевая или отрицательная")
        else:
            self._price = new_price

    @classmethod
    def new_product(cls, product_data: dict):
        """
        Класс-метод для создания экземпляра класса Product из словаря.
        Принимает словарь с данными товара и возвращает созданный объект класса.
        """
        return cls(
            name=product_data['name'],
            description=product_data['description'],
            price=product_data['price'],
            quantity=product_data['quantity']
        )


class Category:
    """Класс с категориями продуктов"""
    product_count = 0
    category_count = 0

    name: str
    description: str
    products: list

    def __init__(self, name, description, products):
        """Метод для инициализации экземпляра класса. Задаем значения атрибутам экземпляра."""
        self.name = name
        self.description = description
        self.__products = products

        Category.category_count += 1
        Category.product_count += len(products)

    def add_product(self, product):
        self.__products.append(product)
        Category.product_count += 1

    @property
    def products(self):
        for product in self.__products:
            print(f"{product.name}, {product.price} руб. Остаток: {product.quantity} шт.\n")
