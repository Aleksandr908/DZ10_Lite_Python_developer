'''
1. **Проверка типа входных данных**: Функция сначала проверяет, является ли `data` словарем. Если нет, генерируется `TypeError`.
2. **Проверка ключа 'name'**: Если ключ отсутствует или его значение не является строкой, генерируется `ValueError`.
3. **Проверка ключа 'age'**: Аналогично, если ключ отсутствует или его значение не является положительным числом, также генерируется `ValueError`.
4. **Тестирование**: После определения функции представлены примеры тестирования с разными вариантами входных данных, включая корректные и некорректные случаи.
При желании можно любых проверок напихать не меняя структуру
'''

def validate_user_input(data):
    # Проверка, что data является словарем
    if not isinstance(data, dict):
        raise TypeError("Входные данные должны быть словарем.")

    # Проверка наличия ключа 'name'
    if 'name' not in data:
        raise ValueError("Отсутствует ключ 'name'.")
    if not isinstance(data['name'], str):
        raise ValueError("Значение для ключа 'name' должно быть строкой.")

    # Проверка наличия ключа 'age'
    if 'age' not in data:
        raise ValueError("Отсутствует ключ 'age'.")
    if not isinstance(data['age'], (int, float)) or data['age'] <= 0:
        raise ValueError("Значение для ключа 'age' должно быть положительным числом.")

    return True  # Если все проверки пройдены, возвращаем True


# Примеры тестирования функции

# Корректные данные
try:
    print(validate_user_input({"name": "Alice", "age": 30}))  # True
except Exception as e:
    print(f"Ошибка: {e}")

# Отсутствующий ключ 'name'
try:
    print(validate_user_input({"age": 30}))  # ValueError
except Exception as e:
    print(f"Ошибка: {e}")

# Некорректное значение для 'age' (строка)
try:
    print(validate_user_input({"name": "Alice", "age": "30"}))  # ValueError
except Exception as e:
    print(f"Ошибка: {e}")

# Некорректный тип входных данных (строка вместо словаря)
try:
    print(validate_user_input("не словарь"))  # TypeError
except Exception as e:
    print(f"Ошибка: {e}")

# Некорректное значение для 'age' (отрицательное число)
try:
    print(validate_user_input({"name": "Alice", "age": -5}))  # ValueError
except Exception as e:
    print(f"Ошибка: {e}")