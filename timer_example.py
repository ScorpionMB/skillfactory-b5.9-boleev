# Импортируем класс из файла timer.py
from timer import TimeThis

# Пример использования как декоратора

# Задаём количество запусков
@TimeThis(20)
def f():
    for i in range(1000000):
        pass
f()

# Количество запусков по умолчанию
@TimeThis()
def f():
    for i in range(1000000):
        pass
f()

# Пример использования как контекстный менеджер
# Функция для теста
def f():
    for i in range(1000000):
        pass
# Запускаем тест
with TimeThis() as t:
    f()