# Завдання 1: Перевірка, чи введене число є додатним
num1 = float(input("Введіть число для перевірки на додатність: "))
if num1 > 0:
    print("Число є додатним")
print("-" * 30)

# Завдання 2: Визначення, чи введене число парне, чи непарне
num2 = int(input("Введіть ціле число: "))
if num2 % 2 == 0:
    print("Число парне")
else:
    print("Число непарне")
print("-" * 30)

# Завдання 3: Перевірка повноліття (18 років)
age = int(input("Введіть ваш вік: "))
if age >= 18:
    print("Ви досягли повноліття")
else:
    print("Ви ще неповнолітні")
print("-" * 30)

# Завдання 4: Зчитування двох чисел та виведення більшого з них
a = float(input("Введіть перше число: "))
b = float(input("Введіть друге число: "))
if a > b:
    print(f"Більше число: {a}")
elif b > a:
    print(f"Більше число: {b}")
else:
    print("Числа рівні")
print("-" * 30)

# Завдання 5: Оцінка (від 1 до 100) з використанням вкладених умов
score = int(input("Введіть оцінку (1-100): "))
if score >= 60:
    if score >= 90:
        print("Відмінно")
    else:
        print("Добре")
else:
    print("Незадовільно")
print("-" * 30)

# Завдання 6: Перевірка логіна та пароля
CORRECT_LOGIN = "admin"
CORRECT_PASSWORD = "password123"

user_login = input("Введіть логін: ")
user_password = input("Введіть пароль: ")

if user_login == CORRECT_LOGIN and user_password == CORRECT_PASSWORD:
    print("Вхід дозволено")
else:
    print("Доступ заборонено")