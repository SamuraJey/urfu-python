# Создать декоратор simple_decorator с "хорошим поведением", то есть

# декоратор при котором происходит сохранение "магических" полей __name__  и  __doc__

# Должны проходиться тесты

import functools
from functools import wraps


def simple_decorator(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        name = args[0].__name__
        doc = args[0].__doc__
        answer = func(*args, **kwargs)
        answer.__name__ = name
        answer.__doc__ = doc
        return answer

    return wrapper


@simple_decorator
def my_simple_logging_decorator(func):
    def you_will_never_see_this_name(*args, **kwargs):
        print('calling1 {}'.format(func.__name__))
        return func(*args, **kwargs)

    return you_will_never_see_this_name


@my_simple_logging_decorator
def double(x):
    'Doubles a number.'
    return 2 * x


assert double.__name__ == 'double'
assert double.__doc__ == 'Doubles a number.'
print(double(155))
