def prime_numbers(n):
    yield 2
    for i in range(3, n + 1):
        for j in range(2, int(i**0.5) + 1):
            if i % j == 0:
                break
        else:
            yield i


a = prime_numbers(100)
for i in range(100):
    try:
        print(next(a))
    except StopIteration:
        break
