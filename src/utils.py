import json
from typing import List

from src.models import Category, Product


def load_data_from_json(filename: str) -> List[Category]:
    """Загружает данные из JSON файла и создает объекты классов Category и Product."""
    try:
        with open(filename, 'r', encoding='utf-8') as file:
            data = json.load(file)
    except FileNotFoundError:
        print(f"Ошибка: Файл {filename} не найден")
        return []
    except json.JSONDecodeError:
        print(f"Ошибка: Неверный формат JSON в файле {filename}")
        return []

    categories = []

    for category_data in data:
        products = []

        # Создаем объекты продуктов для текущей категории
        for product_data in category_data.get('products', []):
            product = Product(
                name=product_data.get('name', ''),
                description=product_data.get('description', ''),
                price=product_data.get('price', 0.0),
                quantity=product_data.get('quantity', 0)
            )
            products.append(product)

        # Создаем объект категории
        category = Category(
            name=category_data.get('name', ''),
            description=category_data.get('description', ''),
            products=products
        )

        categories.append(category)

    return categories
