# Завдання 1: Три змінні різних типів (int, float, str)
age = 18
height = 1.75
name = "Олександр"

print(f"Змінна age: {age}, тип: {type(age)}")
print(f"Змінна height: {height}, тип: {type(height)}")
print(f"Змінна name: {name}, тип: {type(name)}")
print("-" * 30)

# Завдання 2: Конвертер кілометрів у метри
km = 12.5
meters = km * 1000
print(f"{km} км = {meters} м")
print("-" * 30)

# Завдання 3: Конвертер градусів Цельсія у Фаренгейти (F = C * 9/5 + 32)
celsius = 25
fahrenheit = celsius * 9 / 5 + 32
print(f"{celsius}°C = {fahrenheit}°F")
print("-" * 30)

# Завдання 4: Перетворення годин у хвилини та секунди
hours = 2.5
minutes = hours * 60
seconds = hours * 3600
print(f"{hours} год = {minutes} хв = {seconds} сек")
print("-" * 30)

# Завдання 5: Конвертер валют (UAH у USD)
usd_rate = 41.20  # курс обміну
uah_amount = 1000
usd_amount = uah_amount / usd_rate
print(f"{uah_amount} UAH = {usd_amount:.2f} USD (курс: {usd_rate})")
print("-" * 30)

# Завдання 6: Зчитування см та переведення у метри і кілометри
cm_input = float(input("Введіть значення у сантиметрах: "))
meters_from_cm = cm_input / 100
km_from_cm = cm_input / 100000
print(f"{cm_input} см = {meters_from_cm} м = {km_from_cm} км")