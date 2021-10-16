# Задание_1

import re

EMAIL = re.compile(r'([a-z0-9_\.]+)@([a-z0-9]+\.[a-z]+)')


def email_parse(email):
    found_inf = EMAIL.findall(email)[0]
    if found_inf:
        name, adr = found_inf
    else:
        raise ValueError(f'wrong email: {email}')
    print(name, adr)


email_parse('someone@geekbrains.ru')

# Задание 3


from functools import wraps


def type_logger(func):
    @wraps(func)
    def wrapper(*args):
        for arg in args:
            print(f'{func.__name__}({arg}: {type(arg)})', end=', ')
        return func(*args)

    return wrapper


@type_logger
def calc_cube(*args):
    return list(map(lambda x: x ** 3, args))


a = calc_cube(5, 3)
print(a)
print(calc_cube.__name__)
print(calc_cube.__doc__)
