#Декоратори:
#Напишіть декоратор, який логує аргументи та результати викликаної функції.

def log_args(func):
    def wrapper(*args, **kwargs):
        if not args:
            print(f"{func.__name__} з kwargs={kwargs}")
        elif not kwargs:
            print(f"{func.__name__} з args={args}")
        else:
            print(f"{func.__name__} з args={args}, kwargs={kwargs}")
        result = func(*args, **kwargs)
        print(f"Результат: {result}")
        return result
    return wrapper


@log_args
def greet(name="User", greeting="Привіт"):
    return f"{greeting}, {name}!"

greet(name="Alex")
greet("Alex")

@log_args
def test_func(a, b=10):
    return a + b


test_func(5, b=7)


#Створіть декоратор, який перехоплює та обробляє винятки, які виникають в ході виконання функції.


def exception(func):
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except Exception as e:
            print(f"Виняток у {func.__name__}: {e}")
            return None
    return wrapper

@exception
def get_element(lst, index):
    return lst[index]


get_element([1, 2, 3], 5)


@exception
def sum_values(a, b):
    return a + b


sum_values(10, "20")