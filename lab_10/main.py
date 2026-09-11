# Завдання 1: Список чисел, сортування за зростанням
numbers_asc = [42, 12, 88, 3, 25]
numbers_asc.sort()
print("Сортування за зростанням:", numbers_asc)
print("-" * 30)

# Завдання 2: Список чисел, сортування за спаданням
numbers_desc = [42, 12, 88, 3, 25]
numbers_desc.sort(reverse=True)
print("Сортування за спаданням:", numbers_desc)
print("-" * 30)

# Завдання 3: Список слів, сортування в алфавітному порядку
words = ["яблуко", "апельсин", "вишня", "банан"]
words.sort()
print("Алфавітний порядок:", words)
print("-" * 30)

# Завдання 4: Список рядків, сортування за довжиною елементів
words_len = ["груша", "кавун", "ананас", "дим"]
words_len.sort(key=len)
print("Сортування за довжиною:", words_len)
print("-" * 30)

# Завдання 5: Зчитування 5 чисел з клавіатури та виведення у відсортованому порядку
user_numbers = []
for i in range(5):
    val = float(input(f"Введіть число {i + 1}: "))
    user_numbers.append(val)
sorted_user_numbers = sorted(user_numbers)
print("Відсортовані введені числа:", sorted_user_numbers)
print("-" * 30)

# Завдання 6: Сортування прізвищ за алфавітом та за довжиною
students = ["Шевченко", "Коваленко", "Бойко", "Франко", "Кравчук"]

students_alphabetical = sorted(students)
print("За алфавітом:", students_alphabetical)

students_by_length = sorted(students, key=len)
print("За довжиною прізвища:", students_by_length)