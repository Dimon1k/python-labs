# Завдання 1: Кортеж із 5 чисел, перший та останній елементи
numbers_tuple = (10, 20, 30, 40, 50)
print("Перший елемент:", numbers_tuple[0])
print("Останній елемент:", numbers_tuple[-1])
print("-" * 30)

# Завдання 2: Кортеж з ім'ям та прізвищем у форматі "Прізвище Ім'я"
student_tuple = ("Тарас", "Шевченко")
print(f"{student_tuple[1]} {student_tuple[0]}")
print("-" * 30)

# Завдання 3: Словник з трьома парами та виведення всіх значень
student_dict = {"name": "Іван", "age": 20, "group": "КІ-21"}
print("Усі значення словника:", list(student_dict.values()))
print("-" * 30)

# Завдання 4: Додавання нової пари "ключ: значення" у словник
student_dict["city"] = "Львів"
print("Оновлений словник:", student_dict)
print("-" * 30)

# Завдання 5: Міні-словник перекладу з англійської на українську
dictionary = {
    "apple": "яблуко",
    "book": "книга",
    "cat": "кіт",
    "sun": "сонце",
    "python": "пайтон",
}
user_word = input("Введіть слово англійською: ").strip().lower()
if user_word in dictionary:
    print(f"Переклад: {dictionary[user_word]}")
else:
    print("Слово відсутнє у словнику.")
print("-" * 30)

# Завдання 6: Словник товарів та розрахунок загальної вартості покупки
products = {"хліб": 25.0, "молоко": 38.5, "яблука": 30.0, "сир": 120.0}

total_cost = 0.0
print("Каталог товарів та ціни за одиницю:")
for name, price in products.items():
    print(f"- {name}: {price} грн")

print("\nВведіть кількість для кожного товару:")
for name, price in products.items():
    qty = float(input(f"Кількість ({name}): "))
    total_cost += qty * price

print(f"\nЗагальна вартість покупки: {total_cost:.2f} грн")