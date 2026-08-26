import sqlite3

# Підключення к базі даних
conn = sqlite3.connect("data.db")
cursor = conn.cursor()
cursor.execute("PRAGMA foreign_keys = ON;")

# Створення таблиці
cursor.executescript(
    """
CREATE TABLE categories (
    category_id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    description TEXT
);

CREATE TABLE goods (
    goods_id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    description TEXT,
    price REAL NOT NULL DEFAULT 0.00,
    stock_quantity INTEGER DEFAULT 0,
    category_id INTEGER,
    created_at DATETIME DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (category_id) REFERENCES categories(category_id) ON DELETE SET NULL ON UPDATE CASCADE
);
"""
)
print("1. Таблиці 'categories' та 'goods' успішно створені.")

# Внесення даних в таблиці

categories_data = [
    ("Електроніка", "Прилади"),
    ("Побутова техніка", "Техніка для дому"),
    ("Друковані книги", "Електроні книги"),
]

cursor.executemany(
    "INSERT INTO categories (name, description) VALUES (?, ?);",
    categories_data,
)


goods_data = [
    ("Смартфон", "Преміум телефон", 999.99, 10, 1),
    ("Ноутбук", "Гральний ноутбук", 1499.50, 5, 1),
    ("Кавомашина", "Автоматична кавомашина", 450.00, 3, 2),
    ("Холодильник", "Двокамерний холодильник", 850.00, 2, 2),
    ("Книга 'Вивчаємо Python'", "Посібник з програмування", 35.00, 20, 3),
]

cursor.executemany(
    """
    INSERT INTO goods (name, description, price, stock_quantity, category_id)
    VALUES (?, ?, ?, ?, ?);
    """,
    goods_data,
)

conn.commit()

print("2. Дані вдало внесені в таблиці.")

# Виконання JOIN-запиту

join_query = """
SELECT 
    p.goods_id,
    p.name AS goods_name,
    p.price,
    c.name AS category_name
FROM goods p
JOIN categories c ON p.category_id = c.category_id;
"""

cursor.execute(join_query)
results = cursor.fetchall()

print("3. Результат JOIN-запиту:")
print("-" * 65)
print(f"{'ID':<4} | {'Назва товару':<20} | {'Ціна':<10} | {'Категорія':<15}")
print("-" * 65)

for row in results:
    goods_id, goods_name, price, category_name = row
    print(
        f"{goods_id:<4} | {goods_name:<20} | {price:<10.2f} | {category_name:<15}"
    )

print("-" * 65)

conn.close()