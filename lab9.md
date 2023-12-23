#Лабораторная работа №9.
##Генераторы
1.Программа, решающая задачу
Генератор, создающий пароли по определённым правилам.
```python
import random
import string
def generate_password(length=8):
    """
    Функция генерирует пароль заданной длины, состоящий
    из случайных символов верхнего и нижнего регистра, а также
    цифр и специальных символов.

    Параметры:
    - length (int): длина генерируемого пароля (по умолчанию 8)

    Возвращает:
    - str: сгенерированный пароль
    """
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for _ in range(length))
    return password
# Пример использования функции generate_password()
password = generate_password(12)
print(password)
```

2. Результаты решений:

![display:block;margin:auto|](111.png)
