def prime_numbers(n):
    yield 2  # 2 Первое простое число
    for i in range(3, n + 1):
        # Проверка на простоту, до корня из i (математический прикол)
        for j in range(2, int(i**0.5) + 1):
            if i % j == 0:
                break
        else:
            yield i




# for number in prime_numbers(100):
#     print(number)

print(type(next(range(10).__iter__())))