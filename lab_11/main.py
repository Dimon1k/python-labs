# Завдання 1: Список із 10 чисел та зріз перших 5 елементів
nums10 = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
print("Перші 5 елементів:", nums10[:5])
print("-" * 30)

# Завдання 2: Список чисел від 1 до 10 та зріз усіх парних чисел
numbers = list(range(1, 11))
even_numbers = numbers[1::2]
print("Парні числа:", even_numbers)
print("-" * 30)

# Завдання 3: Виведення списку у зворотному порядку через зріз
original_list = [1, 2, 3, 4, 5]
reversed_list = original_list[::-1]
print("Зворотний порядок:", reversed_list)
print("-" * 30)

# Завдання 4: Об'єднання двох списків рядків
list1 = ["яблуко", "банан"]
list2 = ["вишня", "груша"]
combined_list = list1 + list2
print("Об'єднаний список:", combined_list)
print("-" * 30)

# Завдання 5: Повторення списку з 5 елементів тричі
five_items = [1, 2, 3, 4, 5]
repeated_list = five_items * 3
print("Повторений список:", repeated_list)
print("-" * 30)

# Завдання 6: Перевірка входження слова у список
word_list = ["python", "code", "lab", "college", "programming"]
user_word = input("Введіть слово для пошуку: ")
if user_word in word_list:
    print(f"Слово '{user_word}' є у списку!")
else:
    print(f"Слово '{user_word}' відсутнє у списку.")
print("-" * 30)

# Завдання 7: Min, max та sum елементів списку чисел
num_data = [15, 2, 89, 44, 7, 30]
print("Список чисел:", num_data)
print("Мінімальне значення:", min(num_data))
print("Максимальне значення:", max(num_data))
print("Сума елементів:", sum(num_data))