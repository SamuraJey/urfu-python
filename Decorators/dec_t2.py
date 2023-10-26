import functools
import math
import random

from typing import List

# Модифицируйте код декоратора prime_filter
def prime_filter(func):
    """Дан список целых чисел, возвращайте только простые целые числа"""
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        primes = [num for num in result if is_prime(num)]
        return primes
    return wrapper

@prime_filter
def numbers(from_num, to_num):
    return [num for num in range(from_num, to_num)]

def is_prime(n):
  for i in range(2,int(math.sqrt(n))+1):
    if n % i == 0:
      return False
  return True

# вывод для примера
print(numbers(from_num=2, to_num=20)) 
