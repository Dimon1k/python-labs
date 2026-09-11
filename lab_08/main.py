# Завдання 1: Числа від 1 до 10, вихід при 7 (break)
for i in range(1, 11):
    if i == 7:
        break
    print(i)
print("-" * 30)

# Завдання 2: Числа від 1 до 10 без парних чисел (continue)
for i in range(1, 11):
    if i % 2 == 0:
        continue
    print(i)
print("-" * 30)

# Завдання 3: Запит пароля з достроковим виходом (break)
CORRECT_PASS = "python123"
while True:
    user_pass = input("Введіть пароль: ")
    if user_pass == CORRECT_PASS:
        print("Пароль правильний! Доступ надано.")
        break
    print("Неправильний пароль. Спробуйте ще раз.")
print("-" * 30)

# Завдання 4: Сума чисел від 1 до 100 без кратних 5 (continue)
total_sum = 0
for i in range(1, 101):
    if i % 5 == 0:
        continue
    total_sum += i
print(f"Сума чисел від 1 до 100 (без кратних 5): {total_sum}")
print("-" * 30)

# Завдання 5: Непарні числа від 1 до 20 через while, continue та break
num = 0
while True:
    num += 1
    if num > 20:
        break
    if num % 2 == 0:
        continue
    print(num)
print("-" * 30)

# Завдання 6: Перше число понад 50, яке ділиться і на 3, і на 7
val = 51
while True:
    if val % 3 == 0 and val % 7 == 0:
        print(f"Перше число понад 50, яке ділиться на 3 і 7: {val}")
        break
    val += 1