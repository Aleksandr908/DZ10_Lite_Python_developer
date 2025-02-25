'''
1. **Класс `NegativeNumberError`**:
   - Наследует от встроенного класса `Exception`.
   - В конструкторе принимает значение числа и сообщение об ошибке. Сообщение по умолчанию указывает, что число не должно быть отрицательным.
   - Переопределяет метод `__str__`, чтобы возвращать информативное сообщение, которое включает значение, вызвавшее исключение.

2. **Функция `check_positive_number`**:
   - Принимает число в качестве аргумента.
   - Если число отрицательное, вызывает исключение `NegativeNumberError`.
   - Если число положительное, возвращает `True`.

3. **Тестирование**:
   - В первом блоке `try-except` проверяется поведение функции с отрицательным числом. Ожидается, что будет вызвано исключение, и его сообщение будет выведено.
   - Во втором блоке проверяется положительное число, которое должно вернуть `True`.
'''


# Определение класса NegativeNumberError
class NegativeNumberError(Exception):
    def __init__(self, value, message="Число не должно быть отрицательным."):
        self.value = value
        self.message = message
        super().__init__(self.message)

    def __str__(self):
        return f"{self.message} (Полученное значение: {self.value})"

# Функция, проверяющая, является ли число положительным
def check_positive_number(num):
    if num < 0:
        raise NegativeNumberError(num)
    return True  # Возвращаем True, если число положительное

# Примеры тестирования функции

# Тест с отрицательным числом
try:
    print(check_positive_number(-10))  # Должно вызвать исключение
except NegativeNumberError as e:
    print(f"Ошибка: {e}")

# Тест с положительным числом
try:
    print(check_positive_number(5))  # Должно вернуть True
except NegativeNumberError as e:
    print(f"Ошибка: {e}")