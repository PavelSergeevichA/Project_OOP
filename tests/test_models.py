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

    def test_product_with_zero_quantity(self):
        """Тест создания продукта с нулевым количеством"""
        product = Product("Планшет", "Графический планшет", 30000.0, 0)

        assert product.quantity == 0
        assert product.name == "Планшет"


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
        assert len(category.products) == 2
        assert isinstance(category.products, list)

    def test_category_with_empty_products(self):
        """Тест создания категории с пустым списком продуктов"""
        category = Category("Аксессуары", "Различные аксессуары", [])

        assert category.name == "Аксессуары"
        assert category.description == "Различные аксессуары"
        assert category.products == []
        assert len(category.products) == 0

    def test_category_attributes_types(self):
        """Тест типов атрибутов объекта Category"""
        category = Category("Техника", "Электронная техника", [])

        assert isinstance(category.name, str)
        assert isinstance(category.description, str)
        assert isinstance(category.products, list)


class TestCounters:
    """Тесты для подсчета количества продуктов и категорий"""

    def setup_method(self):
        """Сброс счетчиков перед каждым тестом"""
        Category.category_count = 0
        Category.product_count = 0

    def test_category_counter_single_category(self):
        """Тест счетчика категорий для одной категории"""
        initial_count = Category.category_count
        category = Category("Аудио", "Аудиотехника", [])

        assert Category.category_count == initial_count + 1
