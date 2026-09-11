import math


# Завдання 1: Функція hello(name)
def hello(name):
    print(f"Привіт, {name}!")


hello("Іван")
hello("Олена")
hello("Максим")
print("-" * 30)


# Завдання 2: Функція square(x)
def square(x):
    return x**2


print("Квадрат числа 5:", square(5))
print("Квадрат числа 9:", square(9))
print("-" * 30)


# Завдання 3: Функція sum_numbers(a, b)
def sum_numbers(a, b):
    return a + b


print("Сума 12 + 8:", sum_numbers(12, 8))
print("-" * 30)


# Завдання 4: Функція max_of_two(a, b)
def max_of_two(a, b):
    return a if a > b else b


print("Більше з чисел 15 і 27:", max_of_two(15, 27))
print("-" * 30)


# Завдання 5: Функція convert(celsius)
def convert(celsius):
    return celsius * 9 / 5 + 32


c_temp = 25
print(f"{c_temp}°C у Фаренгейтах: {convert(c_temp)}°F")
print("-" * 30)


# Завдання 6: Функція circle(r)
def circle(r):
    area = math.pi * r**2
    length = 2 * math.pi * r
    return area, length


r_val = 5
s, l = circle(r_val)
print(f"Для радіуса {r_val}: площа = {s:.2f}, довжина = {l:.2f}")
print("-" * 30)


# Завдання 7: Функція is_even(n)
def is_even(n):
    return n % 2 == 0


print("Чи число 8 парне?", is_even(8))
print("Чи число 7 парне?", is_even(7))