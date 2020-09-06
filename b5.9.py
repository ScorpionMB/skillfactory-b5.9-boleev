import time

# Принимаем количество запусков
def time_this(num_runs = 10):
    # Принимает обертываемую функцию
    def decorator(func):
        # Создаём функцию обертку для функции func()
        def wrap():
            avg_time = 0
            for n in range(num_runs):
                t0 = time.time()
                func()
                t1 = time.time()
                avg_time += (t1 - t0)
            avg_time /= num_runs
            print("Выполнение заняло %.6f секунды" % avg_time)
        # Возвращаем обёртку
        return wrap
    # Возвращаем декоратор
    return decorator

@time_this()
def f(): # функция последовательности Фибоначчи
    fib = [1, 2]
    fib_even = []
    a = 2
    _len = 0
    for i in fib:
        print(fib)
        if i % 2 == 0:
            _len += 1
            fib_even.append(i)
        a += i
        if a < 400000000000000000000:
            fib.append(a)
        else:
            break
f()







