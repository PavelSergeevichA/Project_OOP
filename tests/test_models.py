from src.models import Product, Category


class TestProduct:
    """Тесты для класса Product"""

    def test_product_initialization(self):
        """Тест корректности инициализации объекта Product"""
        product = Product("Телефон", "Современный смартфон", 50000.0, 10)
        assert product.name == "Телефон"
        assert product.description == "Современный смартфон"
        assert product.price == 50000.0
        assert product.quantity == 10

    def test_product_attributes_types(self):
        """Тест типов атрибутов объекта Product"""
        product = Product("Ноутбук", "Игровой ноутбук", 75000.0, 5)
        assert isinstance(product.name, str)
        assert isinstance(product.description, str)
        assert isinstance(product.price, float)
        assert isinstance(product.quantity, int)

    def test_product_price_setter_valid(self):
        """Проверка сеттера цены с корректным значением."""
        product = Product("Тестовый", "Описание", 10.0, 1)
        product.price = 20.0
        assert product.price == 20.0

    def test_product_price_setter_invalid(self, capsys):
        """
        Проверка сеттера цены с некорректным значением.
        capsys используется для захвата вывода в консоль.
        """
        product = Product("Тестовый", "Описание", 10.0, 1)
        original_price = product.price
        product.price = -5.0

        # Проверяем, что цена не изменилась
        assert product.price == original_price

        # Проверяем, что в консоль вывелось правильное сообщение
        captured = capsys.readouterr()
        assert "Цена не должна быть нулевая или отрицательная" in captured.out


class TestCategory:
    """Тесты для класса Category"""

    def test_category_initialization(self):
        """Тест корректности инициализации объекта Category"""
        products = [
            Product("Мышь", "Компьютерная мышь", 1500.0, 20),
            Product("Клавиатура", "Механическая клавиатура", 4500.0, 15),
        ]
        category = Category("Периферия", "Компьютерная периферия", products)

        assert category.name == "Периферия"
        assert category.description == "Компьютерная периферия"


    def test_category_add_product(self):
        """Тест метода добавления продукта в категорию."""
        category = Category("Периферия", "Компьютерная периферия", [])
        initial_product_count = len(category._Category__products)
        new_product = Product("Мышь", "Компьютерная мышь", 1500.0, 20)
        category.add_product(new_product)

        assert len(category._Category__products) == initial_product_count + 1

