# Напишите декоратор retry: 

# декоратор вызовает функцию, которая возвращает True/False для индикации успешного или неуспешного выполнения функции. При сбое декоратор должен подождать и повторить попытку выполнения функции. При повторных неудачах декоратор должен ждать дольше между каждой последующей попыткой. Если у декоратора заканчиваются попытки, он сдается и возвращает исключение

import time
import functools

def retry(max_attempts, wait_time):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            attempts = 0
            while attempts < max_attempts:
                result = func(*args, **kwargs)
                if result:
                    return result
                attempts += 1
                time.sleep(wait_time * attempts)
            raise Exception("Retry attempts exceeded")
        return wrapper
    return decorator

@retry(max_attempts=3, wait_time=1)
def test():
    i = 1
    print('test', i)
    i += 1
    return False

test()